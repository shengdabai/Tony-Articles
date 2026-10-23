# Keep the Reason for the Handoff

> 发布日期:2026-10-23 · [中文](../zh/2026-10-23-把交接理由留下来.md) | [English](../en/2026-10-23-keep-the-reason-for-the-handoff.md)

---

An experiment conducted with a consulting firm produced an awkward pair of results. One group of consultants using AI did better at developing a product idea. A separate group using the same version of AI was more likely to give the wrong answer on a business problem that combined a spreadsheet with interviews. The tool had not suddenly become stupid. The task had changed. I think one human skill is worth preserving in AI assisted work: being able to say why a step was handed to the machine, and why a person took it back. If all we keep is the polished deliverable, we will have to guess again when the next task looks different.

A summary of a talk about learning loops describes learning as a cycle of action, feedback, and revision. It raises a more specific question: at the moment when a person and an AI hand work to each other, where does the revision go? A system that stores only the finished product and a thumbs up will struggle to know when to stop next time. I will struggle to tell what I actually learned.

## How can faster work be more wrong?

Because the task can change, while a familiar workflow keeps moving.

The [consulting experiment](https://www.hbs.edu/ris/Publication%20Files/dell-acqua-et-al-2026-navigating-the-jagged-technological-frontier_5c589c8c-fbb5-458f-b285-c944746cd717.pdf) involved 758 consultants. Researchers used the GPT-4 available in 2023 and assigned different participants to two kinds of work. The paper was published in 2026. One kind involved inventing a shoe product, segmenting its market, and writing supporting material. In that arm, the consultants with AI completed 12.2% more subtasks on average. The other kind required participants to combine a spreadsheet with interview material and recommend how a business should grow. In that arm, the two AI groups combined were about 19 percentage points less likely to reach the correct answer than the group without AI.

These results matter precisely because both kinds of work look like consulting. A job label cannot tell us whether to hand the entire job to AI. The researchers also found that AI assisted recommendations in the second kind of task sounded more coherent and persuasive even when the underlying conclusion was more likely to be wrong. Fluent language can make a decision feel settled before it has been checked. The danger is not a clumsy draft. It is an untested judgment dressed for a presentation.

The business problem contained a consequential detail. A reader looking only at the spreadsheet could reach one answer; the interviews supplied information that could change the recommendation. Turning all the material into a smooth report can be useful. Deciding whether to accept that report depends on whether the information that changes the conclusion actually enters the decision. The handoff reason I would keep is therefore more precise than “AI can write reports”: when a recommendation depends on two kinds of evidence correcting each other, someone must identify which interview detail changes the conclusion suggested by the spreadsheet.

A single experiment is not a permanent capability chart for every model. The consultants, the selected problems, and that particular GPT-4 set its scope. A current model might solve the very same problem. But as long as tasks change, deciding where the handoff belongs remains work. When the model changes, test it again, especially on problems that look familiar but contain one consequential hidden condition.

A successful delivery tells us that this delivery worked. To turn it into experience we can use again, we also need to answer two questions. What signal made me comfortable letting AI continue? What signal made me take over? Delete those answers, and the lesson becomes “the tool worked well.” That is easy to write down and almost useless for the next decision.

A subtler mistake is to count an answer that a person corrected at the end as something AI completed on its own. The next time the workflow expands automation on the strength of that result, the human correction may be missing from the rule, and the error returns. The report says complete; the process is missing a step. Mark that step before comparing tools, or we cannot even say what we are comparing.

## When should I take the task back?

At a point where I can check what matters.

A [2025 survey](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee_2025_ai_critical_thinking_survey.pdf) from researchers at Microsoft and elsewhere gathered 936 work examples from 319 knowledge workers. Participants described a shift from producing material themselves toward checking information, integrating answers, and overseeing the task. Greater confidence in AI on a particular task was associated with less self reported critical thinking. This was a survey of perceptions and associations. It did not show that AI use caused anyone's skills to decline.

It makes me want to replace an easy question, “Can AI do this?” with a more useful one: after it has done it, what independent way do I have to catch an important mistake? An independent check might be the original document, an executable test, a person who knows the domain, or an observable result in the world. Then ask what happens if a mistake slips through. The available check and the cost of failure together determine where I should take over.

For work that is low risk, easy to reverse, and immediately observable, AI can often go further. It can turn confirmed points into versions of different lengths, for example, while a person chooses the right one. If the points have not been confirmed, attractive formatting does not help. A spreadsheet figure can be recalculated; a condition in an interview must be checked against the interview. “It looks plausible” is not an adequate substitute for either check.

Someone might object that work is busy enough without keeping a record of every handoff. Fair. For a tiny task with a low cost of failure, where checking costs more than doing it again, use the tool and fix the occasional error. Requiring a person to do everything once before AI touches it would erase much of its benefit. I am concerned with tasks that recur and can pass an error into later work. There, a little effort can turn one correction into a rule for a future task.

There is a harder case: what if the person taking over does not understand the subject either? Calling that “human review” does not create expertise. We can narrow the AI's authority, ask it to list the evidence to inspect and the conditions it may have missed, and then consult an original source or a qualified person. If no checking path exists, the AI's explanation of its own answer is not acceptance evidence. Knowing to stop under that condition is itself a handoff reason worth keeping.

The point of a handoff is not for people to beat machines every time. People make mistakes, and machines can sometimes be steadier. The point is for whoever is responsible to know what evidence would allow the work to proceed and what evidence would change the decision. Without that gate, saying that AI is responsible may simply leave the consequences with the last person who clicked approve.

The timing of the check matters, too. Catch a bad sentence in a draft and it is cheap to change. Catch the same error after that sentence has become the input to another step, and more work has to be inspected. The handoff point may therefore change as the task progresses: the closer a decision is to being hard to reverse, the stronger the evidence needed to let it proceed. One fixed human review gate for every step can become a ritual that misses the detail that matters.

## What should the record contain?

Write down a trigger, not an impression.

A reusable note can be as short as a sticky note: What was the task? How far did I let AI go? What did I see that made me intervene? Which evidence changed the result? Under what condition should I use the same rule again? This is not a meeting transcript or an archive of the whole conversation. More stored text does not ensure that the crucial sentence can be found. “AI got this one wrong” will not tell anyone whether the lesson applies to a different subject.

Consider the consulting problem again. “AI cannot do business analysis” is a poor record; it turns a failure on one selected task into a universal verdict. A better record is: “When the growth story in the spreadsheet conflicts with a constraint in the interviews, mark the conflict before writing the recommendation.” It names a visible trigger and an action. If the next task has no interviews, or if the spreadsheet already incorporates that constraint, we must revise the rule. Rules expire. What matters is knowing what supported them.

In their 1988 [article on teaching for transfer](https://files.ascd.org/staticfiles/ascd/pdf/journals/ed_lead/el_198809_perkins.pdf), education researchers D. N. Perkins and Gavriel Salomon argued that people often fail to apply something learned in one setting to another. They proposed deliberately extracting a relationship that can be reused, then looking for its counterpart in a new setting. This is a teaching framework, not a recent experiment estimating a success rate. Applying it to AI handoffs is my proposal; the research did not test this record keeping method. The relationship I want to extract is the condition that triggers a handoff. Saving the previous answer alone does not carry that condition over.

Changing the pan in your kitchen presents a small version of the problem. Memorize the heat setting and the number of minutes for the old pan, and a faster heating pan may ruin dinner. Watch when the food changes color and how much liquid remains, and you have a chance to adjust. The shared mechanism is using feedback to decide when to intervene. The difference is that a cooking result is often visible immediately. The outcome of a business decision can arrive late and be influenced by many other factors. A work record therefore has to distinguish signals we can check now from conclusions that must wait.

This is why I hesitate to call “I used AI” a measure of learning. The number of words the machine wrote or the number of steps it ran may have little to do with whether I make a better decision next time. If I can identify a new trigger and change the division of work when it appears again, the experience has left something useful behind. If I merely fix each output by feel at the end, while the process never records why, my effort does not feed the collaboration.

The record also needs room for a counterexample. After writing “take over when the spreadsheet and interview conflict,” ask whether some apparent conflicts are only differences in wording or units. Ask whether both sources could agree yet omit the same important fact. A rule that collects only confirming examples soon becomes another habit that no one examines.

I would leave one more small space in the note: what do I not know yet? Perhaps the original material is missing, or perhaps I have never handled this kind of task. Stating the unknown protects the next decision better than pretending the rule applies everywhere. When new material arrives, test it against that space. If it overturns the rule, change the rule rather than invent an excuse for the old conclusion.

## Will I recognize it in a new task?

Try it with changed conditions.

Hours of practice do not automatically become judgment that travels to another setting. A [meta-analysis](https://gwern.net/doc/psychology/2014-macnamara.pdf), which combines results from multiple studies, examined deliberate practice: structured activities designed to improve performance, such as repeatedly working on a weak point and checking the result. A 2018 corrigendum revised some of its 2014 estimates: differences in practice were associated with about 23% of the variation in performance for highly predictable activities, such as running, versus about 6% for activities with low predictability, such as handling an aviation emergency. These are associations, not a guaranteed return from an extra hour of practice. The studied domains cannot be mapped directly onto today's AI work. The useful reminder is that repeating a task is less likely to be enough when the setting keeps changing.

In the consulting problem, the step worth practicing may not be writing another elegant recommendation. It may be spotting where the materials disagree. We can test whether a person or a machine does that step better, provided we can compare the conflicts each one finds with the underlying material. If a workflow rewards only the speed of the finished report, people may become very good at submitting quickly. If it also records which kind of conflict changed an earlier decision, the next task begins with a condition that can be tested.

Here is a small test of this proposal. Choose a recurring task with a manageable cost of failure, and keep its original material. Before AI starts, write one sentence predicting where you expect to take over. After AI finishes, check that point against the original material and add the evidence that actually made you intervene or let the work proceed. Finally, use a similar task with a different condition and see whether the sentence helps you decide where the handoff belongs. The steps are short enough to complete.

How do you judge whether it worked? On the second task, the note should help you spot a reason to intervene earlier, or justify skipping a check that is no longer needed. If both predictions fail, that is still a result: the trigger was too vague, or perhaps you lack a genuinely independent way to check. Make the condition more precise or admit that limit. Do not grade yourself on how impressive the report looks. That was the misleading signal in the consulting experiment.

When choosing the second example, do more than change a filename. Change one condition that could alter the conclusion: perhaps two sources go from conflicting to agreeing, or perhaps a key fact goes from checkable to temporarily unavailable. Then you can see whether the note captured a relationship between the pieces of the task or merely remembered the surface of the first document. If it recommends the same handoff in both cases, it may be written too broadly.

The question I want to keep is simple: when the next task changes, can I explain why I hand the work to AI here and take it back there? If I cannot, I will save one handoff reason first. When that reason survives a new task, the learning loop has actually moved forward.

## References

- [Navigating the Jagged Technological Frontier](https://www.hbs.edu/ris/Publication%20Files/dell-acqua-et-al-2026-navigating-the-jagged-technological-frontier_5c589c8c-fbb5-458f-b285-c944746cd717.pdf), Fabrizio Dell’Acqua et al., 2026. Used for the consulting experiment, its two task types, and the risk of persuasive but wrong recommendations. The experiment used GPT-4 as available in 2023.
- [The Impact of Generative AI on Critical Thinking](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee_2025_ai_critical_thinking_survey.pdf), Hao-Ping Lee et al., 2025. Used for workers' reported verification and oversight. The survey does not establish long term skill change or causation.
- [Teaching for Transfer](https://files.ascd.org/staticfiles/ascd/pdf/journals/ed_lead/el_198809_perkins.pdf), D. N. Perkins and Gavriel Salomon, 1988. Used to explain deliberate connection making across settings; it is a teaching framework.
- [Deliberate Practice and Performance in Music, Games, Sports, Education, and Professions, with corrigendum](https://gwern.net/doc/psychology/2014-macnamara.pdf), Brooke N. Macnamara et al., 2014; corrigendum 2018. Used for the association between practice and performance across levels of predictability. The article uses the corrected estimates.
