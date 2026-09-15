# Don't Weld Today's Intelligence Into the System

> 发布日期:2026-09-15 · [中文](../zh/2026-09-15-别把今天的聪明焊死在系统里.md) | [English](../en/2026-09-15-dont-weld-todays-intelligence-into-the-system.md)

---

Recently, I was building a small piece of software by separating it into several independent parts.

Each part worked. One produced the right visual result. Another responded to input. A third recorded the data I needed. In isolation, every demo looked convincing.

Then I connected them.

The trouble started at the seams. One part expected a state that another part had not saved. A small timing change affected the interface. Fixing one edge case created a new dependency somewhere else.

Nothing was fundamentally impossible. The individual parts were still good. But I had crossed an invisible line: I was no longer proving that features could work. I was discovering whether they could keep working together.

That distinction matters even more with AI.

AI makes it remarkably cheap to produce another prompt, parser, retry rule, summary step, or fallback. Each addition can improve today's result. Yet each can also encode an assumption about today's model. If we keep doing this, we may build something impressive that nobody dares to change.

I call the future cost of those choices the coupling tax.

## A local improvement can become a system-wide debt

An AI agent is not just a model. It also has a harness: the surrounding code and rules that decide what context the model sees, which tools it may call, how errors are handled, when a task ends, and what gets remembered.

The harness often grows through reasonable decisions.

The model returns inconsistent formats, so we add a parser. The parser sometimes fails, so we add retries. Retries loop, so we add a stopping rule. The stopping rule ends useful work too early, so we add reflection. The context becomes too long, so we add compression. Compression drops an important detail, so we add another memory layer.

No single step looks foolish. That is precisely why coupling tax is hard to notice. We receive the performance gain now; the invoice arrives when the model, tool, workflow, or owner changes.

A recent paper, WHALE, makes the upside of coupling unusually clear. It alternates between updating model weights and searching for a better harness. On Qwen3.5 2B and 4B agents across search question answering, mathematical reasoning, and chess puzzles, it beat several one-sided optimization methods by 4.15 to 24.38 percentage points in best mean@8 accuracy. The important lesson is that agent capability does not live inside model weights alone. Model and harness shape what each other can do. [The paper also states its scope clearly: particular models, tasks, and evaluation settings.](https://arxiv.org/abs/2609.00196)

That result supports joint optimization in research. It does not prove that a production system should keep every layer in permanent co-evolution.

A benchmark rewards the score it measures. A living system pays for migration, maintenance, incidents, changing permissions, tool failures, and the day a better model arrives. The pair with the highest score today may be the hardest pair to separate tomorrow.

## Coupling is useful; invisible coupling is dangerous

I do not think the answer is to make everything generic.

If a task is frequent, stable, automatically verifiable, and valuable enough, close adaptation between a model and its harness can be a sensible investment. A specialized production line should fit its product.

The danger begins when temporary intelligence scaffolding is mistaken for permanent infrastructure.

Some scaffolding compensates for what a model cannot yet do: a special prompt, an extra reflection loop, a context reset, or a workaround for a formatting habit. Other parts protect the system regardless of which model is used: identity, permissions, event history, tool contracts, checkpoints, failure rules, and recovery.

The first category should be easy to question and remove. The second should survive model changes.

Anthropic described a concrete version of this problem in its engineering work. A context-reset strategy helped one model that tended to finish early near its context limit. A later model no longer showed the same behavior, so the old strategy became dead weight. In its Managed Agents architecture, the company separated the session log, harness, and sandbox so each could fail or be replaced independently. That architecture is one implementation, not a universal law, but the design principle is useful: preserve the record and the boundaries; let the intelligence layer change. [Anthropic's engineering account explains both the obsolete workaround and the decoupled interfaces.](https://www.anthropic.com/engineering/managed-agents)

This changes how I think about “building for the future.” It does not mean predicting the next model. Prediction is fragile. It means making replacement possible without losing the truth of what happened.

## Run a replacement rehearsal

There is a simple exercise I now find more useful than asking whether a system is “modular.” Take twenty minutes and pretend the current model disappears tomorrow.

Can another model—or a human—recover these five things?

- What task was requested?
- What actions were allowed?
- What has already happened?
- What state is the work in now?
- What evidence decides whether it is complete?

If the answers exist only inside the current conversation or inside a prompt tuned to one model's habits, the system has no durable memory. It merely has a long dependency.

Then choose one component and imagine replacing it: the model, a tool, the memory layer, or the evaluator. Do not ask whether the replacement performs equally well. Ask how long it takes before you can make a fair comparison. That time is a rough but practical measure of coupling tax.

Finally, give every model-specific patch an expiry label. Record three short lines:

- Which observed failure does this patch address?
- What evidence shows that it helps?
- What test would allow us to remove it?

This is small enough to do today. It also changes the direction of the system. A patch without a removal test tends to become geology. A patch with one remains a hypothesis.

## The system should remember more than the model

The promise of AI is not that we can pile up more clever instructions. It is that a person or small team can operate beyond their old limits.

But leverage compounds only when the system can absorb a better component without forgetting its own history. Otherwise, every model upgrade becomes a partial rebuild, and every clever workaround makes the next change more expensive.

So my standard is becoming stricter: optimize capability aggressively where the return is real, but keep the evidence, permissions, state, and recovery path outside any one model's personality.

Today's intelligence will age. That is normal.

The question is whether the system we build around it will be able to let it go.
