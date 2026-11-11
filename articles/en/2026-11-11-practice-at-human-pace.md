# Practice Should Not Scale at AI's Pace

> 发布日期:2026-11-11 · [中文](../zh/2026-11-11-练习量不能按%20AI%20的产量算.md) | [English](../en/2026-11-11-practice-at-human-pace.md)

---

If AI can give you more exercises and more complicated assignments, should you keep increasing your workload? I don't think so. The amount of practice should follow the pace at which you understand something and get feedback. A machine can produce ten assignments easily. Understanding why you got one of them right may take repeated attempts.

An AI summary of an article about studying computer science in my notes drew my attention to the tension between adding assignments and increasing the burden of learning. I want to follow that question further: when both setting a task and supplying an answer become cheap, who controls how much learning is packed into the space between them?

This deserves some thought if you are using AI to learn a new skill. A tool can expand an exercise into a whole project. That does not do the understanding for you. What a learning plan can easily leave out is how long you need before you can use one piece of knowledge reliably.

## More tasks can leave the same difficulty unresolved

Suppose you want to learn to build a small tool for organizing a public book list. You enter titles and publication years. The program groups the books by year and keeps records without a definite year in a separate group. You can already ask AI to generate a working version. Now you want to understand how the program decides where each record belongs.

This is a conditional: the program uses a rule to decide what to do next. A record with a definite year goes into that year's group; one marked as undecided stays aside for you to handle. What you are learning is how to turn an everyday requirement into an unambiguous rule, then check whether the program follows it.

But ask AI for a learning plan, and it can readily add more work: import files, build a search box, connect a database, and add an attractive page. Each item may sound reasonable. You may even end up with something that looks much more like a product. The trouble is that the classification rule you did not understand may remain just as unclear.

Finishing a project has value. But if you cannot tell whether a record was misclassified because the rule was unclear or because the program failed to follow it, building another page may do little to resolve that difficulty. The task count has gone up. The difficulty has stayed put.

Suppose a record's year field says 2020/2021, and the program chooses the first year. The interface reports no error, and the table looks tidy. Yet a decision is hiding here: does that count as a definite year? If your requirement allows classification only when there is a single, unambiguous year, the record belongs in the group awaiting review. Making that distinction clear is something worth spending practice time on.

I worry about a tempting way to design assignments: someone sees what AI can complete and includes all of it in what the learner should complete. The basis for setting the workload quietly changes from what the person is beginning to master to what the tool can generate next.

That substitution is easy to miss because deliverables are easy to count and understanding is not. An extra page is immediately visible. Resolving an ambiguity may add just one sentence to an existing rule. If a learning plan rewards only visible additions, you have a reason to keep adding features and little reason to stop over that small distinction.

Faster grocery delivery does not add burners to your stove. The practice materials are like the ingredients; understanding, trying, and checking are the cooking. More ingredients may first mean more sorting and clearing up. Learning does let you combine familiar steps, so a person's capacity can change. Delivering more food does not, by itself, teach you how to cook it.

Back at the book-list tool, you may spend plenty of time copying prompts, waiting for generation, and switching between pages, while spending very little time understanding the rule. All that activity is real. It just does not automatically become practice in the action you wanted to learn.

The person offering help has work to do as well. In his [2013 essay](https://www.paulgraham.com/ds.html), Paul Graham describes how Stripe's founders would help people get set up on the spot after they agreed to try the service. This is a practitioner's account of early startups, customer acquisition, and user experience, rather than an experiment on educational outcomes.

That detail reminds me of the distance between giving someone access and helping them actually use something. Applied to learning arrangements, it prompts another check: when the learner gets stuck, can the person providing the assignment see where the difficulty is? Without that visibility, richer materials may simply pile up at the entrance.

So I would not assume that a plan suits me just because it looks comprehensive. I would check whether it leaves time to try the rule I have not understood, make mistakes, ask for help, and try again. If the time is missing, I would remove a peripheral task. The world will survive one fewer search box.

Removing peripheral work need not make the thinking easier. Working through two ways of writing a year may demand more thought than following a prompt to generate an entire page. To judge whether practice is challenging enough, look at whether you are making a judgment you could not make before. The number of files or features in the finished product will not tell you that.

## Check what you can still use after some time has passed

How, then, do you decide whether to add more? I would move the check a little later. Performing smoothly right now is one result. Being able to use the important knowledge after some time has passed is another. They may differ.

In the first experiment of their [2006 study](https://learninglab.psych.purdue.edu/downloads/2006/2006_Roediger_Karpicke_PsychSci.pdf), Roediger and Karpicke had 120 university students read prose passages, then compared rereading with recalling the material without looking at it. Researchers divided each passage into separate points, called idea units, and scored how many participants recalled correctly. On a test five minutes later, the rereading condition recalled 81% of those points, compared with 75% in the recall condition. One week later, the recall condition remembered 56%, compared with 42% in the rereading condition. The study measured memory for points in passages; it used no AI and did not test programming ability.

Change the time of the check, and the ranking of the same learning conditions reverses. That makes me reluctant to treat smooth performance immediately after practice as sufficient reason to add work. You have just seen the explanation, so following along may be easy. To find out whether the rule stayed with you, give yourself another occasion to use it.

Retrieval practice means briefly putting the answer aside and trying to bring what you learned back from memory. It can be small: hide the explanation of that part of the book-list tool and write, in your own words, what should happen when a year is missing. The important part is to produce an answer and then check it against the material, instead of silently nodding along.

You might say that remembering a rule is still a long way from being able to build something. Agreed. Learning also has to survive a change of material. Memorizing the explanation in front of you is not enough.

Butler's [2010 study](https://andymatuschak.org/files/Butler%20-%202010%20-%20Repeated%20Testing%20Produces%20Superior%20Transfer%20of%20Learning%20Relative%20to%20Repeated.pdf) took the check further. University students read material, then either repeatedly studied it or repeatedly answered questions and reviewed the correct answers. A week later, researchers tested them with previously unseen inference questions within the same knowledge domain. In the relevant experiments, repeated testing produced better performance. These were defined reading materials and inference tasks, not evidence that answering a few questions gives you a professional skill.

Another detail matters: in one comparison, repeatedly rephrasing the practice questions produced no better transfer than repeating the same questions. Transfer means using what you learned to answer a new problem. Novelty can be welcome, but exercises that look different do not necessarily train an additional ability.

For the book-list tool, a useful change might be a list you have not processed before. Can you explain which records should be classified, which should be kept aside, and why? You do not yet need to expand the exercise into a whole new application. Changing the material can already check whether you depend on the old examples.

The same Butler paper contains a finding worth building into the plan: when data from the first three experiments were pooled, rereading produced better memory for information that the practice questions had not tested. Choosing one small part to practice also leaves some content unattended for now. I would therefore still read the necessary material in full before narrowing the scope of the current exercise, rather than treating everything unpracticed as unnecessary knowledge.

I suggest checking against the existing goal before deciding where to add more. If I can use the rule reliably, I can introduce one kind of exception. If a different book list leaves me confused, I should understand that confusion first. This arrangement has not been tested in this article. The interval and the amount to add need adjustment through actual practice.

You may have a more urgent objection: real work will not wait until you have mastered every small action. AI also lets people take on whole projects. Should learning really retreat into isolated little exercises?

I favor working on complete projects. You can ask AI to help build the entire book-list tool, then choose one rule within it to study carefully. The overall goal can be large while the current practice stays small. Borrowing the capability for the remaining parts does not prevent you from gradually taking on more. What matters is naming what you intend to learn this time, rather than listing every feature AI can generate as something you must master today.

If the deliverable is due tomorrow, you may not have time to wait for a delayed check. You can finish the task first and record the parts for which you still depend on AI, then arrange practice after the deadline. That is a tradeoff between delivery time and learning time. Acknowledging that this session mainly got the work done makes the next step easier to plan than counting every borrowed capability as something you have already learned.

In their [2025 survey](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee_2025_ai_critical_thinking_survey.pdf), Lee and colleagues collected 936 examples of AI use from 319 knowledge workers. The analysis of whether participants reported critical thinking used 930 of those examples. Participants who were more confident that AI could do the specific task they reported were less likely to report critical thinking during that task. This confidence concerns the task at hand, not overall trust in AI; the study found no significant association between overall trust and whether participants reported critical thinking.

Participants also described time pressure as an obstacle to checking and reflection. Critical thinking here includes checking answers, verifying grounds for a claim, and judging whether a result fits the task at hand. These are reported experiences and associations, not proof that AI causes a decline in ability.

That survey makes me more interested in which activity loses time first when assignments grow. I worry that, in the rush to finish a complete project, explaining a rule, checking differences, and trying again are especially easy to cut. The result may still look good, while the learning plan has crowded out its own purpose.

## Let a follow-up check decide whether to add more

If you simply want a usable tool right away, getting AI to finish it is entirely reasonable. If you also want to learn something, set aside time for that part. Both goals can coexist. One completion record should not be expected to establish both outcomes.

Nor do you need to rebuild every feature yourself to demonstrate commitment. If you want to learn conditionals in this round of the book-list project, let AI handle the page and runtime environment. Keep your attention on the classification rule. When you want to learn file reading, arrange a separate round. A clear practice scope also makes it easier to ask for specific help.

I would keep the first answer you produced, too. Without it, the corrected version may hide the step you originally missed. Preserving one mistaken judgment can help you plan your next practice more than collecting another apparently perfect explanation.

Mistakes have different causes. An unclear rule calls for an explanation. Too few examples call for comparison. Too many operations leaving no attention for thought call for a smaller assignment. Identify the cause before adding practice, or you may keep treating a problem with the arrangement by prescribing more of it.

The follow-up check should fit your goal as well. If you want to recognize gaps in a rule, check whether you can find and explain them; you do not need to reproduce the entire program from memory. If you want to implement that function independently, then check whether you can write it yourself. Keep the help available during checks reasonably similar. Otherwise, you may compare yesterday's unaided product with today's AI-assisted one and have trouble telling where the improvement came from.

You can try this today with the hypothetical book-list tool, or with one small task you are already learning. No new software is required. Paper will do. The four steps below are my proposed exercise, not an AI learning method tested by these studies.

1. Write down the single judgment you intend to practice. For example, classify records with a definite year and retain those without one for review. Prepare one record with a year, one with the year missing, and one marked as undecided. Write where you think each belongs.

2. Ask AI to help build or explain the relevant function, then compare the result with your initial judgment. If they differ, find out whether the requirement was ambiguous, your understanding was wrong, or the program made an error. When you revise the rule, keep the reason beside it.

3. Tomorrow, use a different small book list. Before looking at yesterday's explanation, make the same classification judgment yourself and explain your reasons. AI can still assist with the other operations. Answer this particular step yourself first, then check it against the original material and the program's actual behavior.

   If you find that you merely recognized yesterday's answer, change another record and explain how it differs from the old one. Following an answer and explaining a new record require different actions. Be clear about the action you are checking.

4. Use that check to decide what comes next. If you can explain the rule and handle the new records, add just one kind of exception. If you cannot, return to the step that went wrong, reduce peripheral demands, and check again a few days later. Record how long it actually took, where you went wrong, and whether the help you requested addressed that error.

These intervals and increments are a starting arrangement, not an optimal recipe established by the research. A single success or mistake will not establish that the whole method works. Across several sessions, watch whether the same kind of judgment becomes steadier, whether the help you need becomes more specific, and whether you have time to understand your mistakes.

For now, write down that one rule and schedule tomorrow's check. The next assignment can wait. Leave room to find out what this attempt taught you.

## References

- Paul Graham, 2013, [Do Things that Don't Scale](https://www.paulgraham.com/ds.html). Used to discuss a helper's attention to the actual process of use. A practitioner essay about startups, not causal evidence about educational outcomes.
- Henry L. Roediger III and Jeffrey D. Karpicke, 2006, [Test-Enhanced Learning: Taking Memory Tests Improves Long-Term Retention](https://learninglab.psych.purdue.edu/downloads/2006/2006_Roediger_Karpicke_PsychSci.pdf). Uses Experiment 1's prose-recall results to distinguish immediate and delayed performance, without claiming an effect on programming learning.
- Andrew C. Butler, 2010, [Repeated Testing Produces Superior Transfer of Learning Relative to Repeated Studying](https://andymatuschak.org/files/Butler%20-%202010%20-%20Repeated%20Testing%20Produces%20Superior%20Transfer%20of%20Learning%20Relative%20to%20Repeated.pdf). Uses new-inference results from Experiments 1b and 2, the comparison showing no extra benefit from rephrasing practice questions, and the pooled untested-information result from Experiments 1a, 1b, and 2. Limited to the tested materials and tasks.
- Hao-Ping Lee and colleagues, 2025, [The Impact of Generative AI on Critical Thinking](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee_2025_ai_critical_thinking_survey.pdf). Used to discuss reported thinking effort and time pressure during AI use. Associations are not presented as causal evidence of declining ability.
