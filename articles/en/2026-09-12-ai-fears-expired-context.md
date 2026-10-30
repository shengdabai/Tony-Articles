# AI Doesn't Fear Hard Problems. It Fears Expired Context.

> 发布日期:2026-09-12 · [中文](../zh/2026-09-12-AI 不怕难题，它怕过期的上下文.md) | [English](../en/2026-09-12-ai-fears-expired-context.md)

---

Before writing this article, I did something that looked unrelated to writing.

I checked a list of topics I had already published.

I was not looking for inspiration. I was trying to avoid producing a new-looking version of an old idea. An AI can change the title, rearrange the examples, and polish every paragraph. If its record of my past work is incomplete, though, the result may still be a repetition.

The sentences are new. The work is not.

That small routine made me notice a mistake I often make when thinking about AI. I keep asking whether a task is hard enough for the model. But in many real workflows, difficulty is not the main problem.

The main problem is that the facts around the task keep expiring.

A powerful model working from yesterday's context does not become slightly less useful. It can become confidently wrong. It may reason perfectly and still complete the wrong task.

## Difficulty is not the same as instability

In one of my notes today, I came across a useful distinction between two kinds of work.

The first kind is cumulative. A result can be tested, kept, and built upon. If a proof is valid, a program passes a stable test, or an experiment reveals a repeatable result, tomorrow's work can start from that point. Progress does not have to be rediscovered every morning.

The second kind is non-stationary. The environment changes while the work is happening. A customer's concern changes. A dependency slips. A teammate revises a decision. A platform changes a rule. Yesterday's correct move may be today's mistake.

This creates a strange reversal.

A mathematically difficult problem can be easier for an AI system to improve on than a simple coordination task. The difficult problem may have fixed rules and a clear verifier. The coordination task may have no complicated equation at all, but its target keeps moving.

A proof does not renegotiate its deadline on Wednesday afternoon. A project does.

That is why benchmark strength and workplace reliability are not the same thing. Benchmarks usually hold the question still long enough to measure the answer. Real work often changes the question before the answer arrives.

## A smarter model cannot repair stale input

When an AI workflow disappoints us, the most tempting response is to upgrade the model or rewrite the prompt.

Sometimes that helps. But it does not solve expired context.

Imagine an assistant preparing a weekly plan. It knows the goals, deadlines, and available time as of Monday morning. On Tuesday, one deadline moves. On Wednesday, a promised input fails to arrive. On Thursday, the most important outcome changes.

If none of those changes reaches the assistant, stronger reasoning only helps it optimize Monday's world more thoroughly.

This is not a theoretical edge case. Google's production machine-learning guidance includes a blunt rule: [know the freshness requirements of your system](https://developers.google.com/machine-learning/guides/rules-of-ml). It asks teams to examine what happens when a model is a day, a week, or a quarter old. The same guide warns that data changes between training and serving can create skew even when the underlying machinery works as designed.

NIST makes a related point in its work on [monitoring deployed AI systems](https://www.nist.gov/publications/challenges-monitoring-deployed-ai-systems-center-ai-standards-and-innovation): testing before deployment happens in controlled conditions, while real use brings dynamic inputs and unforeseen outputs. Monitoring is not an optional layer added after the “real” system is complete. It is part of what makes the system real.

The lesson applies far beyond machine-learning teams.

If I ask AI to compare tools using an old budget, summarize a project from an abandoned plan, or prepare an article from an incomplete topic history, the failure began before the prompt. The system was missing a way to notice that its world had changed.

## Every important fact has a half-life

I have started thinking about context as if it had a half-life.

This is a practical metaphor, not a scientific measurement. It asks a simple question: how long can this fact be safely reused before I must check it again?

Some context decays slowly. My preferred writing voice, a durable principle, or the purpose of a long-running project may remain useful for months.

Some context decays at a medium speed. The structure of a project, the tools it depends on, or who owns a decision may remain reliable for weeks, then change without much ceremony.

Some context decays almost immediately. Today's priority, the latest file, an approval state, a deadline, or whether a topic has already been published can become stale in hours.

Most AI setups put all of these facts into one undifferentiated pile called “context.” That is convenient, but dangerous. A beautifully written instruction from six months ago can sit beside today's status update, and the model has no natural sense of which one is aging faster.

So here is the test I now find more useful than “How smart is the model?”

**Is the context's half-life shorter than the workflow's refresh interval?**

If the answer is yes, the workflow is already unreliable.

This does not mean checking everything before every action. That would replace stale context with delay and noise. The point of the half-life is to separate facts that can be safely cached from the few facts that can change the decision. Refreshing a stable preference every hour is waste. Rechecking a changed deadline before sending the work is basic hygiene.

Suppose a daily writing system refreshes its notes every morning but refreshes its published-topic list once a month. The prose source is current, while the duplication check is stale. The system may produce excellent articles and still fail at the one thing that protects the body of work.

Or suppose a project assistant reads the plan at kickoff but never sees later decisions. It may finish every assigned step and make the project harder to finish.

In both cases, the issue is not a lack of intelligence. It is a mismatch between how fast reality changes and how often the system looks again.

## Write a freshness contract before another prompt

For any repeated AI workflow, I now want a small “freshness contract.” It does not need to be software. A note with four lines is enough:

- **Critical fact:** What information could change the action?
- **Source of truth:** Where should the AI check it?
- **Invalidation event:** What makes the old value unsafe to reuse?
- **Stale behavior:** What must the AI do when it cannot confirm freshness?

Take the article workflow.

The critical facts include today's material, the publication date, and the history of published topics. The source of truth is not the model's memory; it is the current record. A newly published article invalidates the previous topic list. If the list cannot be checked, the correct stale behavior is not “make a reasonable guess.” It is “do not claim the topic is new.”

The same pattern works for a personal weekly review. The critical facts might be current commitments and remaining time. A new commitment invalidates the old plan. If the calendar cannot be read, the assistant should draft options without pretending it knows the schedule.

This last line matters. We spend a lot of effort telling AI what to do. A freshness contract also tells it when its knowledge is no longer good enough to act.

That boundary makes the system less fluent for a moment. It may have to re-read a source, request an update, or leave a decision open. But it makes the whole workflow more trustworthy.

The deeper point is that self-improvement requires more than remembering past successes. It also requires detecting when the past has stopped describing the present.

Stable problems reward memory, even when they remain extremely hard. Changing environments reward renewal.

So when an AI workflow fails, I no longer want to ask only whether the model was capable enough. I want to ask a more uncomfortable question:

Did the system know which parts of its world had expired?
