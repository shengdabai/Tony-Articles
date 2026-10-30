# Taste Must Become a Test

> 发布日期:2026-08-13 · [中文](../zh/2026-08-13-品味要长成测试.md) | [English](../en/2026-08-13-taste-must-become-a-test.md)

---

Before a machine can do good work, someone has to define what good work is.

This sounds obvious. It is also the part most people skip.

When people talk about AI progress, they usually talk about the model: which model is smarter, which one is cheaper, which one reasons longer, which one uses tools better, which one writes cleaner code, which one answers like a person. The model is visible, dramatic, and easy to compare. It gives us a scoreboard.

But in the parts of work that actually matter, the hard question is often not "Can AI generate an answer?" The hard question is "Who knows how to tell whether this answer is any good?"

That second question is where the future is moving.

The next advantage will not belong only to the people with the largest model. It will belong to the people who can turn domain taste into tests: rubrics, examples, edge cases, review loops, private standards, failure memories, and living environments where the machine has to meet reality.

In other words, judgment has to leave your head and become part of the system.

## The Real Work Starts Before Automation

One of the most interesting AI company patterns right now is not "we built a better chatbot." It is "we built a better way to evaluate work."

Harvey's Legal Agent Benchmark is a useful example. Its launch version included more than 1,200 agent tasks across 24 legal practice areas, evaluated by more than 75,000 expert-written rubric criteria.[^1] The open-source repository describes LAB as a benchmark for evaluating agents on real legal work in realistic environments.[^2]

The exact legal details are not the point for most of us. The deeper pattern is the point.

Legal work is full of hidden standards. A memo is not good because it sounds confident. A contract review is not good because it finds many issues. A diligence summary is not good because it is long. It is good only if it catches the right risks, respects the factual record, cites the right material, understands what matters to the client, and knows when uncertainty should be escalated instead of beautified.

That kind of quality is not sitting in a public dataset waiting to be scraped. It lives in experts' heads, in review comments, in mistakes that hurt, in partner preferences, in institutional memory, in boring checklists, and in thousands of small distinctions that outsiders do not even know to ask about.

So the first serious act is not automation. It is definition.

What counts as a correct answer? What counts as a dangerous miss? What must always be cited? What is a minor formatting problem versus a substantive failure? What kinds of uncertainty require human review? Which examples are easy, which are deceptive, and which reveal whether the system actually understands the work?

Until those questions are answered, "AI for this field" is mostly theater. You can generate outputs, but you cannot build trust. You can ship demos, but you cannot improve systematically. You can say the model feels good, but you cannot tell whether it is becoming useful.

Taste that cannot be inspected cannot compound.

## Benchmarks Are Not Just Scoreboards

People often treat benchmarks as scoreboards. Model A beats Model B by three points. Company X climbs the leaderboard. A new release makes the old chart obsolete.

That is the shallow use.

A serious benchmark is not merely a ranking device. It is a definition of what the field is trying to become.

ImageNet did not matter only because it let researchers compare computer vision models. Its challenge explicitly evaluated object detection and image classification at large scale, giving a scattered field a shared target and a shared language for progress.[^3] LegalBench did something similar for legal reasoning: it collected 162 tasks across six types of legal reasoning, built with legal professionals, so lawyers and model developers could talk about capabilities with more precision.[^4]

The benchmark says: this is what we believe deserves attention.

That is powerful because attention becomes investment. Investment becomes tools. Tools become habits. Habits become the shape of the field.

This is also why a benchmark is dangerous.

Goodhart's Law is usually summarized as: when a measure becomes a target, it stops being a good measure.[^5] Once a test becomes important, people optimize for the test. Models learn the shape of the exam. Companies select examples that flatter them. Teams confuse passing the benchmark with doing the job.

So the answer is not "use benchmarks blindly." The answer is "build better, living standards."

A real standard must keep moving toward reality. It should include obvious cases and ugly cases. It should measure results and process. It should combine automated scoring with expert review. It should preserve examples of failure. It should know when a single metric is too fragile. It should be updated when users change, tools change, and the work itself changes.

The goal is not to freeze taste into a dead checklist.

The goal is to give taste a body.

## Most People Still Keep Their Standards Private

This is where the lesson becomes personal.

Many people say they want to use AI seriously. But their standards are still private, vague, and emotional.

They know a good article when they see one, but they have never written down what makes it good. They know a useful report when they receive one, but they have no checklist for checking it. They know a student, customer, or reader is confused, but they have not captured the patterns of confusion. They know an AI answer is "not quite right," but they cannot name the failure.

So every interaction starts over.

The model produces something. The human reacts. The human edits. The human feels tired. The model learns little or nothing from that local correction. The next day, the same flaw returns in a slightly different coat.

This is not an AI limitation. It is a standard-capture limitation.

If your taste stays in your nervous system, AI can only borrow it moment by moment. If your taste becomes examples, rules, rubrics, tests, and review notes, AI can work inside it. More importantly, you can improve it.

The first version will be crude. That is fine. A crude rubric is better than a mysterious frown. A rough checklist is better than "make it better." A saved failure is better than a forgotten annoyance. A small test set is better than a thousand vibes.

The key is to make judgment external enough that it can be reused.

This does not make you less human. It makes your humanity operational.

## The New Craft Is Writing Standards

In the pre-AI world, craft often lived in execution. The person who could write the paragraph, build the spreadsheet, draft the contract, edit the video, or debug the code had the advantage.

Execution still matters. But AI is pushing more and more execution into the machine. When that happens, the craft moves upward.

The valuable skill becomes the ability to say:

This is the goal.

This is what good looks like.

These are the common traps.

These are the examples worth imitating.

These are the errors that look small but matter.

These are the facts that must be checked.

These are the boundaries we do not cross.

This is how we know the work is done.

That is not "prompting" in the shallow sense. It is standard design.

For an individual, this might be a personal writing checklist, a folder of strong and weak examples, a private style guide, or a review ritual after each public piece. For a small business, it might be a service delivery rubric, an onboarding standard, a support response library, or a set of before-and-after examples. For a team, it might be test cases, acceptance criteria, incident reviews, and decision records.

The form is not important. The loop is important.

Do the work. Review the work. Name the failure. Update the standard. Make the next run inherit the lesson.

That loop is how taste becomes infrastructure.

## The Risk: Dead Standards

There is a trap here.

Once people hear "rubric" and "benchmark," they may build a little bureaucracy. Everything gets a score. Every score gets a dashboard. Every dashboard gets a weekly meeting. Eventually the system is full of measurement, but empty of judgment.

Dead standards are worse than no standards because they create fake confidence.

A dead standard rewards what is easy to count. It stays unchanged after reality changes. It treats edge cases as noise. It punishes the person who notices the test is wrong. It makes the work look objective while quietly narrowing the work.

This is especially dangerous with AI. Machines are very good at satisfying visible criteria while missing invisible meaning. If your rubric is shallow, the model will become shallow at scale. If your examples are stale, the model will imitate yesterday's world. If your tests never include the weird cases, the system will look reliable until the first real mess arrives.

So the standard itself needs a standard.

Does it catch the failures that actually matter? Does it protect the user, not just the provider? Does it include cases where the right answer is "I cannot safely answer"? Does it make room for expert disagreement? Does it get updated after mistakes? Does it teach the human something, or only grade the machine?

The best standards do not remove judgment. They concentrate it.

## Your Small Benchmark

Most people do not need to build a public benchmark. They need a small private one.

Take one kind of work you repeat: writing, research, coaching, sales, design review, planning, coding, studying. Collect ten examples: three strong, three weak, three tricky, one embarrassing failure. For each, write down what makes it strong or weak. Then turn those observations into a review checklist.

Do not make it beautiful. Make it usable.

The next time AI helps you produce that kind of work, run the output against the checklist. When it fails, do not only fix the output. Fix the checklist. Add the failure. Add the missing distinction. Add the example that would have caught it.

After a few cycles, something changes. You stop asking AI to "make it better." You start giving it a world where better has meaning.

This is how ordinary people build leverage without becoming passive. You are not asking the machine to replace your judgment. You are forcing your judgment to become clearer than it used to be.

That is uncomfortable. It exposes the places where your taste was only a mood, where your standards were borrowed, where your confidence depended on not being asked to explain yourself.

Good.

AI should not only make you faster. It should make your standards visible.

## Define Good First

The lazy version of AI is: let the machine do the work so I do not have to think.

The strong version is: let the machine do more of the execution so I am forced to define the work more clearly.

That difference decides whether AI makes you weaker or stronger.

If you skip the standard, you become a consumer of plausible output. If you build the standard, you become the designer of a system. If you improve the standard every time reality pushes back, you build a compounding asset.

This is true for companies, but it is also true for one person with a notebook and a folder.

The future will contain stronger models. That part is obvious. The less obvious part is that stronger models will make weak standards more expensive. Bad taste will scale. Vague goals will scale. Hidden assumptions will scale. Sloppy review will scale.

So the work in front of us is not only to learn new tools.

It is to write down what we mean by good.

Taste must become a test.

Not because tests are the highest form of intelligence, but because a test is one way judgment survives contact with repetition.

And in an age when machines can repeat almost anything, the person who can define, inspect, and improve the standard is no longer just a user.

That person is building the field the machine has to live inside.

[^1]: Harvey, "Introducing Harvey's Legal Agent Benchmark," 2026. https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark
[^2]: Harvey AI, "harvey-labs" GitHub repository. https://github.com/harveyai/harvey-labs
[^3]: ImageNet, "ImageNet Large Scale Visual Recognition Challenge." https://www.image-net.org/challenges/LSVRC/
[^4]: NeurIPS Proceedings, "LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models." https://proceedings.neurips.cc/paper_files/paper/2023/hash/89e44582fd28ddfea1ea4dcb0ebbf4b0-Abstract-Datasets_and_Benchmarks.html
[^5]: Goodhart's Law overview. https://en.wikipedia.org/wiki/Goodhart%27s_law
