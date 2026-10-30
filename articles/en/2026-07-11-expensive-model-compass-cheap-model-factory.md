# The Expensive Model Is a Compass. The Cheap Model Is a Factory

> 发布日期:2026-07-11 · [中文](../zh/2026-07-11-贵模型是罗盘便宜模型是工厂.md) | [English](../en/2026-07-11-expensive-model-compass-cheap-model-factory.md)

---

The most useful AI question today may no longer be "Which model is best?"

That question still matters. If you are doing frontier research, high-stakes reasoning, difficult coding, or a task whose failure mode you do not yet understand, raw model capability is real. Pretending otherwise is cheap wisdom.

But today's notes point to a stranger pattern: the model that helps you discover a new use case is often not the model that should run the use case forever.

This looks like an industry story at first. A recent Decagon article says the company now runs about 90 percent of its workloads on open-weight models. The reason was not ideology or simple cost-cutting. It was production reality: in customer-service AI, an eight-second turn is not a product people will use, and the right answer often comes from a small, fast model tuned for one specific task.[^1]

The same article also points to the paradox. Open models are becoming more useful in mature deployments, yet open-source models reportedly fell to 11 percent of enterprise LLM spend, down from 19 percent a year earlier.[^1] TechCrunch found the same split in public infrastructure data: on Vercel's AI Gateway, DeepSeek had recently grown to more than a third of token volume, while Anthropic still accounted for more than half of spend. On OpenRouter, DeepSeek V4 Flash was processing about 5.3 trillion tokens weekly, while the most popular frontier model, Opus 4.8, processed just over 2 trillion; but Opus was roughly 23 times more expensive per million tokens.[^2]

More usage below. More spending above.

That is not a contradiction. It is a lifecycle.

## Discovery Wants General Intelligence

When a use case is new, you do not know its shape yet.

You do not know which inputs matter. You do not know which edge cases will break trust. You do not know whether the user actually wants the thing they asked for. You do not know if the workflow is a language problem, a data problem, an incentive problem, or a missing decision problem.

In that stage, paying for the strongest general model makes sense. You are not buying efficiency. You are buying search.

The expensive model is a compass.

It helps you walk through fog. It can compare frames, generate prototypes, attack weak assumptions, write first versions, summarize messy evidence, and show you several possible shapes of the work before you have committed to one.

Most people waste the compass by treating it like a factory worker.

They ask the strongest model to repeat the same mature task again and again. Draft this standard reply. Summarize this familiar document. Generate the same report. Rewrite the same template. Answer the same operational question.

That may work for a while, but it hides a bad habit. If the task has become clear enough to repeat, then the intelligence should start moving out of the conversation and into the system.

The prompt should become a checklist.

The conversation should become a workflow.

The clever answer should become a test case.

The expert judgment should become a small rule, a template, a script, a fine-tuned model, a retrieval set, or a documented procedure.

The point of using a powerful model is not to rent genius forever. The point is to discover enough structure that you no longer need genius for that part of the work.

## Production Wants Specific Intelligence

Once the use case is mature, the trade changes.

Now you know the shape of the inputs. You know what good behavior looks like. You know the common failure modes. You know which mistakes are tolerable and which ones must stop the system. You know the few things the model must do extremely well and the many things it does not need to know at all.

At that moment, general intelligence becomes overhead.

A customer-service agent answering a narrow refund question does not need to know every capital city. A local document classifier does not need to reason about philosophy. A routine internal report does not need a frontier model that can write poetry, debug distributed systems, and solve olympiad problems. Those abilities are beautiful, but they are not free. They add latency, cost, uncertainty, and sometimes too much cleverness.

Production wants a factory.

Not a dumb factory. A specialized one.

A factory is not impressive because it can do anything. It is impressive because it can do one thing repeatedly, at cost, with tolerable variance, under real constraints.

This is why "open source versus closed source" is often the wrong debate. In many business settings, the important question is not moral identity. It is maturity.

Is this task still in exploration, where ambiguity is the work?

Or has it matured into execution, where repeatability is the work?

The same company may need both. The same product may need both. The same person may need both in the same afternoon.

The danger is mixing the phases.

If you use a cheap specialized model too early, you may lock in the wrong shape of the problem. You optimize before understanding. You turn a blurry need into a rigid process and then spend months wondering why the process feels wrong.

If you use a frontier model too late, you may never build a system. You keep paying for fresh reasoning where a stable mechanism should exist. You enjoy the feeling of intelligence without accumulating infrastructure.

That second failure is quieter, and more common.

It feels productive because the output stays good.

But nothing compounds.

## Individuals Have the Same Problem

This is not only an enterprise AI story.

It is also a personal growth story.

Many ordinary users now have access to a model that is too strong for most of their daily tasks. That sounds like a blessing, and often it is. But abundance creates a new form of laziness: not the laziness of doing nothing, but the laziness of never distilling.

You ask the model to help you think through a decision. It gives you a useful frame.

Good.

But if you face the same kind of decision again next week, and you return to the model with the same fog, something was missed. The first conversation should have left behind a small instrument: a decision checklist, a scoring table, a question sequence, a personal principle, a saved prompt, a note you can reuse, or a simple script.

The same applies to learning.

Use the strongest model when you do not yet understand why you are confused. Let it ask better questions. Let it show counterexamples. Let it expose the hidden assumption. Let it help you find the right mental doorway.

But once the doorway is found, do not keep asking it to carry you through every time.

Turn the discovery into practice.

Make flashcards. Write examples. Explain the idea out loud. Build a small exercise. Revisit it after forgetting. Test yourself without the model. Let the knowledge become something your own mind can retrieve.

The best tutor is not the one who keeps sounding brilliant. The best tutor makes you need less tutoring for the same problem.

The best AI workflow is similar.

It should leave residue.

After a good session, your system should be slightly better: a clearer note, a sharper checklist, a stronger template, a tested script, a better taste for what to ask next time. If nothing remains except a polished answer, then the intelligence passed through you like weather. It was pleasant. It did not become capital.

## The Zeroth Class Migrates Intelligence

I keep returning to the idea of the zeroth class: people who use AI to become stronger, not lazier.

Here is one practical definition:

The zeroth class knows how to migrate intelligence.

They migrate it from model output into personal judgment.

They migrate it from a one-off conversation into a repeatable workflow.

They migrate it from expensive exploration into cheaper production.

They migrate it from "AI helped me once" into "my system is now better because AI helped me once."

That is the real compounding loop.

Not "I used the newest model."

Not "I generated more."

Not even "I saved time."

The stronger question is: What did this session make easier next time without making me weaker?

If the answer is nothing, the work may have been useful, but it did not compound.

If the answer is a new tool, a new habit, a clearer standard, a reusable asset, a sharper question, or a piece of judgment you can now perform without assistance, then AI has done something more important than produce.

It has helped you evolve.

## Ask Which Phase You Are In

So the next time the model debate gets loud, I want to remember this simple distinction.

The frontier model is a compass.

The cheap model is a factory.

The compass matters when you are lost.

The factory matters when you know what must be made.

A compass used as a factory becomes expensive theater. A factory used as a compass becomes efficient confusion. The art is not choosing one side forever. The art is knowing which phase the work is in.

This is true for companies choosing model infrastructure.

It is true for one-person businesses turning services into systems.

It is true for writers turning scattered notes into essays.

It is true for learners turning explanation into ability.

It is true for anyone trying to use AI without letting AI quietly replace the part of them that should be growing.

Do not worship the strongest model.

Do not romanticize the cheapest one.

Use the strong one to find the shape.

Use the cheap one to repeat the shape.

Then keep moving the shape into your own system.

That is where leverage becomes learning.

That is where AI stops being a brilliant answer machine and becomes a self-evolving loop.

The future will not belong only to people who can afford the best compass.

It will belong to people who know when to stop admiring the compass, mark the road, and build the factory.

[^1]: Decagon, "Everyone is wrong about open source AI in the enterprise," 2026-07-09. https://decagon.ai/blog/everyone-is-wrong-about-open-source-ai-in-the-enterprise
[^2]: TechCrunch, "Why the rise of open source AI isn't hurting Anthropic ... yet," 2026-07-07. https://techcrunch.com/2026/07/07/why-the-rise-of-open-source-ai-isnt-hurting-anthropic-yet/
