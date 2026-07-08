# A Mind Needs a Workbench

> 发布日期:2026-07-08 · [中文](../zh/2026-07-08-头脑需要一张工作台.md) | [English](../en/2026-07-08-a-mind-needs-a-workbench.md)

---

Today’s notes circled around a strange new phrase: J-space.

Anthropic published a piece of interpretability research arguing that Claude has developed a small internal space where certain concepts can be held, reported, controlled, reused, and used for multi-step reasoning.[^1] The paper calls these verbalizable representations a kind of global workspace.[^2]

It is tempting to run straight toward the loud question:

Is Claude conscious?

I think that question is too fast. It grabs the most dramatic interpretation before we have learned the practical lesson. The more useful question, at least for people trying to live and work with AI, is quieter:

Why does capable thinking seem to need a workbench?

Not a stage. Not a personality. Not a beautiful final answer.

A workbench.

A small shared place where unfinished things can sit long enough to be inspected, combined, tested, redirected, and used by more than one part of the system.

That is the part worth staring at.

## Output Is Already Late

Most people judge AI by output. The answer is fluent or clumsy. The code passes or fails. The summary is sharp or vague. The image is beautiful or dead.

This is natural, but it is also late.

Output is what becomes visible after the system has already done its hidden work. By the time words arrive on the screen, many decisions have already been made: what mattered, what was ignored, what intermediate idea was kept, what risk was noticed but not mentioned, what frame was chosen, what direction the reply should take.

Anthropic’s J-space research matters because it gives us a way to look at some of that hidden middle. According to the research summary, J-space is not the same as chain-of-thought or a written scratchpad. It is not text the model writes to itself. It sits inside the model’s activations, silently carrying concepts the model may be able to use before it says anything.[^1]

In the experiments, this space behaved in several important ways. The model could report concepts held there. It could hold a requested idea there while copying unrelated text. Intermediate steps in math and reasoning appeared there before the final answer. A country concept placed in the workspace could be reused across different questions about capital, language, continent, and currency. And when researchers interfered with the space, some higher-order reasoning tasks collapsed while simpler fluent behavior remained relatively intact.[^1]

That last point is the useful one.

Fluency can survive without deep workspace use.

Thinking cannot.

At least, not the kind of thinking that chains steps together, carries an intermediate result, notices conflict, and lets one representation be used by many downstream operations.

This should make us more suspicious of smooth output. A system can speak well while doing very little deliberate work. A person can also speak well while doing very little deliberate work. Polished language is not proof of a mind at work. Sometimes it is just a surface that learned to shine.

## Intelligence Is a Coordination Problem

Global workspace theory in neuroscience describes the mind as a collection of many specialized processes, most of them working outside conscious access. A piece of information becomes consciously accessible when it enters a small shared workspace and can be broadcast to other systems.[^2]

Whether or not one accepts the whole theory of consciousness, the engineering intuition is powerful.

A capable system does not only need many parts. It needs a place where parts can meet.

If one part detects danger, another part plans action, another part retrieves memory, another part understands language, and another part chooses the next move, then intelligence is partly a routing problem. Which information becomes central? Which intermediate result is worth preserving? Which small object gets written once and read by many processes?

Without a shared workbench, every capability becomes local. It may work in isolation, but it cannot easily become judgment.

This is why the J-space finding feels larger than an AI interpretability result. It points at a general pattern:

automatic competence lives everywhere;

deliberate ability needs a shared surface.

The same pattern appears in real work. A team with smart people but no shared document, no decision log, no tests, no design review, and no visible definition of done often becomes strangely stupid. Everybody has local intelligence. Nobody has a workbench.

A person can have the same problem internally. Many ideas, no place to combine them. Many notes, no question. Many tools, no loop. Many intentions, no visible next move.

The failure does not feel like ignorance. It feels like fog.

## The Human Lesson Is Not “AI Thinks Like Us”

We have to be careful here.

Anthropic itself is cautious: the research does not prove that Claude has subjective experience or feels anything.[^1] External commentary also emphasizes major differences from animal consciousness, including Claude’s lack of a body, biological vigilance systems, and human-like episodic memory.[^3] Independent reviewers have also treated J-lens as useful but limited: it may approximate part of a model’s working memory, but it can miss things and produce misleading readings.[^4]

So the lesson is not:

AI has a human soul.

The lesson is:

complex intelligence may repeatedly converge on some form of shared workspace, even when the implementation is very different.

That distinction matters. The first claim becomes metaphysical theater. The second claim becomes practical design.

If a language model benefits from a workspace, maybe a human working with AI needs one even more.

Because our problem is not that we lack outputs. We are drowning in outputs. Summaries, drafts, plans, screenshots, transcripts, bullet lists, dashboards, prompts, courses, recommendations, templates. The world is now very good at producing finished-looking things.

What we lack is the workbench between input and output.

A place where we can keep the question alive.

A place where assumptions are visible.

A place where evidence is separated from interpretation.

A place where the system remembers what we already rejected.

A place where AI can help us reason without quietly replacing our reasoning.

This is the real difference between “using AI” and building an AI-augmented self.

## Your External J-Space

For a person, an external J-space does not need to be mystical. It can be a note, a checklist, a Git issue, a small table, a whiteboard, a test file, a daily review, or a project folder that always carries the same fields.

The format is less important than the function.

It should hold intermediate thought.

It should be readable by both you and the machine.

It should be writable, so wrong assumptions can be corrected rather than merely admired.

It should be small enough that attention can actually enter it.

And it should connect to action.

For example, when you ask AI to help with a hard problem, the workbench should not only contain the prompt. It should contain:

- the current question;
- what success would look like;
- what is known;
- what is guessed;
- what must not be exposed or touched;
- what has already failed;
- the next smallest test;
- the stopping condition.

This looks boring.

Good.

Workbench design is usually boring. So are kitchens, laboratories, workshops, and operating rooms. Their job is not to entertain the visitor. Their job is to make repeated high-quality work possible.

Most AI usage fails here. People throw a need into the model, receive a plausible answer, feel a small burst of motion, and then lose the thread. The next conversation begins from zero. The next prompt re-explains the same context. The next output feels impressive but does not accumulate.

No workbench, no compounding.

With a workbench, AI can do something much better than answer. It can help maintain the loop. It can bring back yesterday’s unresolved assumption. It can turn a vague concern into a test. It can compare a new idea against an old constraint. It can notice that the beautiful plan violates the original definition of done. It can help your system remember.

That is when AI makes a person stronger.

Not when it saves a few minutes.

When it gives your thinking a place to return to.

## Keep the Bench Small

There is a trap: once people hear “system,” they build a cathedral.

Too many folders. Too many tags. Too many dashboards. Too many automations. Too many agents. Too many ways to avoid the work while feeling very organized.

A workbench is not a warehouse.

The power of a workspace comes partly from limited capacity. Anthropic’s summary notes that Claude’s J-space holds only a small selection of internal concepts at a time, while most processing happens elsewhere.[^1] Human attention is also limited. A real workbench forces selection. What is the one question now? What are the two assumptions that matter? What is the next test?

If everything is on the bench, nothing is on the bench.

This is why I am increasingly skeptical of “second brain” systems that become museums. The point is not to keep everything. The point is to keep the right few things alive long enough for them to change your next move.

The bench should be small, but alive.

Alive means it changes after contact with reality. A claim becomes a source. A guess becomes a test. A test becomes evidence. Evidence changes the plan. The plan changes the next action. The next action creates new evidence.

That loop matters more than the tool.

## The Zeroth Class

I keep returning to the phrase “the zeroth class.”

It names the people who do not use AI to become passive consumers of answers. They use AI to strengthen the layer before answers: attention, judgment, memory, practice, taste, and execution.

The zeroth class will not be defined by owning the newest model. Models will spread. Interfaces will improve. A lot of capability will become cheap.

The difference will be workbench quality.

Some people will have AI conversations that vanish.

Some people will have AI systems that remember, test, refine, and compound.

Some people will ask for better outputs.

Some people will build better places for unfinished thought.

The second group will look slower at first. They will spend time naming assumptions, writing down constraints, checking sources, preserving decisions, designing tests, and closing loops. From the outside, this can look less magical than typing one prompt and receiving a polished answer.

But over time, the difference becomes obvious.

One person collects outputs.

Another person builds a mind with a bench.

## What the Research Really Reminds Me

The J-space research does not make me want to worship AI.

It makes me more respectful of infrastructure.

It reminds me that intelligence is not only in the answer. It is in the invisible organization that lets an answer become possible.

It reminds me that a fluent system can be shallow, and a clumsy-looking system can be doing real work if it preserves the right intermediate states.

It reminds me that humans should stop competing with AI at the surface level of output and start building the environments where judgment can accumulate.

A mind without a workbench becomes noise.

A tool without a workbench becomes entertainment.

A person with a workbench can use AI without disappearing into it.

So maybe the practical lesson of J-space is not that Claude is like us.

Maybe the lesson is that we should become less careless with our own thinking.

Put the unfinished thought somewhere.

Make it visible.

Let it be challenged.

Let it survive long enough to become action.

That is where intelligence starts to compound.

[^1]: Anthropic, “A global workspace in language models,” 2026-07-06. https://www.anthropic.com/research/global-workspace
[^2]: Gurnee et al., “Verbalizable Representations Form a Global Workspace in Language Models,” Transformer Circuits, 2026. https://transformer-circuits.pub/2026/workspace/
[^3]: Anthropic, “External commentary for global workspace paper,” 2026. https://www-cdn.anthropic.com/files/4zrzovbb/website/cc4be2488d65e54a6ed06492f8968398ddc18ebe.pdf
[^4]: Neel Nanda, “A Review of Anthropic’s Global Workspace Paper,” LessWrong, 2026-07-07. https://www.lesswrong.com/posts/zFJ3ZdQwrTWE9jT5S/a-review-of-anthropic-s-global-workspace-paper
