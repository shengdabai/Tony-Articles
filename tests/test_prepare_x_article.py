import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import call, patch


SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "prepare_x_article.py"
SPEC = importlib.util.spec_from_file_location("prepare_x_article", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def sample_article(**updates):
    article = {
        "date": "2026-08-20",
        "slug": "safe-output",
        "title": "Safe output",
        "body": "A useful opening paragraph with enough detail to be readable.",
        "footnotes": [],
        "thesis": "A useful opening paragraph with enough detail to be readable.",
        "sections": [],
        "tagline": "Safe output",
    }
    article.update(updates)
    return article


class PrepareXArticleTests(unittest.TestCase):
    def test_external_command_retries_and_preserves_last_error(self):
        errors = [
            subprocess.CalledProcessError(128, ["git"], stderr="first failure"),
            subprocess.CalledProcessError(128, ["git"], stderr="final failure"),
        ]

        with (
            patch.object(MODULE.subprocess, "run", side_effect=errors),
            patch.object(MODULE.time, "sleep") as sleep,
        ):
            with self.assertRaisesRegex(RuntimeError, "failed after 2 attempts: final failure"):
                MODULE.run_external_with_retry(
                    ["git", "clone"], description="GitHub article sync", timeout=1, attempts=2
                )

        sleep.assert_called_once_with(MODULE.RETRY_DELAYS_SEC[0])

    def test_imagegen_404_is_summarized_without_dumping_logs(self):
        error = subprocess.CalledProcessError(
            7,
            ["gen.sh"],
            stderr="prompt details\nimage generation failed: http 404 Not Found",
        )

        self.assertEqual(
            MODULE.external_error_detail(error),
            "imagegen service returned HTTP 404; GPT Image 2 is unavailable for this Codex session",
        )

    def test_sync_retries_clone_after_removing_partial_checkout(self):
        with tempfile.TemporaryDirectory() as directory:
            work_dir = Path(directory)
            clone_dir = work_dir / "repo"
            clone_attempts = 0

            def flaky_clone(command, **_kwargs):
                nonlocal clone_attempts
                if command[1] == "clone":
                    clone_attempts += 1
                    if clone_attempts == 1:
                        clone_dir.mkdir()
                        (clone_dir / "partial").write_text("incomplete", encoding="utf-8")
                        raise subprocess.CalledProcessError(128, command, stderr="connection reset")
                    self.assertFalse((clone_dir / "partial").exists())
                    article_dir = clone_dir / "articles" / "en"
                    article_dir.mkdir(parents=True)
                    (article_dir / "2026-08-20-recovered.md").write_text("# Recovered", encoding="utf-8")
                return subprocess.CompletedProcess(command, 0)

            with (
                patch.object(MODULE.subprocess, "run", side_effect=flaky_clone),
                patch.object(MODULE.time, "sleep") as sleep,
            ):
                files = MODULE.sync_2026_articles(work_dir)

        self.assertEqual([path.name for path in files], ["2026-08-20-recovered.md"])
        self.assertEqual(clone_attempts, 2)
        sleep.assert_has_calls([call(MODULE.RETRY_DELAYS_SEC[0])])

    def test_gpt_image_retries_after_transient_generator_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory) / "cover.png"
            attempts = 0

            def flaky_generation(command, **_kwargs):
                nonlocal attempts
                attempts += 1
                raw = Path(command[command.index("--out") + 1])
                if attempts == 1:
                    raw.write_bytes(b"partial")
                    raise subprocess.CalledProcessError(5, command, stderr="temporary service failure")
                self.assertFalse(raw.exists())
                raw.write_bytes(b"generated-image")
                return subprocess.CompletedProcess(command, 0)

            def fake_crop(src, target, _width, _height):
                target.write_bytes(src.read_bytes())

            with (
                patch.object(MODULE.subprocess, "run", side_effect=flaky_generation),
                patch.object(MODULE, "crop_to_size", side_effect=fake_crop),
                patch.object(MODULE.time, "sleep") as sleep,
            ):
                MODULE.gpt_image("prompt", out, 3000, 1200, 1, False)
            output_bytes = out.read_bytes()

        self.assertEqual(attempts, 2)
        self.assertEqual(output_bytes, b"generated-image")
        sleep.assert_called_once_with(MODULE.RETRY_DELAYS_SEC[0])

    def test_sources_are_deduplicated_in_markdown_and_rich_copy(self):
        article = sample_article(
            body="Intro paragraph.\n\n## Sources\n\n- [Primary](https://example.test/source)\n- [Primary](https://example.test/source)",
            footnotes=["[Primary](https://example.test/source)"],
        )

        markdown = MODULE.x_article_markdown(article)
        rich_html, _, _ = MODULE.x_article_copy_files(article)
        article_html, _ = MODULE.render_copy_article_body(article)

        self.assertEqual(markdown.count("Primary"), 1)
        self.assertEqual(markdown.count("**Sources**"), 1)
        self.assertEqual(rich_html.count('class="sources"'), 1)
        self.assertEqual(article_html.count("Primary (https://example.test/source)"), 1)

    def test_sources_end_at_next_heading_and_preserve_appendix(self):
        article = sample_article(
            body=(
                "Intro paragraph.\n\n## Sources\n\n- [Primary](https://example.test/source)"
                "\n\n## Appendix\n\nThis appendix remains part of the article."
            ),
        )

        markdown = MODULE.x_article_markdown(article)
        article_html, _ = MODULE.render_copy_article_body(article)

        self.assertIn("**Appendix**", markdown)
        self.assertIn("This appendix remains part of the article.", markdown)
        self.assertIn("<h2>Appendix</h2>", article_html)
        self.assertEqual(article_html.count("Primary (https://example.test/source)"), 1)

    def test_source_dedupe_prefers_canonical_url_and_first_display(self):
        sources = [
            "1. [First display](https://EXAMPLE.test/source/#part)",
            "[^2]: [Different label](https://example.test/source)",
            "3. https://example.test/source/",
        ]

        self.assertEqual(MODULE.dedupe_sources(sources), ["First display (https://EXAMPLE.test/source/#part)"])

    def test_inline_script_data_cannot_be_terminated_by_article_content(self):
        payload = "</script><script>globalThis.pwned = true &\u2028\u2029</script>"
        article = sample_article(title=payload, body=f"Opening {payload}", thesis=payload)

        rich_html, _, _ = MODULE.x_article_copy_files(article)

        self.assertEqual(rich_html.count("</script>"), 1)
        self.assertNotIn(payload, rich_html)
        self.assertIn("\\u003c/script\\u003e\\u003cscript\\u003e", rich_html)

        serialized = MODULE.inline_js_json(payload)
        self.assertIn("\\u0026", serialized)
        self.assertIn("\\u2028", serialized)
        self.assertIn("\\u2029", serialized)
        self.assertEqual(json.loads(serialized), payload)

    def test_no_textutil_means_no_rtf_asset(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(MODULE.shutil, "which", return_value=None):
            package_dir = Path(directory)
            self.assertFalse(MODULE.save_x_article_copy_assets(sample_article(), package_dir))
            self.assertFalse((package_dir / "_meta" / "x-article-copy.rtf").exists())

    def test_failed_rtf_conversion_is_omitted_from_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "2026-08-20-safe-output.md"
            source.write_text("# Safe output\n\nA useful opening paragraph with enough detail to be readable.", encoding="utf-8")

            def save_placeholder(_article, output):
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_bytes(b"placeholder")

            with (
                patch.object(MODULE, "READY_DIR", root / "ready"),
                patch.object(MODULE, "save_svg_cover", side_effect=save_placeholder),
                patch.object(MODULE, "save_svg_ending", side_effect=save_placeholder),
                patch.object(MODULE.shutil, "which", return_value="/usr/bin/textutil"),
                patch.object(
                    MODULE.subprocess,
                    "run",
                    side_effect=subprocess.CalledProcessError(1, ["textutil"]),
                ),
            ):
                package_dir = MODULE.package_article(source, "svg", 1, False)

            manifest = json.loads((package_dir / "manifest.json").read_text(encoding="utf-8"))
            self.assertNotIn("rtf_article_copy", manifest)
            self.assertFalse((package_dir / "_meta" / "x-article-copy.rtf").exists())

    def test_empty_rtf_output_is_omitted_from_manifest_and_readme(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "2026-08-20-safe-output.md"
            source.write_text("# Safe output\n\nA useful opening paragraph with enough detail to be readable.", encoding="utf-8")

            def save_placeholder(_article, output):
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_bytes(b"placeholder")

            def create_empty_rtf(command, **_kwargs):
                output = Path(command[command.index("-output") + 1])
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_bytes(b"")
                return subprocess.CompletedProcess(command, 0)

            with (
                patch.object(MODULE, "READY_DIR", root / "ready"),
                patch.object(MODULE, "save_svg_cover", side_effect=save_placeholder),
                patch.object(MODULE, "save_svg_ending", side_effect=save_placeholder),
                patch.object(MODULE.shutil, "which", return_value="/usr/bin/textutil"),
                patch.object(MODULE.subprocess, "run", side_effect=create_empty_rtf),
            ):
                package_dir = MODULE.package_article(source, "svg", 1, False)

            manifest = json.loads((package_dir / "manifest.json").read_text(encoding="utf-8"))
            readme = (package_dir / "_meta" / "README.md").read_text(encoding="utf-8")
            self.assertNotIn("rtf_article_copy", manifest)
            self.assertIn("RTF fallback was not generated", readme)
            self.assertEqual((package_dir / "_meta" / "x-article-copy.rtf").stat().st_size, 0)


if __name__ == "__main__":
    unittest.main()
