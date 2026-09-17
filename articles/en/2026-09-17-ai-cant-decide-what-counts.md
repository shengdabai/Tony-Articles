# AI Can Clean Messy Data. It Can't Decide What Counts.

> 发布日期:2026-09-17 · [中文](../zh/2026-09-17-AI 能整理脏数据，却不能替你决定什么算数.md) | [English](../en/2026-09-17-ai-cant-decide-what-counts.md)

---

This morning, I was reviewing several small automation systems when I noticed the same problem appearing in different clothes.

One dashboard counted visits. Another counted people. Both called the result “users.”

One expense report grouped costs by approval date. But some of those costs belonged to work done in the previous month.

One workflow marked a task “complete” as soon as a file was generated. Nobody had checked whether the file was correct, usable, or actually delivered.

None of these systems had a calculation problem. The formulas were doing exactly what they had been told to do.

The problem came earlier.

Nobody had decided what counted.

That distinction matters more now because AI can process a pile of records, extract fields, classify text, and build a polished dashboard before we have finished asking whether the columns mean what we think they mean.

Speed used to expose confusion slowly. AI lets confusion scale.

## Clean data can still carry a dirty meaning

When people talk about messy data, they usually mean visible mess: inconsistent dates, missing fields, duplicated rows, names written in different formats, or numbers trapped inside images.

AI is becoming very good at this kind of cleaning. It can read a receipt, normalize a date, summarize a conversation, tag a complaint, and turn unstructured text into a neat row.

But there is another kind of mess that looks perfectly clean.

Is a “customer” someone who registered, someone who paid, or someone who paid and did not request a refund?

Does “monthly revenue” mean orders placed this month, cash received this month, or service delivered this month?

Does “study time” include a video playing in the background while I answer messages?

Does an AI agent finish when it produces an answer, when the answer passes a check, or when the answer changes a real decision?

No model can discover the one correct definition hiding inside those words, because there may not be one. The definition depends on the decision we are trying to make.

This is why the useful standard for data is not “clean in the abstract.” The U.S. National Institute of Standards and Technology describes data quality in terms of fitness for purpose, including qualities such as accuracy, completeness, consistency, and timeliness. In other words, quality belongs to a relationship between data and use, not to the data alone. ([NIST Research Data Framework](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/1500-18/NIST.SP.1500-18r2.html))

A beautifully formatted number can still be unfit for the decision in front of us.

## Every metric hides a counting contract

I have started thinking of every important metric as a small contract.

Before the number appears, someone has to settle at least six things:

1. **Object:** What exactly are we counting—a person, visit, order, task, attempt, or document?
2. **Event:** What must happen before it counts?
3. **Time:** Which date owns the event—creation, payment, approval, delivery, or completion?
4. **Exclusions:** What looks similar but must not be included?
5. **Authority:** Who decides when a case sits on the boundary?
6. **Decision:** What action will change when this number changes?

I call this a counting contract because two reasonable people can otherwise produce two different answers from the same records and both believe they are right.

Suppose I want to measure whether I am learning consistently.

If I count any day when a course was open on my screen, I will get one number. If I count only days when I produced a note in my own words, I will get another. If I count only days when I used the idea in a real task, I will get a third.

The tracking tool is not the problem. My definition of learning is.

The same thing happens in work. A team can celebrate a rising number of leads while quietly changing “lead” from “a qualified conversation” to “anyone who filled out a form.” The chart goes up. The business does not.

And it happens in AI systems. If “successful run” means “the model returned text,” reliability looks wonderful. If it means “the requested artifact passed validation and reached the right place,” the number may look very different.

Measurement does not merely describe a system. It teaches the system what to become.

## Let AI interpret; let rules count

The answer is not to remove AI from the workflow. It is to give AI the right job.

AI is especially useful at the edge, where reality arrives in messy forms: a voice note, an invoice, a job description, an interview transcript, a customer comment, or a folder full of badly named files.

It can propose structure. It can extract a likely date, summarize intent, suggest a category, or flag an unusual case.

But once the meaning is settled, ordinary rules should do as much of the counting as possible.

A healthy workflow often looks like this:

**messy input → AI interpretation → structured fields → rule-based validation → calculation → action → exception log**

The model may infer that a sentence describes a refund. A fixed rule decides that refunds do not enter recognized revenue. The model may extract a deadline from a message. A deterministic check rejects impossible dates. The model may draft a classification. A person reviews cases that fall below a confidence threshold or carry serious consequences.

This division is not glamorous, but it is powerful.

AI handles variation. Rules preserve meaning. People own consequences.

The research community has been moving in a similar direction for years. The paper *Datasheets for Datasets* proposes documenting a dataset’s motivation, composition, collection process, intended uses, and maintenance—not merely publishing the data and assuming its meaning is obvious. ([Gebru et al., *Datasheets for Datasets*](https://arxiv.org/abs/1803.09010))

Modern data tools also build “semantic layers” so teams can define shared metrics once instead of recreating slightly different business logic in every report. The technology is useful, but the deeper lesson is simple: a shared definition is infrastructure. ([dbt Semantic Layer documentation](https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl))

## Definitions should be stable, not frozen

There is an obvious objection.

The world changes. A definition that works today may become wrong next month. If we turn every judgment into a rigid formula, we can build a system that is consistent and foolish at the same time.

I agree.

A counting contract should be stable enough to compare results, but easy enough to revise when reality changes. The key is to change it deliberately.

Give the definition an owner. Record when a new version takes effect. Recalculate historical data only when comparison requires it. Keep ambiguous cases visible instead of forcing them into the nearest category.

Most importantly, do not encode every temporary preference as a permanent rule.

Rules should hold the meaning that must remain consistent. AI should handle the variation that cannot be listed in advance. Humans should revisit the boundary when exceptions begin to pile up.

That last signal is valuable. A growing exception list is not merely operational noise. It often means reality has outgrown the categories we designed for it.

## A ten-minute test you can run today

Pick one number you look at regularly: weekly study hours, completed tasks, qualified leads, successful AI runs, published pieces, or anything else that influences your behavior.

Now write its counting contract in six lines:

- I am counting ______.
- It counts only when ______.
- It belongs to the period when ______.
- I exclude ______.
- Borderline cases are decided by ______.
- When the number changes, I will change ______.

Then give the same raw examples to another person and ask them to calculate the metric without seeing your answer.

If the two results differ, you probably do not have a data problem yet. You have a meaning problem.

Fix that before adding another model, dashboard, or automation.

I used to think the main advantage of AI was that it could turn unstructured information into structured data. I now think that is only half the story.

The more easily machines can organize the world, the more responsibility we have to define the world they are organizing.

AI can help us count almost anything.

It still cannot decide, on our behalf, what should count.
