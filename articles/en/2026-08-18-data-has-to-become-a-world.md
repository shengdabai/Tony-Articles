# Data Has To Become A World

> 发布日期:2026-08-18 · [中文](../zh/2026-08-18-数据要变成世界.md) | [English](../en/2026-08-18-data-has-to-become-a-world.md)

---

For a long time, when people talked about training intelligence, they talked about data.

More data. Cleaner data. Better labels. Larger corpora. More examples of the right answer. More examples of the wrong answer. More human feedback. More expert demonstrations. More traces from people who already knew how to do the work.

That language still matters.

But it is becoming incomplete.

The next question is not only: what data do we have?

The better question is: what world can the system practice inside?

A sentence can teach a model how people speak. A document can teach it what people have written. A transcript can teach it the visible shape of a task. But an agent that has to act cannot live on text alone. It needs a place where action has consequence, where mistakes are not merely described but encountered, where feedback arrives after a decision, where the same situation can be reset, replayed, varied, and tested again.

In that world, data is no longer a dead pile of examples.

Data becomes an experiment that can run.

## Examples Are Not Enough

A static example is a useful thing. It says: here is a good answer, here is a bad answer, here is what someone did before.

But real work rarely appears as a clean example.

Real work arrives with state. Something has already happened. A customer has a history. A file has changed. A deadline moved. A previous decision created a constraint. A tool call changes what is possible next. A small mistake does not stay small; it changes the next branch of the task.

This is why many AI demos feel impressive and then become fragile in production. The demo shows output. Production tests behavior.

An output can be judged once.

A behavior has to survive a sequence.

If an agent drafts one email, you can read the email and decide whether it is good. If an agent manages a whole workflow, the question changes. Did it notice the missing information? Did it ask at the right time? Did it avoid touching the wrong file? Did it preserve the previous decision? Did it recover after a tool failed? Did it know when to stop? Did it leave evidence for the next run?

Those are not just writing problems. They are environment problems.

The agent needs a task, tools, memory, permissions, initial state, changing state, external events, failure modes, and a verifier. Without those things, we are not really testing the ability to do work. We are testing the ability to sound like work.

That difference is easy to miss because language is so persuasive. A fluent answer creates the feeling of competence. A well-structured plan creates the feeling of progress. But work is not the feeling of progress. Work is what remains after the world has pushed back.

The world has to be part of the training loop.

## Reinforcement Learning Already Knew This

This idea is not new. Reinforcement learning has always been built around interaction.

In a standard reinforcement learning framing, the field studies how a learning agent interacts with an environment in order to achieve a goal.[^1] The agent does not merely absorb examples. It acts, observes what changes, receives feedback, and adapts.

That simple structure matters:

Agent. Environment. Action. Feedback.

It sounds almost too basic. But basic does not mean shallow.

AlphaGo Zero made the point dramatically. The 2017 Nature paper introduced an algorithm based on reinforcement learning without human game data, guidance, or domain knowledge beyond the rules of Go.[^2] DeepMind reported that after three days of self-play training, AlphaGo Zero defeated the earlier published AlphaGo version by 100 games to 0, and after 40 days it surpassed all previous versions.[^3]

The important lesson is not "self-play solves everything." Go is a clean, closed, rule-defined world. Most human work is not like that.

The lesson is more precise:

When the world is well-defined enough, experience can be manufactured.

That is the hidden power. A system does not need to wait passively for humans to produce examples. It can generate attempts, observe outcomes, compare them, and improve. But this only works because the environment is strong enough to answer back. The board enforces the rules. The game ends. Winning and losing are visible. The same opening can be replayed. Variations can be explored. Progress can be measured.

Without that world, "self-improvement" easily becomes theater.

The system produces an answer, critiques its own answer, revises the answer, and sounds wiser. But if the judge has the same blind spots as the generator, the loop may only polish the mistake. If the task has no real consequence, the system may learn the style of improvement rather than improvement itself. If the evaluation space is visible to the system, it may learn to pass the test rather than do the job.

So the hard work is not only building the agent.

The hard work is building a world that can teach the agent.

## A Good Environment Is Expensive In The Right Way

A serious environment has at least three parts.

First, it needs a task.

Not a vague wish like "do better research" or "help the customer." A task has a goal, constraints, inputs, allowed tools, forbidden moves, and a definition of done. The clearer the task, the more useful the experience.

Second, it needs state.

A real environment remembers. It has files, accounts, messages, calendar events, previous attempts, partial failures, and side effects. The agent must learn that action changes the world. That is what makes the task alive.

Third, it needs a verifier.

Someone or something has to judge whether the work actually succeeded. Sometimes the verifier can be automatic: tests pass, the answer matches, the transaction completes. Sometimes it must include human judgment: tone, taste, risk, usefulness, timing. But there must be a judgment channel outside the agent's own self-confidence.

This is where many teams underestimate the work.

They think the product is the agent. The product is often the environment around the agent.

Can you reset the task after a failed run? Can you replay the same situation with a different model? Can you scale the environment without leaking the answer? Can you introduce realistic noise? Can you preserve the trace of decisions? Can you separate research from evaluation so the system cannot simply hack the score? Can you turn a messy customer workflow into a repeatable training ground without lying about its messiness?

These are unglamorous questions. They are also the questions that decide whether learning compounds.

In the old data world, the valuable asset was a large pile of examples. In the agent world, the valuable asset may be a living environment that keeps producing meaningful experience.

The new dataset is not a spreadsheet.

It is a small world with rules, memory, friction, and consequences.

## This Is Also How People Learn

The same pattern applies to people.

Most of us collect too much static data about ourselves.

We save quotes. We collect notes. We highlight passages. We write plans. We keep lists of principles. We watch people explain how they work. We feel smarter because the archive is growing.

But an archive is not yet a learning environment.

If a note never changes what you do, it is mostly decoration. If a principle is never tested under pressure, it is mostly self-image. If a plan never meets a constraint, it is mostly a fantasy with bullet points.

To learn for real, a person also needs a world.

A public writing habit is a world. You publish, readers respond or ignore you, weak arguments expose themselves, and the next piece inherits the lesson.

A weekly review is a world. You predicted something, acted on it, compared result with expectation, and updated the rule.

A small business is a world. Customers pay or refuse, operations break, promises meet capacity, and vague ideas become costs.

A personal AI workflow can be a world too, but only if it includes a task, a state, and a verifier. Otherwise it is just a more flattering notebook.

This is why "use AI to learn faster" is often misunderstood. Faster summaries are not the same as faster learning. A summary gives you compressed information. Learning requires contact with consequences.

The question is not: did AI explain the concept?

The question is: did you build a situation where the concept has to work?

## The Future Belongs To World Builders

As models get stronger, more surface work becomes cheap.

Generating a plan gets cheaper. Writing an answer gets cheaper. Producing a prototype gets cheaper. Translating a document gets cheaper. Even creating examples gets cheaper.

What gets more valuable is the ability to construct the situation in which those outputs can be tested.

That is a different craft.

It asks you to define the task clearly, preserve enough context, introduce realistic difficulty, protect the evaluation, capture failure, and turn feedback into the next run. It asks you to care about the boring parts: permissions, reset, logs, rubrics, edge cases, negative examples, rollback, review, and memory.

This sounds like engineering, and it is.

But it is also a philosophy of growth.

You do not become stronger by hearing more correct sentences. You become stronger when your actions enter a loop that can teach you. You try, reality answers, you inspect the gap, you adjust the system, and the next attempt carries more of the truth than the last one.

AI will make this loop visible because machines force us to define what we used to leave vague.

What is the task?

What is the environment?

What counts as success?

What must be remembered?

What must be forgotten?

What is allowed to change?

What must be isolated from the learner?

These are not only AI questions. They are human questions wearing technical clothes.

The person who only collects data will keep building a larger library.

The person who builds a world will keep generating experience.

And experience, when it can be reset, replayed, challenged, and judged, becomes something far more powerful than information.

It becomes a way to evolve.

[^1]: *Reinforcement Learning: An Introduction*, 2nd ed., MIT Press, 2018. https://incompleteideas.net/book/the-book-2nd.html
[^2]: "Mastering the game of Go without human knowledge," *Nature*, 2017. https://www.nature.com/articles/nature24270
[^3]: DeepMind, "AlphaGo Zero: Starting from scratch," October 18, 2017. https://deepmind.google/blog/alphago-zero-starting-from-scratch/
