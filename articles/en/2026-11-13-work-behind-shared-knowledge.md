# The Work Behind a Shared Knowledge Base

> 发布日期：2026-11-13 · [中文](../zh/2026-11-13-经验库背后的那份工作.md) | [English](../en/2026-11-13-work-behind-shared-knowledge.md)

---

One way to share expertise is to ask experienced people to explain what they do, let AI organize it, and make the results available to everyone. Another way also schedules the work that follows: who receives reports from users, notices when conditions change, and updates the guidance. I favor the second. If expertise can be used repeatedly, the people who provide and revise it need time to keep working on it.

That cost is easy to miss. The system delivers the answers, while an experienced worker may have to squeeze in the corrections. Usage counts appear in reports; the effort spent explaining exceptions may appear nowhere. We can end up with a system increasingly good at answering, without assigning anyone to keep checking its answers.

I want to look at the work that continues after expertise enters a knowledge base. Making that work visible gives sharing a chance to last.

## Misconception 1: Once expertise is captured, the work is done

One of today's notes summarizes, with AI, a linked article about organizational change and AI. The summary emphasizes turning individual expertise into shared material. I agree with that direction. But moving from one person's experience to advice that colleagues can use at any moment involves more work than a single interview can cover.

Consider a published customer-support study. In their paper revised in November 2023, Brynjolfsson, Li, and Raymond analyzed conversation records from 5,179 support agents. Of those agents, 1,636 had conversation records after receiving access to an AI assistant. Most of the staggered rollout occurred between November 2020 and February 2021. For the smaller group whose issues resolved per hour could be measured, the researchers estimated an average gain of about 14%, with larger gains among workers who had been less skilled before access. The setting was one company and its contractors, and the evidence for lasting learning remained suggestive. An especially interesting part of the [original study](https://www.nber.org/system/files/working_papers/w31161/w31161.pdf) is how the recommendations were produced.

The system was trained on support conversations with information such as whether the issue was resolved, how long it took, and how the agent performed. It recommended replies and relevant documentation to agents, who could accept or ignore them. Experience entered the tool through records, then entered other people's work through the tool.

It looks like copying. Yet someone preparing the material still has to decide which conversations deserve to be learned from, what counts as a good result, and under which conditions the advice applies. AI's ability to organize text does not answer those questions automatically.

Raw records and usable expertise are also different things. A complete conversation may contain sound judgment, an approach that happened to work, and irrelevant information. Saving the whole conversation preserves the material without distinguishing what deserves reuse. Separating those parts, adding conditions, and answering other people's questions are professional work. AI can help, but the result still needs checking.

Building a knowledge base is a little like turning a cook's methods into recipes. The recipe stands for shared operational advice; tasting the dish stands for checking whether that advice works. Transcription can be made easier, but someone still has to taste: a change in ingredients may require a change in cooking. Support work involves software versions and human needs with more conditions than a single dish. Recording the steps does not capture every judgment.

That is why I care about what happens after the expertise has been extracted. When the product changes, the advice needs to be checked again. When an attempt fails, someone must distinguish poor execution from a condition missing in the guidance. Someone in contact with the actual work needs to examine these possibilities.

There is a boundary here. Rules with stable conditions and easily checked results can be reused for a long time once validated; an expert need not approve every use. Continuing work needs to be scheduled for advice whose conditions change, whose exceptions emerge, or whose mistakes are difficult to spot immediately.

Mixing these kinds of material creates trouble. Repeatedly debating stable rules wastes effort. Leaving context-dependent advice unattended allows it to be treated as a stable rule. At a minimum, the knowledge base should identify which kind each item is.

It also helps to distinguish who first supplied the material, who turned it into usable guidance, and who later found a problem. They may be the same person, or they may not. A single name at the top of a document may fail to make those different contributions visible. What matters is a traceable history of changes, rather than a permanent claim to credit.

## Misconception 2: More use always means a more valuable contribution

Usage counts tell us how often the system brings up a piece of advice for people to use. They are useful for seeing which material people often need. But they make popular answers easier to see than the conditions that prevent misuse.

The support study illustrates how the system uses earlier information in a hypothetical example. A customer says they cannot track their employees' working hours while those employees are on business trips. A customer using the premium version should have access to the feature, so the agent needs to troubleshoot a technical problem. A customer using the standard version needs to upgrade to the premium version. The same description of the problem calls for a different response because of software-version information supplied earlier.

If a team turns only the second response into guidance, the system may quickly learn to recommend an upgrade. The answer is short and the action is clear. Once an experienced worker adds the missing condition, some uses should be blocked and redirected toward troubleshooting. Adoption of that recommendation then falls, while the guidance becomes more reliable.

That is an awkward incentive. If we reward only how often advice is adopted, might contributors prefer answers that are easy to use over qualifications that prevent a few uses? This is an incentive problem I worry about, not an inevitable outcome established by the evidence.

In their [joint analysis from 2009](https://bear.warrington.ufl.edu/brenner/mar7588/Papers/kahneman-klein-2009.pdf), Kahneman and Klein connected reliable intuition to an environment with learnable regularities, sufficient practice, and useful feedback. They also emphasized that a person may have expertise in one kind of judgment without having it in another. Their article is a synthesis of research, not a new controlled experiment.

The implication for a knowledge base is practical. Being fast at resolving problems does not make someone's views on every problem suitable as standard answers. A more useful contribution preserves the conditions that person recognizes, then lets subsequent results test them.

Research on educational tools also shows how specific this preparation can be. In a mathematics experiment at a Turkish high school, Bastani and colleagues supplied a customized AI tutor with teacher-prepared solutions, common mistakes, and corresponding hints. They hired teachers part-time to help develop the material. The intervention took place in the fall of the 2023–2024 school year and studied short-term mathematics learning, rather than workplace knowledge bases. The [tool-design section of the paper](https://hamsabastani.github.io/education_llm.pdf) makes clear that useful input involved much more than an instruction for AI to explain things patiently.

When recording contributions, then, I would also look at whether qualifications were added, misuse was discovered, and outdated advice was withdrawn. A timely withdrawal may be more valuable than another document. Its value still has to be judged through use; we should not invent a new leaderboard for the number of withdrawals.

This changes how we ask about guidance. Asking only whether it was useful can produce a vague reply that it was fine. Asking which condition led the user to choose which action gives us a chance to find an omission. Maintainers need sufficiently specific results. Otherwise they can do little more than polish the wording again. More complete prose does not necessarily mean better problem solving.

## Misconception 3: Sharing will naturally be rewarded later

Someone could reasonably argue that a company already pays salaries, and sharing work experience is part of the job. Paying separately for every piece of advice could turn a team into a marketplace and encourage piles of useless documentation. Experienced people can also be stubborn. Contributing the original guidance should not give anyone a monopoly on revising it.

I share those concerns. Sharing need not be priced by the item, and expertise should not become private territory that nobody else may touch. But if it is part of the job, it must occupy working time, with an explicit choice when tasks compete.

If a person must complete their existing assignments while also explaining methods, documenting exceptions, and checking feedback, evaluating them only on the original assignments leaves the work plan unchanged while adding new work. Praising their generosity does not replace adjusting the plan.

The conflict is straightforward. The original delivery has a deadline; maintaining the guidance may have none. A late delivery brings immediate questions; outdated guidance may take much longer to be exposed. When the two compete and maintenance keeps getting postponed, unwillingness to share is not the only possible explanation. Relying on enthusiasm means that work without a clear place in the schedule keeps giving way.

The support study specifically raises an incentive problem: top workers are generally not compensated for their contributions to the training data. It asks what happens to the system's ability to address new problems without those contributions. This is a long-term challenge raised by the authors. The paper does not establish which arrangement for distributing rewards works best.

My judgment is that sharing expertise should bring at least three concrete things: time for maintenance, feedback from use that reaches the contributor, and recognition of that work when performance is evaluated. Additional compensation is open to discussion. A promise that everyone will eventually benefit is not enough.

Recognizing the work also means looking beyond the most conspicuous experts. Someone else may make the guidance understandable, identify an overlooked condition, or organize the results of a failure. Recognition should follow contributions that can be checked. Otherwise the knowledge base becomes another way to celebrate existing reputations, while the people doing the organizing remain invisible.

Feedback is particularly important. People who supply expertise need to know what happened when others followed it. If they provide the guidance but the results stay inside the system, they lose the information needed to see where their explanation was incomplete or has become outdated.

In a [2013 essay](https://paulgraham.com/ds.html), Paul Graham recalled building online stores on merchants' behalf in Viaweb's early days. While using the software, he would discover a missing feature, implement it, and resume building the store. This is a participant's retrospective account, not a law of success for every startup. The detail that interests me is that the person building the tool also encountered the problems it did not solve.

Contributors to shared expertise need that kind of contact too. We cannot simply ask them to supply knowledge at the beginning and then send thanks while keeping failures out of sight. Thanks feel good. Information about failure gives them more to work with in the next revision.

Assigning maintenance to someone does not establish that they are always right. Others should be able to challenge the guidance, and changes should retain their supporting reasons. When new results overturn an old method, timely correction should count as work well done. Otherwise people have another reason to defend whatever they originally wrote.

## Misconception 4: We must organize all our knowledge before addressing this

There is no need to begin with a large new system. More material can make it harder to identify what deserves maintenance. Turning every conversation into a document also hands the burden of searching and filtering to the next user.

I propose starting with one frequently used recommendation that depends on professional judgment, then scheduling its upkeep. Limit the scope to that item. See whether it can receive sustained attention before expanding the arrangement. This is my proposal for organizing work, not a result established by the studies.

1. Find the recommendation and add both its conditions of use and a situation in which it should not be followed. In the working-hours example, record the software version rather than just the action to take. If the source includes private information, preserve only rules authorized for sharing.
2. Assign a maintainer and reserve time in the next work plan to review it. Also identify which other work will be reduced to make room. The maintainer could be the original contributor or someone else who understands the material. Do not assume an experienced colleague will naturally fill the gap after everything else is finished.
3. Return the actual results of use to the maintainer, who can use the evidence to decide whether to retain, revise, or withdraw the guidance. Let others challenge that decision. Recording what changed and why is more useful than merely recording another addition to the library.

Whether this is worth doing depends on the results. I would check whether the change reduced misuse and helped users distinguish the relevant conditions more quickly, then weigh that against the time spent on maintenance. If it merely creates more forms without helping people judge, shrink the arrangement.

Do not rush to declare success, either. Faster handling could mean that the revision helped, or that this particular problem was easier. Keep the versions from before and after the change. Check whether the new results actually concern the condition that was revised before deciding to keep observing or expand use. This small experiment helps reveal whether maintenance is happening in practice; it cannot by itself establish that the entire arrangement is effective.

People working alone can try this too. When adding a rule for AI to use repeatedly, also specify what kind of result should prompt a review. Organizing the rule and checking its results both require your time. The first should not count as completion while the second is left for whenever you happen to be free.

I would also give the experiment an exit condition. If the material becomes stable and maintenance no longer produces useful changes, move it to review as needed. If its conditions of use remain impossible to state clearly, reduce automatic recommendations and retain human judgment. Formally scheduling work does not make it permanent. It, too, should be able to finish, shrink, or stop.

Here is a specific question to ask: Who last changed the piece of advice you reuse most often, and what result prompted the change? If you can identify neither a person nor a result, the advice may still be useful for now, but it does not yet have continuing maintenance.

Both approaches at the beginning may produce an attractive knowledge base. The difference appears the next time conditions change. One waits for an experienced person to fill the gap voluntarily; the other has already reserved time for the work. I hope sharing expertise reaches that second stage. Then the ease of using it will no longer make the work behind it disappear.

## References

- [Generative AI at Work](https://www.nber.org/system/files/working_papers/w31161/w31161.pdf), Erik Brynjolfsson, Danielle Li, and Lindsey R. Raymond, 2023, revised November. Used for the support assistant's effects, training material, version-dependent advice, and incentives for contributors. The study concerns one company and its contractors; evidence of learning is suggestive.
- [Conditions for Intuitive Expertise: A Failure to Disagree](https://bear.warrington.ufl.edu/brenner/mar7588/Papers/kahneman-klein-2009.pdf), Daniel Kahneman and Gary Klein, 2009. Used for the relationships among regularities, practice, feedback, and the boundaries of expertise. A synthesis of research.
- [Generative AI Without Guardrails Can Harm Learning: Evidence from High School Mathematics](https://hamsabastani.github.io/education_llm.pdf), Hamsa Bastani and colleagues; publication year is not stated in the supplied version. The intervention took place in the fall of the 2023–2024 school year. Used for teacher involvement in preparing solutions, common mistakes, and hints; not to infer the effectiveness of workplace knowledge bases.
- [Do Things that Don't Scale](https://paulgraham.com/ds.html), Paul Graham, 2013. Used for his account of discovering and implementing missing Viaweb features while working on merchants' behalf. The case does not represent every startup.
