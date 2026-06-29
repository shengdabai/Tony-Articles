# Put the Machine Across the Table

> 发布日期:2026-06-29 · [中文](../zh/2026-06-29-让机器坐到你对面.md) | [English](../en/2026-06-29-put-the-machine-across-the-table.md)

---

A lot of people still use AI as if it were a faster hand.

Write this. Summarize that. Turn these notes into a post. Make this code run. Translate this paragraph. Design this page. Find me an answer. Make it shorter. Make it cleaner. Make it sound better.

There is nothing wrong with that. A faster hand is useful. Much of daily work is still dead work: copying, rearranging, formatting, checking the same kind of thing for the hundredth time. If a machine can carry that layer, good. Let it carry it.

But today my notes kept circling a different question.

What if the most valuable use of AI is not to put it beside you as an assistant, but across from you as an opponent?

Not an enemy in the dramatic sense. Not a machine that humiliates you or argues for sport. I mean something more practical: a second force in the room that is allowed to say, "This may be wrong. Start again from the ground. Show me the assumption. Show me the failure path. Show me what breaks if reality refuses to cooperate."

That sounds less comfortable than "help me finish this."

It is also where the leverage starts.

## The cheap part moved

The old bottleneck was production.

You had to know how to write code before you could build software. You had to know layout tools before you could design a page. You had to know search operators, file formats, scripts, and a dozen little workflows before you could turn an idea into an artifact.

AI has not removed skill, but it has lowered the cost of visible production. A non-engineer can make a small app. A writer can build a local tool. A teacher can turn repeated explanations into exercises.

This is not theory anymore. Anthropic's June 2026 analysis of Claude Code usage looked at about 400,000 interactive sessions from roughly 235,000 people between October 2025 and April 2026. One of its most useful findings is the division of labor: in a typical session, people made most planning decisions, while Claude made most execution decisions. The report summarized the pattern simply: people decide what to build, and the agent decides how to build it.[^1]

That means the scarce part is moving.

If the machine can produce ten versions, the hard question is no longer, "Can I make one?" The hard question is, "Which one should exist?"

If the machine can implement a plan, the hard question is no longer, "Can I write all the steps?" The hard question is, "Is this the right plan?"

If the machine can polish the argument, the hard question is whether there is a real argument underneath the smoothness.

AI makes output cheaper. It does not make judgment cheaper.

In fact, it makes weak judgment more expensive, because weak judgment can now produce much more material before anyone notices.

## First principles are not a magic phrase

One of today's notes was about adding a simple instruction to an AI task: reason from first principles.

I understand why people like that phrase. It is compact. It reminds the model, and the human, not to imitate the nearest pattern too quickly. Instead of asking, "What does this look like?" it asks, "What is this made of?"

But I do not think the power is in the phrase itself.

The power is in the interruption.

Most thinking, human or machine, begins by matching. This looks like that. This bug resembles that earlier bug. This product should follow that competitor. This article needs the same shape as the last one that performed well. Matching is fast, and often it is good enough.

The problem is that matching can hide the place where the situation is different.

First-principles thinking interrupts the match. It asks what must be true, what the real constraint is, which parts are habit, which parts are evidence, and what we would build if we had never seen the standard answer.

This is useful with AI because language models are extremely good at producing plausible continuations. That is their gift. It is also their danger. If you ask for a normal answer, you often get the most normal path through the training fog.

Sometimes normal is fine.

But when the cost of being slightly wrong is high, or when you are stuck in a loop of patches, normal is not enough. You need the machine to stop pattern completion and help you take the thing apart.

The instruction is not "be clever."

It is "stop borrowing other people's tracks for a moment."

## The opposite seat matters more than the helpful seat

The second idea in today's notes was adversarial review.

This one may be even more important.

A helpful AI tries to complete your intention. An adversarial AI tries to break your intention in a useful way.

It asks what could go wrong if the input is too large, the date is wrong, the user is malicious, the source is stale, the business assumption is false, the reader is unconvinced, the edge case is not rare, the metric can be gamed, or the beautiful plan meets a tired Tuesday.

This is not new. The business world has had a version of it for years. In September 2007, Harvard Business Review published a short article on the "project premortem." The method asks a team to imagine that the project has already failed, then work backward and generate plausible reasons. The point is to make doubts speakable early enough to improve the plan.[^2]

AI makes this practice easier to run alone.

That matters because most of us do not naturally seek strong opposition. We seek fluency. We seek completion. We ask, "Can you improve this?" when the better question is, "What would make this fail?"

The difference is huge.

"Improve this" usually polishes the surface.

"Make the strongest case against this" changes the room.

It lets the machine sit across the table and become the person who is not impressed by your momentum. It can ask where the evidence is thin, where the story is too convenient, where the user would get confused, where the code would fail, where the plan depends on a version of you who is never tired.

This is not negativity.

It is respect for reality.

## Critical thinking changes shape

There is a lazy fear about AI: people will stop thinking.

There is also a lazy optimism: people will think more because AI removes tedious work.

Both are too simple.

A 2025 Microsoft Research paper surveyed 319 knowledge workers and collected 936 examples of generative AI use at work. The interesting result was not "AI good" or "AI bad." It was conditional. Higher confidence in GenAI was associated with less critical thinking, while higher confidence in one's own task ability was associated with more critical thinking. The paper also found that critical thinking shifts toward verification, integration, and task stewardship.[^3]

That phrase, task stewardship, feels important.

In an AI workflow, critical thinking is no longer only the moment before production. It is spread across the loop.

You frame the task, decide what evidence counts, let the machine produce, ask it to attack the output, check the attack, repair the plan, and decide when the result is good enough.

The human is not merely a prompt writer. The human is the steward of the loop.

This is why "use AI to think for you" is such a dangerous phrase. Thinking is not one blob that can be handed away. It is a chain of responsibilities. Some links can be accelerated. Some links can be delegated. Some links must stay with you, not because humans are romantic, but because the whole system needs an accountable owner.

The machine can produce objections.

It cannot decide what you are willing to stand behind.

## A simple loop for becoming harder to fool

The method I want to keep is very small.

First, ask for the constructive version.

What is the best plan? What is the cleanest explanation? What is the most direct implementation? What is the strongest version of the argument?

Second, force a return to the ground.

What are the first principles? What must be true? What is the real constraint? What evidence would change the plan?

Third, move the machine across the table.

Assume this failed. Why? Assume the reader does not believe me. Where do they attack? Assume the user behaves badly. What breaks? Assume the input is ugly, late, huge, missing, contradictory, or malicious. What happens?

Fourth, ask for evidence.

Not reassurance. Evidence.

In software, that may be tests, a build, logs, screenshots, or a diff. The Claude Code documentation is blunt about this: give the agent a check it can run, because without a check, "looks done" becomes the only signal available.[^4] The same idea works outside code. For writing, evidence may be source links, a contradiction map, a list of unsupported claims, or a paragraph-by-paragraph challenge. For a decision, it may be a premortem, a risk table, or a small reversible test.

Fifth, decide.

Do not let the adversarial step become endless self-doubt. Review creates better work only when it feeds back into action. Otherwise it becomes a refined form of avoidance.

The loop is:

Build the best version.

Return to the facts.

Attack the result.

Collect evidence.

Decide and ship.

Then remember what happened.

That last part matters. A self-evolving system is not a system that sounds smart today. It is a system that gets less naive next month because it kept the scars from this month.

## Do not turn opposition into theater

There is one trap: adversarial review can become a performance.

People will ask AI to "be brutally honest," receive a dramatic list of issues, fix the easiest three, ignore the important one, and feel rigorous. That is not opposition. That is decoration.

Real opposition has a price. It may force you to delete a paragraph you like, shrink the scope, admit that the product is only a clever demo, or see that the code works only because the test data is polite.

If nothing is ever cut, the review probably was not real.

## The new literacy is not prompting. It is placement.

People often ask what prompts they should memorize.

I understand the impulse. A good phrase can unlock a better response. But prompt collecting is still too shallow.

The deeper skill is placement.

Where do you place AI in the thinking process?

At the start, it can help you explore.

In the middle, it can help you construct.

Near the end, it can help you attack.

After shipping, it can help you remember.

If you only place it in the production slot, you become faster at making whatever your current judgment already wants. That is useful, but limited. If your judgment is off, AI scales the error.

If you place it in the opposing slot, something different happens. You train a habit of not believing your first fluent answer. You become less impressed by output and more interested in the loop that produced it. You learn to separate speed from truth, polish from structure, confidence from evidence.

This is what I mean by using AI to make people stronger rather than lazier.

Not using AI less.

Using it in a position that makes escape harder.

Put it beside you when the work is dead.

Put it behind you when you need memory.

Put it ahead of you when you need exploration.

But when the question matters, put the machine across the table.

Let it ask the impolite question.

Let it assume the plan failed.

Let it search for the missing premise.

Let it show you the path where your beautiful idea breaks.

Then do the human part.

Look at the evidence.

Change what deserves to be changed.

Ship what still stands.

That is not a prompt trick.

It is a way to become harder to fool.

## References

[^1]: Anthropic, "Agentic coding and persistent returns to expertise," 2026. https://www.anthropic.com/research/claude-code-expertise
[^2]: Harvard Business Review, "Performing a Project Premortem," September 2007. https://hbr.org/2007/09/performing-a-project-premortem
[^3]: CHI 2025 program, "The Impact of Generative AI on Critical Thinking." https://programs.sigchi.org/chi/2025/program/content/189154
[^4]: Anthropic, "Best practices for Claude Code." https://code.claude.com/docs/en/best-practices
