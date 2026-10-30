# Intelligence Needs a Harness

> 发布日期:2026-08-12 · [中文](../zh/2026-08-12-智能越强越需要缰绳.md) | [English](../en/2026-08-12-intelligence-needs-a-harness.md)

---

There is a seductive story about AI progress.

The model gets smarter. The prompts get shorter. The tools get simpler. The human writes fewer rules, applies less pressure, removes more scaffolding, and eventually the whole outer system disappears. Intelligence eats the wrapper. The machine becomes strong enough to need no harness.

This story feels right because part of it is true.

Weak models need heavy babysitting: rigid prompts, formatting rules, retries, examples, and defensive wrappers around every step. When the model improves, many of those local patches become unnecessary. A better model can infer intent, recover from small mistakes, choose tools more flexibly, and tolerate ambiguity. The bottom layer of the harness really does get thinner.

But this is only half the movement.

The other half is easier to miss: when intelligence becomes stronger, we ask it to enter larger, messier, longer, more valuable parts of work. It stops being a clever text box and starts touching files, tools, calendars, repositories, browsers, payments, workflows, teams, memory, and decisions. Then the problem is no longer "Can the model think?"

The problem becomes: can this intelligence act in the world without losing the plot, crossing the wrong boundary, or making the human weaker?

That is where the harness comes back. Not as prompt tricks, but as the operating layer around intelligence.

## The Harness Moves Up

By harness, I mean the runtime system that lets an AI model interact with reality in a stable, continuous, and accountable way.

It includes context management, tool access, memory, permissions, evaluation, observability, handoff, recovery, cost control, and the final human responsibility for what happens. Some of it is code. Some of it is workflow. Some of it is writing. Some of it is taste.

In early AI use, the harness lives close to the model. You tell it exactly what format to use. You paste examples. You ask it to reason step by step. You add retries because it forgets an instruction. You are compensating for raw capability gaps.

As models get better, that layer becomes less visible. But the work does not become simple. It moves upward.

Now the question is not whether one agent can write a decent answer. The question is whether several agents can divide a problem without duplicating work, whether a long-running task can resume after a tool fails, whether context can survive across sessions, whether sensitive operations require permission, whether the output can be evaluated, and whether the human can still understand what changed.

Anthropic's write-up on its multi-agent research system is a good public example. The architecture is not "one smarter model, no structure." It uses an orchestrator-worker pattern, separate subagents, memory for long research plans, citation processing, tool-use heuristics, evaluation rubrics, tracing, checkpoints, and deployment coordination.[^1] The stronger model did not remove the need for structure. It made a more ambitious structure worth building.

The article also reports a sober tradeoff: in their data, agentic systems used about four times as many tokens as chat, and multi-agent systems about fifteen times as many.[^1] When intelligence is connected to bigger tasks, it becomes an economic and operational design problem.

That is the real pattern. Capability reduces some local friction. Ambition expands the arena. The harness does not vanish. It migrates.

## Humans Proved This First

Human beings did not become more capable by becoming structure-free. As our brains became more powerful, we invented more external aids: language, writing, contracts, maps, schools, libraries, accounting, law, markets, scientific method, version control, project management, and organizations. They are all harnesses around human intelligence.

A smart person still needs a calendar. A serious team still needs norms. A company full of talented people still needs accounting, onboarding, access control, review, and governance. Civilization is not what happens when intelligence no longer needs structure. Civilization is what happens when intelligence becomes dense enough that structure becomes unavoidable.

The same is true in a personal life. The more capable you become, the more you need systems, not because you are weak, but because your possible actions multiply. More opportunities mean more ways to drift. More tools mean more hidden coupling. More output means more need for taste. More responsibility means more need for boundaries.

So the dream of "I will just talk to a superintelligent box and everything will be handled" is not serious enough. Even if the box becomes brilliant, the moment it touches your real work, it needs a world to operate in: files with names, tasks with owners, permissions with teeth, memory with pruning, tests with pass/fail signals, and a human who knows when to say no.

Intelligence without a harness is not freedom. It is exposure.

## The First Harness Is Attention

The smallest harness is not software. It is attention.

Where do you allow the AI to look? What do you allow it to touch? What counts as finished? What must it verify before acting? What should it never infer? What should it ask permission for? What kinds of work are you trying to become better at, rather than escape from?

These questions sound boring. That is why they matter.

Most people want the exciting layer: a new model, a new agent, a new demo that makes the future feel close. But compounding value usually lives in the dull layer: clear names, project rules, reusable context, decision records, tests, changelogs, tool boundaries, review loops, and pruned memory.

Claude Code's own documentation points in this direction. It treats memory as something deliberately stored in project and user instruction files, not as a mystical cloud of perfect recall.[^2] Its hooks system lets teams run deterministic commands at lifecycle events, such as before a tool is used or after a file is edited.[^3] Its best-practices guide emphasizes custom commands, specific context, screenshots, and iterative workflows.[^4]

None of this is glamorous. All of it is harness.

A folder is a harness. A naming convention is a harness. A checklist is a harness. A test is a harness. A budget is a harness. A permission dialog is a harness. A rule that says "do not publish until facts are checked" is a harness. A rule that says "do not let private material leak into public writing" is also a harness.

These are not signs of distrust in intelligence. They are signs of respect for consequences.

## Do Not Offload Judgment

There is one boundary I keep returning to: AI should reduce the burden of execution without deleting the growth of judgment.

If AI helps you search more widely, but you still decide what matters, the system can strengthen you. If AI drafts alternatives and forces you to compare, it can sharpen taste. If AI runs tests and shows failures, it can make standards more concrete. If AI remembers messy details so you can think at a higher level, it is doing useful cognitive offloading.

But if AI chooses the goal, defines the standard, selects the evidence, writes the conclusion, performs the verification, and tells you that everything is fine, you have not gained a colleague. You have lost the pressure that forms skill.

This is dangerous because the loss feels efficient. The page fills faster. The task list moves. Friction disappears. You feel upgraded. Yet the place where your judgment should have been exercised has gone quiet. You are not becoming a stronger producer. You are becoming a better requester of plausible output.

That is not enough.

In an AI age, the valuable person is not the one who can make the machine speak. Everyone will be able to do that. The valuable person is the one who can build an environment where machine intelligence must meet reality: clean inputs, dense context, bounded tools, fast feedback, sharp standards, and human responsibility.

The harness is not there to make AI obedient for its own sake. The harness is there to keep intelligence in contact with truth.

## Thin Where Possible, Thick Where Necessary

This argument can be overdone. Some people hear "harness" and immediately build a bureaucracy around a toy problem: too many agents, roles, protocols, dashboards, and process. The system becomes impressive from the outside and slow from the inside. That is not engineering. That is decoration.

The better rule is: thin where possible, thick where necessary.

Use the model's strength to delete unnecessary local scaffolding. Stop writing ritual prompts if the model no longer needs them. Stop over-specifying formats when a simple instruction works. Stop keeping workflows that exist only because last year's model was brittle.

But become more serious about the higher layers. When money can be spent, add permission. When private data can be exposed, add boundaries. When the task spans days, add memory and checkpoints. When multiple agents work in parallel, add division of labor and merge rules. When output will be public, add fact checking and privacy review. When the work affects other people, add accountability.

This is not a contradiction. It is maturity.

Children need rules because they are weak. Adults need rules because they are powerful.

AI is crossing the same line.

## The Personal Version

The most useful question for an individual is smaller than "How do I build a grand AI system?" It is: where is my harness missing?

If you ask AI for ideas every day but never save the few that survive contact with reality, your memory harness is missing. If you generate drafts but never compare them against a standard, your evaluation harness is missing. If you automate work but cannot explain what changed, your observability harness is missing. If you let the model touch private material and then publish quickly, your boundary harness is missing. If you keep opening new tools but rarely ship public artifacts, your priority harness is missing. If AI makes you faster but not more honest, your human harness is missing.

The answer does not have to be complicated. Start with one project folder. Put the rules, source material, outputs, review checklist, and failures there. Make the machine work inside a small world you can inspect.

Then let the world grow.

This is how ordinary people can use AI without being swallowed by it. Not by waiting for a perfect model. Not by chasing every new interface. Not by pretending structure is old-fashioned.

By building a small operating system around their own attention.

## The First Harness Is You

The strange thing about AI is that the more powerful it becomes, the more it reveals the quality of the environment around it. A weak model exposes its own limits. A strong model exposes yours: whether your goals are clear, whether your knowledge is organized, whether your standards are real, whether your workflows can survive speed, and whether you know what should remain human.

So the question "Will the harness disappear?" is probably the wrong question.

Some harnesses will disappear: the clumsy ones, the compensations for weak models, the prompt hacks, the rituals, the scaffolds that existed only because the machine could not yet walk.

But the deeper harness will remain, and in many places it will become thicker. It will be less visible because it will be built into tools, teams, folders, permissions, memory, contracts, and habits. Like roads, law, and language, the best harnesses eventually feel like the world itself.

That is not the disappearance of structure. That is structure becoming natural.

The future does not belong to people who remove every constraint from intelligence. It belongs to people who know which constraints make intelligence real.

Your AI does not need a longer prompt. It needs a world where it can act, fail, be checked, remember, hand off, recover, and answer to a standard.

In other words, intelligence needs a harness.

And the first harness is still you.

[^1]: Anthropic, "How we built our multi-agent research system," June 13, 2025. https://www.anthropic.com/engineering/multi-agent-research-system
[^2]: Anthropic, "How Claude remembers your project." https://code.claude.com/docs/en/memory
[^3]: Anthropic, "Hooks reference." https://code.claude.com/docs/en/hooks
[^4]: Anthropic, "Best practices for Claude Code." https://code.claude.com/docs/en/best-practices
