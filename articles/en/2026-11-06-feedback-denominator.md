# Who Counts in Your Feedback?

> 发布日期：2026-11-06 · [中文](../zh/2026-11-06-反馈的分母.md) | [English](../en/2026-11-06-feedback-denominator.md)

---

Ask AI to play a user and produce a long list of suggestions. Find an actual user and see whether they choose to use the product again. Both can help improve a product, but they belong in different accounts of demand.

Here is what concerns me: when AI can generate praise, complaints, and suggestions, how do we know we are responding to someone's need? My view is that AI can propose reasons worth investigating, but it cannot cast votes for users. Before feedback determines what we build, we need to know who actually encountered the problem and who has merely produced a convincing description.

More suggestions do not necessarily mean more understanding. People who care about their work may be especially vulnerable to this confusion. Give us a suggestion, and we immediately want to make an improvement.

## Isn't more praise a good thing?

First, check who gave it.

A clipping about automated replies in comment sections raises a question about where comments come from. Consider what happens after a reply arrives: a creator uses comments to choose subjects; a developer uses suggestions to plan features. Treat generated responses as reactions from actual users, and the work that follows can head in the wrong direction.

An occasional polite response from a machine is not my main concern. The more troubling possibility is that we use a machine to generate suggestions, take those suggestions as proof of demand, and then ask the machine to implement the changes. Every stage produces something. What remains unconfirmed is whether anyone needs it.

One detail matters here in [Superhuman founder Rahul Vohra's account of his product](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/). Writing in 2018, he explained that the team surveyed users who had experienced the product's core functionality and used it at least twice in the previous two weeks. This is a founder's account of a method and company-reported results, rather than an experiment establishing that the method works everywhere.

The team wanted to know how disappointed those people would be if they could no longer use the product. Before asking about disappointment, though, there was a condition: they had used it.

This is what I mean by the denominator of feedback: who is included, and why those people are being asked. Ask someone who is searching through email whether attachments are easy to find, or ask a model to impersonate a busy professional. Both produce text, but the text rests on different foundations. One draws on an actual experience; the other offers a possible explanation.

We can discuss both kinds of input together. We cannot add them together and declare widespread user demand. Generating ten different user voices does not bring ten additional users into existence.

Repeated comments from one person do not amount to many independent users, either. Conversely, a real user's experience does not become invalid because they used AI to organize their wording. What matters is whether we can trace the account back to what that person did, and distinguish it from anything the model added. Tracing where feedback came from matters more than guessing whether the prose sounds machine-written.

## Does feedback from a person settle it?

We still need to know what it answers.

Feedback from real people can answer the wrong question, too. Someone may find a product entertaining, hesitate to disappoint its maker, or accurately describe a feeling that remains some distance from the outcome we want to understand. These are possibilities to consider when collecting feedback, not conclusions we should draw about someone from a compliment.

[A mathematics learning experiment by Bastani and colleagues](https://hamsabastani.github.io/education_llm.pdf) offers a concrete reminder. Conducted at one high school in Turkey, its main analysis covered 839 students and compared a standard chat-style AI, a hint-oriented AI, and no AI. The hint-oriented version also received teacher-prepared solutions and guidance on common mistakes, so the difference cannot be attributed entirely to withholding answers. The study measured short-term outcomes on particular mathematics review tasks, rather than adults' long-term learning.

The standard chat-style AI improved practice performance. Once the tool was removed, however, that group's exam scores were about 17% lower relative to the control group, which had no AI. Students' self-reports did not correspondingly indicate that they had learned less. The hint-oriented version largely avoided this loss, but did not show a statistically significant improvement on the unaided exam. Here, "statistically significant" means the study's test can distinguish an observed score difference from random variation. The evidence did not establish an improvement; it also did not prove that the two groups had exactly the same outcome.

The reminder seems straightforward to me: asking how an experience felt and checking what someone could do afterward are separate questions. A smooth conversation and an easier task may be product benefits. A product promising learning still owes us a check of the learning outcome.

Likewise, calling an email tool useful does not tell us whether it reduced missed replies to important messages. Praising a design and choosing to move everyday work into it are different things. We have to identify the outcome we want to improve before choosing feedback that can answer that question.

There is another detail in the Superhuman account that is easy to read past. In his closing recap, Vohra puts the initial share of users who would be very disappointed at 22%, rising to 33% after narrowing the user segment. That portion of the change came from adjusting whom the team observed; it cannot all be credited to improving the product. Narrowing the segment can identify people the team is better placed to serve. It does not suddenly create a need among the original users who cared less.

Choosing a narrower audience may be the right decision. But when reporting progress, we should distinguish a change in the people measured from a change in the product. Otherwise, a product that appears increasingly popular may simply be hearing less from people who dislike it.

This also changes whom we should ask next. Listening only to people who stayed can tell us why they stayed, but tells us much less about where those who left ran into trouble. I would record these separately: serving existing users requires attention to their reasons for staying; reaching new users also requires hearing from people who left or never started. Both purposes are legitimate. Neither can stand in for the other.

## Can AI's suggestions still help?

Yes. Use them to find checkable problems.

Suppose we are building a tool to help organize email replies. AI points out that an exported file will not open: we can generate the file and try opening it. It says a reply has missed a request in the original email: we can compare the two, item by item. The value of these suggestions depends on whether the problem can be reproduced. We do not first need to establish that a human raised it.

But when AI says busy people will certainly pay for the tool, the claim has changed. Inspecting a file can produce evidence about whether that file works. Asking a model to explain a willingness to buy, however many times, still reveals no person's actual choice. Keeping that judgment as an open question gives us a useful next step.

Work made with AI can certainly be good. In their [2023 working paper, Noy and Zhang](https://economics.mit.edu/sites/default/files/inline-files/Noy_Zhang_1_0.pdf) studied 444 college-educated professionals, randomly giving some access to ChatGPT and having professionals in the same occupations evaluate short writing assignments without knowing the experimental assignment. They found faster completion and higher quality. This early working paper measured short-term output on relatively self-contained tasks, rather than market demand for a particular product.

That helps me separate two things. Machines can contribute to making the work, while evaluation must still address the claimed outcome. A clear email reply and someone's willingness to keep using a reply tool each require their own evidence. Establishing the first does not automatically establish the second.

When buying clothes, we already understand this distinction. A mirror shows how a garment looks. Trying it on tells us how it fits. Taking it home also depends on the price, the clothes we already own, and where we would wear it. A clearer mirror cannot create a purchase record at the checkout.

Software sometimes needs sustained use before its value becomes apparent, so we cannot copy the speed of trying on clothes. But different actions still answer different questions. AI-generated suggestions can be a useful mirror for examining problems. Counting the people reflected in a mirror as customers is a counting error.

I am happy to have AI propose situations I may have overlooked or identify a counterexample. Until someone actually experiences, chooses, or rejects something, though, these remain possible explanations. However plausible the explanation, we still need the corresponding person and behavior.

Conversely, if AI analyzes a record of real use and identifies where users repeatedly fail to open attachments, we should not discard the analysis simply because a machine handled it. We should check whether the original record supports the conclusion and whether contrary cases were omitted. A machine can help observe what happened, or simulate what has not happened. Both can become reports. Their evidential foundations cannot be exchanged.

## What if nobody gives feedback?

Start with one instance of real use.

A small team might reasonably object: where are we supposed to find all these people? The product is unfinished, recruiting users is difficult, and simulation seems better than guessing in isolation. I accept that argument. Particularly early in development, simulation can help check whether a process makes sense and expose obvious omissions.

What I do not want is to count money saved on interviews as demand evidence already obtained. When there is nobody to ask, allowing ourselves not to know yet is more useful than filling the gap with generated praise. If we know we do not know, we will keep looking for someone. If we mistakenly believe we know, we may spend the remaining time adding features.

In [his 2013 essay, Paul Graham](https://paulgraham.com/ds.html) described how Stripe's founders would help people install the product on the spot once they agreed to try it. These are observations and experiences from early companies, rather than proof that every business should follow suit. For the question at hand, the account at least suggests a feasible direction: real contact can begin with one person and one attempt. It need not start with a large survey.

What interests me about this approach is that it puts feedback where action happens. Where someone gets stuck, which information they never look at, and where they need help bring us closer to actual product use than guesses about what users might like. We should also record the assistance we provide. Success with someone helping throughout does not establish that independent use is already straightforward.

For our email tool, we could invite one willing person to complete a task with material they voluntarily provide and can share. Watch whether they struggle to find the right place to start, or still need to move the result back into their original tool. If they keep using it afterward, ask why. If they do not, retain that observation, too.

One observation does not represent everyone. Its value is to provide a more precise starting point for the next observation, not to authorize an early declaration of market acceptance. With few users, we can make a smaller claim. We do not need to inflate the sample.

Not continuing does not necessarily mean there is no need. The person may have no email to deal with at the moment, may have forgotten, or may find switching too troublesome. Silence gives us a reason to investigate; it does not name its own cause. I would rather retain an unexplained gap than let AI fill it with an assumption about price or missing features and send us into another round of work.

## What can I try today?

Examine the most recent feedback.

Here is a small practice I intend to try. Before deciding on the next change, I want to take a recent suggestion and reconstruct how it became a decision. I have not verified that this method works. I want to begin by checking whether I have mistaken a conjecture for support.

1. Find one suggestion and record its origin. An actual user, someone who has never used the product, a team member, or AI: write down which it was. Also record what part of the experience the source encountered, rather than grouping every comment under user feedback.
2. State exactly what the suggestion supports. Does it identify a reproducible error, describe a feeling, or predict a future purchase? Check the error, retain the feeling, and leave the purchase prediction for subsequent behavior to test.
3. Arrange an action that could change the decision. For the email tool, we could observe someone completing a reply and agree on when to check whether they continued using it. Write down in advance what result would make us cancel the proposed change.
4. Return at the agreed time and include nonresponses, attempts never started, and use not continued. Keep AI's predictions separate from what actually happened. Examine the differences without letting later explanations overwrite the original judgment.

The record need not be elaborate. It should show what evidence is missing between a suggestion and an action. If a feature looks popular only because several generated suggestions praise it, this can reveal the gap now. If AI has identified a reproducible problem, we can address it immediately.

Then ask what the new evidence would make us give up. We may have planned to add a set of reply styles, only to observe that the person cannot find the draft they saved last time. Adding more styles would then lack support from the immediate observation. AI can still help propose solutions, but the observed problem should constrain what we address next. That is precisely the constraint I want.

I also want to leave room for patience. Real feedback can be brief, or amount to a single exit; generated feedback can be orderly, detailed, and emotionally convincing. A more polished response does not imply a more real need behind it. The same applies to improving ourselves: an appealing explanation is no reason to count a change that has not happened as an achievement.

Before acting on the next suggestion, here is what I want to understand: behind the last piece of feedback that made you substantially revise your work, how many people had actually used it, and how many came back after the change?

## References

- [How Superhuman Built an Engine to Find Product Market Fit](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/), Rahul Vohra, November 12, 2018. Used to check survey eligibility, segmentation, and the different populations behind the 22% and 33% figures. This is a company-reported case, not evidence attributing commercial success to the method.
- [Generative AI Without Guardrails Can Harm Learning: Evidence from High School Mathematics](https://hamsabastani.github.io/education_llm.pdf), Hamsa Bastani, Osbert Bastani, Alp Sungu, Haosen Ge, Özge Kabakcı, and Rei Mariman. The supplied manuscript does not state a publication date; the experiment took place in the fall semester of the 2023–2024 academic year. Used to distinguish practice performance, reported feelings, and unaided exam outcomes. Verification covers only the main text and appendix excerpts visible in the supplied packet; conclusions concern short-term mathematics learning at that school.
- [Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence](https://economics.mit.edu/sites/default/files/inline-files/Noy_Zhang_1_0.pdf), Shakked Noy and Whitney Zhang, working paper dated March 10, 2023; the title page states that it was not peer reviewed. Used for random assignment, blinded evaluation, and output improvements on specified writing tasks, rather than long-term skills or product demand.
- [Do Things that Don't Scale](https://paulgraham.com/ds.html), Paul Graham, July 2013. Used for the public account of Stripe's founders manually helping users install the product, and for learning about use through direct contact. This is an experience-based essay.
