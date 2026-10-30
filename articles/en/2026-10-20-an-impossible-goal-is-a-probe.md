# An Impossible Goal Is a Probe

> Published: 2026-10-20 · [中文](../zh/2026-10-20-不可能的目标是一支探针.md) | [English](../en/2026-10-20-an-impossible-goal-is-a-probe.md)

---

Asking AI for something it cannot currently deliver can be more honest than giving it a reasonable target. A reasonable target may already contain a concession to the old way of working. We think we are describing the result we want, when we are really describing the size of an improvement we know how to make. A higher target may produce no miracle. It can, however, expose the question we quietly skipped: what constraint makes the familiar route seem like the only route?

I think of that request as a probe. A probe is useful because it hits something and brings information back. It does not make the obstacle vanish. The distinction matters: an ambitious target helps us find another route only when we connect it to a test we can check. Connected solely to AI's enthusiasm, it can become a convincing performance we put on for ourselves.

## What does a higher target do?

It makes us inspect the old route. An AI summary of a saved piece relayed a proposal: give AI a seemingly unreasonable goal and resist the urge to lower it the first time the model says it cannot be done. This is a proposal to try, not a research finding that this way of asking works. I agree with exploring before conceding, but I want to go a step further: what exactly should the model deliver after we raise the bar? I do not want a cheerful yes. I want an account of the constraints, alternative routes, and ways to check them.

Suppose you are building a page of public information, and visitors have to wait before its main content appears. You first plan a modest reduction in waiting time, so you ask AI to compress images and remove some scripts. Those changes might help, but they assume the page must follow the same loading sequence. Change the goal to “visitors should barely have to wait,” and an earlier set of questions becomes unavoidable. Which content must arrive first? What can arrive later? Which work can be finished in advance?

This is a hypothetical example, not a report of an optimization that worked. After a change, you would still need to test whether the page feels faster on real devices and networks for real visitors. My point is that the higher target changes where we search. It does not certify any proposed solution. If the model says “use caching” without explaining what content would be stored ahead of time and where that changes the path, its answer is upbeat but gives us no usable next move.

Moving furniture has a similar order of operations. If all we say is “push the bookcase through the door faster,” we will keep changing our grip and pushing harder. Ask first whether the bookcase can pass through intact, and we start measuring the doorway, the corner, and the bookcase. We may find removable parts. We may find that the boards themselves are too wide and the design has to change. Software offers more ways to rearrange the process than furniture does. The analogy helps explain why we should find the constraint before choosing an action; it cannot replace a software test.

A higher target also has an uncomfortable effect. It shows where we have mistaken familiarity for a boundary. Someone who is good at changing images, fonts, and features will naturally propose those tasks first. Once the target stops accommodating familiar methods, the question changes from “how would I do this?” to “what must happen for the visitor to get that result?” AI can expand the menu of possible methods. A person still has to judge whether the visitor benefits.

## What if AI says no?

Ask what blocks the way. “It cannot be done” is a conclusion, not a record of an inspection. It might mean that the cost is too high, the available information is inadequate, access to one step is missing, or the target combines conflicting requirements. Those causes call for different responses. Folding them into one no is like ordering a smaller bookcase before measuring the doorway.

I would ask AI to separate three things: the constraints it already knows, the constraints it suspects but has not checked, and the cheapest check that would distinguish the two. That turns “try harder” into an investigation someone can perform. If a check shows that a supposed constraint is absent, we can change routes. If it confirms the constraint, we can change the target, choose another route, or accept the cost. Each step leaves something another person can inspect.

This is also why I want several genuinely different approaches to the same goal, rather than repeated rewordings of one approach. For the page, one approach might reduce the data that must travel. Another might change the order in which content appears. A third might do some work ahead of time. We should compare which part of the causal chain each approach changes and which costs it creates. “Option A sounds more advanced” is not a comparison.

[Research by Gentner, Loewenstein, and Thompson](https://groups.psych.northwestern.edu/gentner/papers/GentnerLoewensteinThompson03.pdf) offers a limited but useful parallel. In one experiment on learning negotiation strategies, undergraduate students read the same two cases. Of those asked to compare the cases, 48% applied the principle to a new problem; among those studying the cases separately, 19% did. The study tested transfer of negotiation strategies, not AI website optimization. The action I borrow is narrower: put two routes side by side and make yourself explain their meaningful similarities and differences.

Comparison can also catch a familiar form of wasted effort: doubling down on one kind of fix after it keeps failing. If a page loads slowly, asking AI to compress the images a little more for the third time may produce a nicer explanation without touching the slowest step. If several approaches hit the same measured constraint, we have a reason to narrow the goal. If they hit different constraints, the choice has only just begun. The high target is there to reveal that distinction, not to justify an endless prompt thread.

## How do we know we're on course?

Return to the user's result. “Fast” might mean build speed to a developer, while to a visitor it means the moment the main content becomes readable. Neither person is necessarily wrong, but one measure cannot stand in for the other. Before testing, I would write down who needs the result, at what moment they need it, and what change they could observe. If I cannot answer those questions, AI should not start racing against an internal metric.

[Superhuman founder Rahul Vohra's account](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/) makes the difference concrete. His team did not declare that its email product was useful simply because its makers thought it was fast. They asked people who had recently used it how disappointed they would be if they could no longer use it. Vohra reported that 22% initially answered “very disappointed.” The team then narrowed its view to users better suited to the product and recalculated the share as 33%; that shift did not come from changing the product. The team used feedback from people who valued speed but still faced obstacles to guide product changes. Vohra said the share reached 58% after three quarters of work and continued surveys of new users, but did not report the number of responses behind that figure. These figures come from different stages and survey groups, so they are not a before-and-after measure of the same people or proof that product changes alone caused the increase. They are one company's self-reported survey results, not a threshold every product should adopt.

What I take from this case is the order of work, not the percentage. First hear what users actually value. Then check whether the obstacles they describe interfere with that central value. Only then choose features to change. “Make everyone love the product” is a grand goal with almost no practical direction. “Make people who need to process email quickly want to return after using it” identifies a person and an observable behavior. It still asks for a lot, but the meaning has begun to settle.

[In his essay on early startup work](https://paulgraham.com/ds.html), Paul Graham describes Stripe's founders helping willing users install the product on the spot. He also describes doing work manually for users first, so founders understand the process before automating it. These are startup cases and advice, not an experiment establishing a rule for every industry. Their value here is that some constraints hide inside actual use. AI, asked to “redesign everything” without contact with users, can list many options but cannot know which step makes a particular person give up.

That is why I would not hand the higher goal to the model alone. The model proposes alternative routes. Users tell us where they experience a loss. Measurement tells us whether a change happened. When those accounts conflict, return to the person and moment named in the goal. A polished technical report that leaves the visitor waiting is still just a polished technical report.

## Won't this waste time?

It will, without a stopping rule. Someone could fairly object that extreme demands invite AI to make solemn promises it cannot keep and drag people through repeated experiments. I agree. When limits on time, money, reliability, or safety are already clear, “I want everything” can pressure a team to hide the real cost elsewhere. That is not ambition. It is dishonest accounting.

The harder case is a high target that can be met in the short run by shifting a cost to someone else. The page shows its main content sooner, but later interactions become slower. A visitor waits a little less, but maintainers must take a complicated route for every future change. We should write those costs down before the test and inspect them in the same round. Otherwise, measuring only the most visible improvement lets us announce progress that has not really been delivered. The target can be high. The cost must remain visible.

I use two boundaries for exploration. The first covers conditions that must hold: user information cannot be exposed, and essential content cannot be lost, for example. I write those down first rather than trading them for speed. The second is a budget for investigation: by what time will we have completed which measurement, and when will we revise the goal or stop if no plausible route appears? A budget does not make the goal smaller. It prevents an ugly habit: treating the time already spent as a reason to ask AI for still more clever-sounding suggestions.

There is an opposite mistake too: using “be realistic” to end learning early. The [author abstract of a study by Brynjolfsson, Li, and Raymond](https://arxiv.org/abs/2304.11771) describes the use of an AI assistant in customer support, using data from 5,172 agents. Productivity, measured as issues resolved per hour, rose by 15% on average; less experienced workers saw larger gains, and the authors also reported evidence of learning. An author abstract is the researchers' own short account of their study. The supplied material contains that account but not the full methods needed here. It does not establish how many workplaces were involved, show that this way of setting a goal works, or show that the customer support result transfers to every job. It makes a narrower point relevant here: what people can do alongside a tool can change, so yesterday's familiar limit need not automatically become tomorrow's target.

“Do not lower the target yet” therefore makes sense only when the constraint is still unclear and the cost of exploring is manageable. When the evidence is clear, admitting a boundary is more useful than insisting. When information is missing, getting it is more useful than pushing the model. A high target should help us discover sooner when to change routes and sooner when to concede. Both discoveries count as progress.

## What can I try today?

Choose a small task you are already doing. Give it a result you genuinely care about but had hesitated to request. Do not write “make it better,” which cannot be checked. Name the user, the visible change, and the cost you will not pay. Begin with a place where feedback can arrive today, away from other people's private information and irreversible decisions. That keeps a long wait from passing for deep thought.

1. Write your original compromise target, then write the result the reader or user actually needs. Describe both with the same observable measure so that “a faster page” does not quietly become “less code.”
2. Ask AI for two routes that work by different principles. For each, have it name known constraints, suspected constraints, a way to test them, and any costs shifted elsewhere. Ask which step requires real evidence so it cannot fill the gap with imagination.
3. Run the cheapest reversible check first. Put the before measurement next to the result and check whether any nonnegotiable condition was damaged. If all you have is the model's own assessment, mark the round unverified.
4. Review the result at the time you chose. If you have ruled out a supposed constraint, try the new route. If you have confirmed it, adjust the target or accept the cost. If you still lack information, suspend the conclusion and get the missing evidence.

I would judge this small experiment by one thing: can you now explain what blocked the result and which step to change next? If you can, the attempt taught you something even if you missed the ambitious target. If you cannot, a bigger target has only made the wish louder.

## References

- [Learning and Transfer: A General Role for Analogical Encoding](https://groups.psych.northwestern.edu/gentner/papers/GentnerLoewensteinThompson03.pdf), Dedre Gentner, Jeffrey Loewenstein, and Leigh Thompson, 2003. Used for case comparison and learning transfer; the experiment concerned undergraduates learning negotiation strategies.
- [How Superhuman Built an Engine to Find Product Market Fit](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/), Rahul Vohra, 2018. Used for one company's user survey and product changes; figures are the founder's account.
- [Do Things that Don't Scale](https://paulgraham.com/ds.html), Paul Graham, 2013. Used for early manual contact with users and learning from their work; this is startup advice illustrated by cases.
- [Generative AI at Work](https://arxiv.org/abs/2304.11771), Erik Brynjolfsson, Danielle Li, and Lindsey Raymond, submitted 2023 and revised 2024. Used for reported productivity and learning evidence in a customer support sample; only the author abstract was checked in this source package.
