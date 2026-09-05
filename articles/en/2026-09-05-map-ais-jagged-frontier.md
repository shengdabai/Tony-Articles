# Stop Asking How Smart AI Is. Map Its Jagged Frontier.

> 发布日期:2026-09-05 · [中文](../zh/2026-09-05-别再问AI有多强先画出它的能力地形图.md) | [English](../en/2026-09-05-map-ais-jagged-frontier.md)

---

We keep asking the same question whenever a new model arrives: How smart is it?

The question sounds reasonable, but it hides a dangerous assumption. It treats intelligence as a single number and an AI model as a person whose competence transfers smoothly from one task to the next. If someone can solve a hard equation, we expect them to handle an easier calculation. If someone can write a good strategy memo, we assume they can summarize a straightforward meeting.

AI does not behave so neatly.

A model can reorganize a dense brief into a clear plan, then miss an obvious constraint in the same document. It can navigate a large codebase and still invent a source link. It can produce a polished answer to both tasks, using the same confident voice, even though one answer sits on a peak of competence and the other over a hidden valley.

That is why “How smart is AI?” is the wrong question. The better question is: Where is this system strong, for this task, under these conditions—and how do we know?

## Intelligence Is a Landscape, Not a Score

Researchers have a useful name for this problem: the jagged technological frontier.

In a field experiment involving 758 consultants, researchers from Harvard Business School and several other institutions, working with Boston Consulting Group, found that AI significantly improved performance on tasks that sat inside its capability frontier. Participants completed work faster, produced higher-rated results, and finished more tasks. But on a task deliberately placed outside that frontier, people using AI were 19 percentage points less likely to reach the correct answer. The authors are careful about the limitation: the experiment included only one outside-the-frontier task. It does not prove that AI hurts every difficult task. It proves something more useful—that help on one task does not guarantee help on the task next to it. ([Full paper](https://www.hbs.edu/ris/Publication%20Files/dell-acqua-et-al-2026-navigating-the-jagged-technological-frontier_5c589c8c-fbb5-458f-b285-c944746cd717.pdf))

The danger is not simply that AI makes mistakes. People make mistakes too. The danger is that the surface of AI is smoother than the capability beneath it. Fluency hides the terrain.

Benchmarks help, but they compress a landscape into an average. A leaderboard can tell us how a model performed across a defined test set. It cannot tell me whether the model should draft this proposal, reconcile these invoices, review this contract clause, or interpret this customer complaint in my particular workflow.

The frontier is also not a property of the model alone. It emerges from the combination of the model, the tools it can use, the context it receives, the way a task is framed, the standard of the output, and the skill of the person reviewing it. Change any one of those, and the boundary may move.

This is why impressive demonstrations are both valuable and dangerous. They reveal a peak. They rarely show the valley one step away.

## Your Workflow Has Its Own Frontier

Most people adopt AI at the level of job titles: “AI can do research,” “AI can write,” or “AI can code.” These categories are too large to be useful.

Consider “research.” It may include finding candidate sources, distinguishing primary evidence from commentary, extracting claims, checking dates, comparing contradictions, calculating a number, and recommending an action. A model may be excellent at the first and fourth steps, adequate at the third, and unreliable at the final judgment. Calling the whole bundle “research” erases the information we need most.

So the first move is to replace nouns with observable verbs.

Do not map “marketing.” Map “group raw interview comments into recurring objections.” Do not map “writing.” Map “turn a verified claim ledger into a first draft for a defined reader.” Do not map “software development.” Map “write a migration, run the tests, and explain every failed assertion.”

This shift matters because the useful frontier is personal. Two people using the same model may get different value because they provide different context, notice different errors, and require different standards. A task that is safe for an experienced reviewer may be unsafe for a beginner—not because the model changes, but because the surrounding system does.

The goal is not to discover whether AI is good or bad. The goal is to discover the division of labor that makes the combined system better than either side alone.

## Build the Map Through Small Bets

A useful capability map does not require a laboratory. It requires disciplined small experiments.

Start with a recurring task and collect a few representative cases, including at least one awkward edge case. Write the success criteria before asking AI to act. Then compare the assisted result with a human baseline or with an independently verified outcome. Judge the work on four dimensions: output quality, elapsed time, review effort, and the cost of a failure.

That last dimension changes everything. A drafting error that takes two minutes to fix is not the same as a fabricated citation that survives into publication. Saving half an hour of generation is not a gain if it creates an hour of anxious inspection. The real unit of productivity is not output produced. It is verified progress.

The map can remain simple:

- Green: repeated success, visible errors, and cheap recovery. Delegate the task, then verify by sampling.
- Yellow: useful but unstable. Work alongside the model and require review at specific checkpoints.
- Red: failures are hard to detect or expensive to reverse. Keep human ownership of the core decision; use AI only to generate alternatives or attack the reasoning.
- Gray: not enough evidence. Run a small, reversible test before making it part of the workflow.

These colors are not permanent grades. Record the model, tools, context, date, examples, and failure patterns behind each judgment. When one of those changes, the map expires.

This is also where AI use can become a self-evolving system. Every meaningful failure should become a new test case. Was the cause missing context, an ambiguous instruction, an inaccessible tool, weak reasoning, or a bad evaluation rule? Change one variable and test again. A pile of chat histories is not a curriculum. Experience compounds only after it has been turned into examples, checks, and better boundaries.

## The Map Must Stay Lighter Than the Work

There is an obvious objection: by the time we finish mapping a model, a new one has already arrived.

That is true if the goal is to certify every possible task. It is not true if the goal is to make a few important decisions better. Map only work that is frequent enough to matter or consequential enough to deserve a boundary. Let low-stakes experiments stay playful. Make high-stakes uses earn trust through evidence.

The map will still be imperfect. Small samples can mislead. A reviewer may prefer AI prose without noticing that it has become less diverse. A test may reward a neat answer instead of a correct one. Whenever possible, connect evaluation to reality: Does the calculation recompute? Does the cited source open and support the claim? Do the tests pass? Does the user complete the task? Reality is a better judge than confidence, including our own.

This is not a demand for permanent suspicion. It is a way to make trust specific. “I trust AI” is almost meaningless. “I trust this setup to perform this task, within this boundary, because it passed these checks” is operational knowledge.

## The New Literacy Is Frontier Cartography

The strongest AI user is not the person who delegates the most. It is the person who knows when to let the machine sprint, when to walk beside it, and when to keep it away from the decision.

That person is not made weaker by automation. Repetition moves to the machine; judgment moves closer to the human. And because execution becomes cheaper, the human can afford more experiments, faster feedback, and more ambitious work.

This is the real promise of AI: not a life without effort, but a life in which effort moves upward—from producing every line to designing the system, from accepting fluent answers to constructing tests, from doing the same task again to improving how the task will be done next time.

The frontier will keep moving. Some valleys will fill in; new ones will appear as we attempt work that was previously impossible. A static list of “things AI can do” will always fall behind.

But a person who knows how to redraw the map will not.

So stop asking only how smart the newest AI is. Ask where it is strong for the work in front of you, what evidence would prove you wrong, and how quickly your next experience can improve the map.
