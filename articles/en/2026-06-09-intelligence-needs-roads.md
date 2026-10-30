# Intelligence Needs Roads

> 发布日期:2026-06-09 · [中文](../zh/2026-06-09-聪明的AI也需要路.md) | [English](../en/2026-06-09-intelligence-needs-roads.md)

---

Most conversations about AI still sound like a contest of brains.

Which model is smarter? Which one reasons better? Which one writes cleaner code? Which one can hold more context, use more tools, pass more benchmarks, or act more like a real assistant?

These are reasonable questions. Intelligence matters. A weak model cannot be saved by good packaging forever.

But the more I use AI in real work, the more I feel that we are overpaying attention to the brain and underpaying attention to the road.

A car with a powerful engine is not very impressive inside an old city built before cars existed. The streets are narrow. The signs are inconsistent. Some turns depend on local memory. Some paths are blocked by doors meant for people, not machines. The car may be excellent, but excellence cannot express itself cleanly when the environment was never designed for it.

This is the hidden problem behind many AI failures.

We think the model is not smart enough. Sometimes that is true. But often the deeper issue is that the world around the model is not executable enough. The task lives in screenshots, web forms, undocumented fields, half-remembered conventions, files with inconsistent names, and rules that experienced people know but never wrote down.

The model is asked to be intelligent, but the environment gives it no road.

## The Biology Example

Anthropic published a research piece on June 8, 2026 about AI agents in biology. The central argument is simple but important: software agents have progressed faster than biology agents not only because code models improved, but because software already has unusually good execution infrastructure.

Software has repositories, version control, package managers, APIs, logs, tests, issue trackers, and relatively clear failure signals. If an agent changes code, it can run tests. If the build fails, the error message points somewhere. The feedback is not perfect, but it is much more deterministic than many real-world knowledge tasks.

Biology is different.

Important biological data often lives across databases, web interfaces, file formats, metadata conventions, and local habits. A human researcher may know which filter matters, which genome version is safe, which database field is unreliable, or why a "complete" record is not really complete enough for this use case. But if that judgment remains hidden inside human practice, an AI agent cannot reliably reproduce it.

This is not a small inconvenience. In scientific work, one wrong filter can change the conclusion. Mixing database records, using the wrong genome version, missing metadata, or confusing similar sequence labels may create results that look plausible and are still wrong.

That is worse than a visible crash.

A visible crash tells you, "I failed." A plausible wrong answer tells you, "Trust me."

## The Click Tax

One phrase from the biology discussion stayed with me: click tax.

Click tax is the cost created when work that should be programmatic is trapped inside human interfaces. A person must open a website, choose filters, scroll, click, download, rename, interpret fields, and remember which exceptions matter.

Individually, none of this looks dramatic. One click is nothing. A dropdown is nothing. A missing field description is nothing. A small mismatch between a web filter and an API parameter is nothing.

But these little nothings accumulate into a wall.

For a human expert, the wall is annoying. For an AI agent, the wall is structural. The agent does not merely need information; it needs actions that can be repeated, inspected, audited, and corrected. If the workflow is made of invisible human judgment, the model is forced to guess.

And when the model guesses, we often blame intelligence.

Maybe the better question is: why did we put a guessing machine in front of a maze and call that automation?

## The Boring Layer

The interesting part of Anthropic's biology work is not that a bigger model solved everything. The interesting part is that a deterministic retrieval layer changed the game.

The researchers worked with NCBI to build `gget virus`, a tool for reliable viral sequence retrieval. In their VirBench benchmark, which contained 120 realistic viral sequence queries across 40 pathogens, agents performed very differently when acting alone. But when paired with the tool, the agents' accuracy jumped above 90 percent, and the best systems approached near-perfect performance. The tool itself reached 100 percent on the benchmark.

The lesson is not "tools are good" in a vague sense.

The lesson is more precise: when the uncertain part of the system is paired with a deterministic execution layer, the whole system becomes more reliable. The model can reason, plan, explain, and generate hypotheses. The tool can perform the boring work of retrieving, filtering, logging, and standardizing data.

Boring is not an insult here.

Boring means repeatable. Boring means inspectable. Boring means the same input does not become three different answers because the interface was ambiguous. Boring means you can check how the result was produced.

AI does not only need more creativity. It needs more boring reliability around it.

## This Is Not Only About Science

It would be easy to file this away as a technical problem for biology labs.

I think that misses the real point.

Every person who uses AI is already living inside the same pattern. The only difference is scale.

When your notes are scattered across apps, screenshots, chat histories, and memory, your AI assistant cannot really help you think. It can only imitate thinking from fragments.

When your work process is "you know what I mean," the AI does not know what you mean. It guesses.

When your standard for a good answer is only a feeling in your head, you cannot delegate quality. You can only react after the fact.

When your recurring decisions have no checklist, your AI cannot improve the decision loop. It can only produce another opinion.

When your writing system has no capture, selection, verification, drafting, criticism, and revision stages, AI can generate words, but it cannot build a writing practice.

This is why many people feel both amazed and disappointed by AI. The model is powerful enough to reveal the weakness of their own systems.

If your life and work have no roads, AI will not magically create a city. It will drive around your confusion faster.

## Infrastructure Is a Form of Thinking

We often treat infrastructure as low-status work.

The visible work gets praise: the essay, the product demo, the model output, the launch, the performance, the final answer.

The invisible work feels dull: naming files consistently, keeping notes searchable, writing a checklist, designing a test, documenting a decision, making a template, creating a repeatable review process, defining what "done" means.

But in practice, the invisible work determines how far intelligence can travel.

A checklist is thinking preserved outside the brain.

A test is doubt made executable.

A template is experience compressed into a reusable shape.

A naming convention is memory shared with the future.

A log is accountability made visible.

A good API is trust offered to a stranger, including a machine stranger.

This is why engineering is not just for engineers. Engineering, in the deeper sense, is the discipline of turning fragile personal judgment into structures that can survive repetition.

That is also why AI should not make us abandon thinking. It should force us to externalize better thinking.

## The Human Part

There is a temptation to hear all this and conclude: fine, then we should make everything machine-readable, automate every workflow, and remove humans from the loop.

I do not believe that.

Some judgment should remain human because it involves values, taste, responsibility, privacy, or care. Some friction is useful because it slows us down before a dangerous decision. Some conversations should not become data. Some uncertainty cannot be eliminated without destroying the thing that matters.

The point is not to turn life into a factory.

The point is to choose which parts deserve roads.

Roads are for repeated movement. If a path is important, repeated, costly, and error-prone, leaving it as private memory is not humility. It is waste. If other people or future versions of yourself will need to travel the same path again, build a road.

But do not pave the forest just because you own a machine.

The human job is selection. What should be made deterministic? What should stay open? What should be slowed down? What should be protected? What should be turned into a tool, and what should remain a conversation?

That selection is where agency lives.

## Use AI to Build Roads, Not Excuses

For ordinary people, the practical move is simple.

Do not ask AI only to finish the task in front of you. Ask it to help you improve the path that produces this kind of task.

If you ask AI to write one document, you get one document.

If you ask AI to help you design a document-review checklist, you improve future documents.

If you ask AI to answer one question, you get one answer.

If you ask AI to turn your repeated questions into a learning map, you improve future learning.

If you ask AI to fix one mistake, you get one patch.

If you ask AI to help you write the test that catches that mistake next time, you improve the system.

The difference is small in language and huge in consequence.

The lazy use of AI is outsourcing effort.

The stronger use is building infrastructure for your future effort.

## The Road Is the Real Upgrade

The next stage of AI will not be decided only by which model has the most impressive brain. It will also be decided by who builds the clearest roads around intelligence.

Science needs reliable data layers.

Companies need agent-friendly workflows.

Creators need searchable archives and repeatable publishing systems.

Learners need feedback loops, not just explanations.

Families, teams, and individuals need clearer standards for what should be remembered, repeated, checked, protected, and improved.

This is not glamorous work. It does not always look like genius. It often looks like cleaning the table before cooking, drawing the map before traveling, writing the rule before arguing, or labeling the box before storing it.

But this is exactly the kind of work that compounds.

A smarter model can help you once.

A better road can help every model, every teammate, every future version of you.

So yes, keep watching the models. They matter.

But do not forget the roads.

Because intelligence without roads becomes performance.

Intelligence with roads becomes power.

## Sources

- [Anthropic: Paving the way for agents in biology](https://www.anthropic.com/research/agents-in-biology)
- [arXiv: Paving the way for agents in biology](https://arxiv.org/abs/2606.04621)
- [NCBI: Virus](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/)
- [Temporal: What is Durable Execution?](https://temporal.io/blog/what-is-durable-execution)
