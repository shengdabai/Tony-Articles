# Your AI Needs a Spine

> 发布日期:2026-06-21 · [中文](../zh/2026-06-21-你的 AI 需要一根脊梁.md) | [English](../en/2026-06-21-ai-needs-a-spine.md)

---

Most people still talk to AI as if the main problem is persuasion.

They want a better prompt, a cleverer role-play, a sharper instruction, a magical sentence that makes the model finally understand. So they collect prompt templates, rewrite the same request ten ways, and treat every failure as a wording problem.

Sometimes wording does matter.

But the deeper problem is not that your AI does not understand you.

The deeper problem is that your AI has no spine.

It can answer. It can draft. It can summarize. It can code. It can imitate confidence beautifully. But unless you give it structure, it cannot reliably know when to stop, when to refuse, when to check, when to preserve evidence, when to ask reality for a verdict, or when to protect you from your own impatience.

That is why the next stage of using AI well is not "prompt engineering" in the narrow sense.

It is building the environment in which intelligence is allowed to move.

## Intelligence Without a Skeleton Collapses

A body without a skeleton does not become more flexible in a useful way. It collapses.

AI has a similar problem. The more capable it becomes, the more tempting it is to let it "just handle everything." This feels efficient at first. You give the model a broad goal, it produces pages of output, and the work appears to move.

But broad ability without boundaries creates a strange kind of softness.

The model says yes too easily. It fills gaps instead of exposing them. It often prefers a plausible continuation to an uncomfortable interruption. It can make the wrong action feel smooth.

For light work, that may be acceptable. For serious work, smoothness is not enough.

Serious work needs a spine: constraints, checks, memory, permissions, feedback loops, and consequences.

In software circles this is increasingly described as a harness: the surrounding system that turns raw model capability into controlled production. A recent essay on harness engineering describes the human role as steering the agent by improving both the feedforward controls and the feedback controls whenever the same issue happens repeatedly.[^1]

That phrase matters: whenever the same issue happens repeatedly.

Most people do the opposite. They get annoyed at the AI, correct it once, and then repeat the same annoyance tomorrow.

A spine begins when a mistake stops being a complaint and becomes part of the system.

## A Boundary Is Not Distrust

Many people misunderstand constraints. They hear "guardrail" and think it means fear, slowness, bureaucracy, or lack of trust.

But a boundary is not the opposite of trust. A boundary is what makes stronger trust possible.

The nuclear industry has a useful phrase for this: defense in depth. The U.S. Nuclear Regulatory Commission defines it as using multiple independent and redundant layers of defense to compensate for potential human and mechanical failures, so no single layer is exclusively relied upon.[^2]

That is a much better metaphor for AI than the fantasy of the perfect prompt.

A prompt is one layer.

But serious AI work needs more layers:

- a clear task definition;
- a limited tool set;
- file and data boundaries;
- automatic formatting and linting;
- tests that run without negotiation;
- logs that preserve what happened;
- review steps that do not grade their own homework;
- rules updated after repeated failures.

None of these layers says, "I do not trust AI."

They say, "This work matters enough that no single layer should carry the whole risk."

Claude Code's hook system is a practical example. Its documentation describes hooks as a way to run code at key points in the lifecycle: format files after edits, block commands before execution, send notifications, inject context at session start, and more.[^3] The important part is not the specific product. The important part is the shift in attitude.

Instead of begging the model to remember a rule, you move part of the rule into the environment.

You stop relying only on intention.

You create a consequence.

## Context Is a Room, Not a Dump Truck

Another mistake is thinking that more context always means better work.

Context matters enormously. But context is not the same as dumping everything into the model. A good work environment does not put every tool, every document, every memory, every half-finished idea, and every old argument on the table at once.

It arranges the room.

The Manus team wrote a useful post on context engineering for AI agents. Among their lessons: keep the prompt prefix stable, mask tools instead of constantly removing them, use the file system as external memory, keep objectives visible, and preserve errors so the agent can learn from failed attempts.[^4]

This is not just a technical optimization.

It is a philosophy of attention.

Good context engineering says:

Do not make the model omniscient. Make the next action clear.

Do not hide the failure. Preserve the evidence.

Do not keep changing the floor under its feet. Stabilize the environment.

Do not confuse "more information" with "more usable information."

This is very close to how humans learn.

A student does not become smarter because you throw the entire library onto the desk. A craftsperson does not improve because every tool is placed within reach at the same time. A writer does not get clearer because every old note is visible at once.

People improve when the environment gives them the right material, at the right moment, with enough friction to force attention.

AI is not exempt from this.

## The AI That Always Helps May Be Hurting You

Here is the uncomfortable part.

If your AI always helps you by removing friction, it may also be quietly weakening you.

It can help you avoid the very moments where learning happens: choosing, naming, testing, deleting, checking, admitting uncertainty, and waiting for evidence.

This is why "use AI to become stronger" is not a slogan. It is a design problem.

If AI writes the email, you may save time.

If AI helps you notice why the email is weak, you become sharper.

If AI summarizes the book, you may get the gist.

If AI forces you to compare the summary with your own prediction, you build judgment.

If AI generates code, you may get a feature.

If AI runs tests, shows failures, preserves the error trail, and pushes you to update the rule that caused the failure, you improve the system.

The difference is not whether AI is used.

The difference is whether AI removes the work or upgrades the loop.

An AI without a spine tends to become a comfort machine. It tells you that your vague idea is promising. It expands your half-thought into a polished paragraph. It turns hesitation into motion.

That can feel good.

But growth often starts where comfort ends.

The better AI system is not the one that always says yes. It is the one that can say:

This is underspecified.

This contradicts yesterday's rule.

This needs a source.

This touches private information.

This should be tested before it is published.

This looks done, but the evidence is weak.

That kind of AI is less flattering.

It is also more useful.

## From Prompt User to System Keeper

The real role shift is simple:

You are not merely a prompt user anymore.

You are the keeper of a system.

That sounds grand, but the daily practice is small. You do not need a complicated platform to begin. You can start with a very plain loop:

1. Write the task.
2. Define what must not happen.
3. Give the smallest necessary context.
4. Let AI produce a draft or action.
5. Run a check outside the model.
6. Record the failure.
7. Convert repeated failures into rules, tests, or hooks.

The last step is the important one.

If the AI makes a formatting mistake once, fix it.

If it makes the same formatting mistake three times, do not merely complain. Add a formatter, a checklist, or an automatic check.

If it leaks private detail once, remove it.

If the same risk appears again, add a privacy review step before publishing.

If it hallucinates sources once, correct the article.

If it happens repeatedly, require links before drafting the claim.

That is how a spine grows: not from theory, but from scar tissue becoming structure.

## The Dignity of Saying No

There is a deeper human lesson here.

We often think power means more ability: more output, more speed, more options, more automation. AI certainly gives us that.

But mature power is not only the ability to act.

It is also the ability to refuse.

To refuse fake completion.

To refuse vague confidence.

To refuse public polish without private evidence.

To refuse convenience when convenience quietly steals the training.

This is why the best AI setup is not the one that makes you feel like a magician. It is the one that helps you become a better operator of your own attention, judgment, and responsibility.

Your AI does not need a more charming personality.

It does not need to flatter you more smoothly.

It does not need to make every task feel frictionless.

It needs a spine.

And if you build that spine carefully, something interesting happens: the spine is not only for the machine.

It becomes yours too.

[^1]: Martin Fowler, "Harness engineering for coding agent users": https://martinfowler.com/articles/harness-engineering.html
[^2]: U.S. Nuclear Regulatory Commission, "Defense in depth": https://www.nrc.gov/reading-rm/basic-ref/glossary/defense-in-depth
[^3]: Anthropic Claude Code Docs, "Automate actions with hooks": https://docs.anthropic.com/en/docs/claude-code/hooks-guide
[^4]: Manus, "Context Engineering for AI Agents: Lessons from Building Manus": https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
