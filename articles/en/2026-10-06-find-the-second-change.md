# Find the Second Change

> 发布日期:2026-10-06 · [中文](../zh/2026-10-06-先找到第二处改动.md) | [English](../en/2026-10-06-find-the-second-change.md)

---

Imagine using AI to revise a learning plan. Instead of reading a chapter every day, you will make a small piece of work each week. The new plan is clear and exciting. But your reminders still tell you to read, a fellow learner still expects reading notes, and your monthly review still counts only pages finished. The edit is done. Your life is still running the old version.

An AI-generated clipped summary about hardware development raises a question: how can we tell what else must change when a requirement changes? The summary is a secondhand account of outside material, not verified engineering research or my own engineering experience. I want to bring that question back to ordinary work and learning: as AI makes the first change cheaper, can we find the second one?

Here is my view. Many tasks are held up less by our inability to change the thing in front of us than by our inability to see what that change affects. Asking AI for more versions may leave that problem intact. The more valuable ability is to trace the consequences of a change, put them in front of someone who can check them, and then decide what to do next.

## The first edit is easy. Where is the second one hiding?

Changing your address is a familiar example. You enter a new delivery address on a shopping site, see a confirmation, and feel finished. Yet a recurring order may still use the old address. Someone who sends you parcels may still have it too. The hard part is not typing the new address. Several pieces of information are connected, and changing one means checking the others.

I call such a connection a dependency: one thing works partly because another thing remains in a certain state. The weekly project, the reminders, and the review criteria in our learning plan have that relationship. If the project goal changes while reminders still demand pages, daily behavior gets pulled toward the old goal. If the review still counts only pages, you may even conclude that you are falling behind. Each piece looks fine in isolation; together, they start to contradict one another.

The address example helps us see a connection. It does not mean that every connection carries the same risk. A misdelivered parcel may be sent again. In a physical design, an interface is where two parts connect and must fit together. If they do not fit, the cost can be far greater. So the useful question is not whether we have listed every imaginable connection. It is which missed connection would produce a consequence we cannot accept.

This is also why a polished AI answer can make progress look bigger than it is. The answer usually concerns the document, page, or decision you asked about. The costly connection may live in somebody else's schedule, an old way of checking progress, or material the model never saw. The faster generation becomes, the more tiresome it can feel to confirm those connections. Yet without that check, speed merely lets the old and new versions coexist sooner.

Picture placing a sheet of paper with the new decision in the middle of a table. Every sheet around it contains an agreement the decision might affect. Which sheet needs an edit, which needs only a notification, and which can wait? That picture is more useful than aiming for an exhaustive process diagram, because it demands a concrete consequence for each connection. It has a clear limit too: real relationships change, and the papers cannot replace checking with the people involved.

I do not want everyone to become an expert in complicated systems diagrams. I want us to be slower to declare an edit finished. A reasonable completion test is this: the new decision is written down, the most important adjacent agreements have been checked, and the remaining unknowns can be named. Admitting what we do not know is fine. Mistaking the unseen for the nonexistent is the danger.

## Why saving time may leave the work intact

It is tempting to treat saved time as proof that AI has transformed work. It may indeed speed up a particular action. In a study involving **66 firms and 7,137 knowledge workers**, researchers randomly selected which workers got early access to AI built into office software during 2023–2024. The email time result used data from **6,441 workers** with recorded email sessions during the experiment and prior Outlook use. Researchers estimated that people who actually used the tool in the second half of the experiment spent about two fewer hours each week in Outlook email sessions. They did not detect an overall change in the quantity or composition of workers' tasks. The [original study](https://arxiv.org/html/2504.11436v4) is careful about this boundary.

That does not make the saved time worthless. Fewer email interruptions and a shorter workday are real benefits. The result simply makes me separate two kinds of change: one person handling an existing task faster, and a group agreeing to do its work differently. A tool can directly help with the first. The second requires someone to notice dependencies and other people to accept a new arrangement.

The study cannot settle the matter for every team. Its researchers mainly observed activity inside office software. They could not see email content or directly measure work quality, and their sample came from large firms taking part in an early trial. “No change detected” is not “no change occurred anywhere.” It certainly does not establish how every small team works. What it offers is a useful counterexample to our intuition: local efficiency may arrive while the wider routine stays on its old tracks.

Return to the learning plan. AI can quickly lay out a weekly production schedule and rewrite the reminders in a kinder voice. But if you still score yourself by pages read, the weekend brings an odd argument. You made something, so why does your record say you did almost nothing? The problem is not that AI cannot write well. Your goal, your actions, and your feedback have not changed together.

That is why I want to test a tool with a harder question than “How long did it save?” After one edit, who can point out the adjacent promise most likely to be missed? If the answer depends on one person suddenly remembering the whole situation, the work still depends on that person's memory. AI can search, compare, and propose possible connections. Someone still has to check each candidate and be able to say that a connection has expired.

This does not mean turning all of life and work into machine readable tables. Many connections begin as spoken agreements or a person's understanding of a situation. Making the links that fail most often, or hurt most when missed, explicit is more realistic than collecting every detail at once. Otherwise, documentation becomes another task that can never be finished.

## Find connections in what people do

A dependency can hide in the way we frame a question. Ask how to make a milkshake taste better, and you focus on flavor and ingredients. In an [interview](https://hbr.org/podcast/2020/01/revisiting-jobs-to-be-done-with-clayton-christensen), Clayton Christensen recalled that he and his colleagues first watched when people bought milkshakes and where they went afterward. Then they asked what those people were trying to accomplish in that situation. His account of morning commuters shifted attention from product attributes to the whole experience of buying and using the drink.

That case is the participant's retrospective account. It does not prove that the same line of questioning works for every business. Nor am I borrowing a tactic for selling milkshakes. I am borrowing the order in which to look for connections: first watch what a person is doing; then ask what else that person relies on to get it done. Editing only the most visible part of a product page may miss the waiting, carrying, or use that actually shapes a choice.

In [*Do Things that Don't Scale*](https://paulgraham.com/ds.html), Paul Graham describes founders personally recruiting early users and helping them with their first setup. His point is that close contact with those users yields feedback on the product. These are a practitioner's observations, not a controlled test across industries. Still, they bring out a simple fact: some connections appear only when you follow someone all the way through a task.

Putting the two accounts together gives me a more specific action than “talk to users.” Do not only ask what feature someone wants, or ask AI to guess how they will use it. Watch one journey from the moment a need arises to the moment the task is complete. When does the person stop, turn to another person or file, or give something up to keep going? Those turns are often where a first change meets a second one.

Of course, observing one person is not discovering a universal rule. Someone willing to talk to you may be more engaged than those who never appear. One smooth session may be luck. I would record the observation as a hypothesis to test, not as a settled account of customer demand. For example: “After the plan changes, the old reminder will pull people back toward pages read.” Then check whether that reminder exists and whether anyone still acts on it.

AI can be a diligent recorder here. It can list scattered agreements as candidates, mark conflicts between old and new language, and ask who needs to confirm them. It can also suggest a counterexample: what fact would show that this supposed connection is absent? But it cannot read real behavior out of a situation it was never shown. Candidate connections and verified connections need separate labels.

## One wrong line can test the whole map

Once we start drawing connections, another danger appears. The map may look complete while containing false links. Suppose AI says, “You now make something each week, so you should stop reading every day.” That leap goes too far. Reading may supply the material for the work. What needs to change may be the reminder and the way progress is checked, rather than reading itself. Careless “sync everything” thinking can remove something useful along with something outdated.

In a low stakes draft, I am willing to invent one plausible but false link and correct it myself. I might write, “The more pieces of work I make, the better I am learning,” then ask whether repeating the same shallow piece counts as progress. Or I might write, “Fewer reminders always improve focus,” then ask how focus can begin if I forget to start. The more believable the mistake, the more clearly I must state the boundary.

I am not offering a universal learning cure. A [2023 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC9902256/) asked undergraduates studying scientific material to write plausible conceptual errors deliberately and then correct them. The three experiments involved **120 participants** in all. In the latter two, which asked students to apply learned concepts in another field, writing and correcting their own errors outperformed producing correct paraphrases. It also outperformed a method that added spotting and correcting someone else's errors to correct paraphrasing. The authors specify the materials and tasks involved. The results do not show that deliberate errors make real engineering projects safer, and they give us no reason to make mistakes in a consequential live setting.

What I take from the study is a prompt about the act of learning. When we look only at correct answers, we can miss what distinction we have actually learned to make. Writing a tempting but wrong connection ourselves, then explaining why it is wrong, forces us to state when two things must change together and when they need not. This is an exercise on paper, not a reason to ship an error.

Research on AI adds a caution. A [small study](https://arxiv.org/html/2501.17247v1) had **24 participants** use AI to help shortlist items; one group also saw brief critiques of the AI's suggested criteria. Researchers observed moments of reflection in interviews and behavior, but did not find significant differences in several overall quantitative measures. They also discuss possible overreliance. A short challenge can open a line of thought. It does not automatically produce a better decision.

So “ask AI to find faults” must not become a new stamp of approval. It may find trivial faults and miss the serious one. People may also trust a system more because it appears to criticize itself. A stronger move is to say how you intend to verify a link before asking AI to look for omissions. If only a person involved, or the outcome of real use, can verify it, leave that check to the person or the real outcome.

## When should you check connections before moving?

The strongest objection is that if we trace the surrounding work for every tiny edit, we will move too slowly to begin anything. I think that objection is right. Many inexpensive experiments should be made first and corrected when reality responds. The early user feedback in Graham's account points in that direction too: seeing real use beats imagining every situation in a room.

I would not demand a complete map before every change. I would first ask two questions. If this goes wrong, can we easily undo it? If we miss a related change, who bears the consequence? With a private draft you can revise at any time, acting first usually makes sense. If someone else will arrange their time or spend money based on it, or if the error will enter a physical object or a decision that is hard to reverse, check the crucial connections first. The test is consequence and reversibility, not how sophisticated a task sounds.

You can try this with one small change today. The following checks are my proposed method, not a procedure tested by the studies above. Write a sentence stating the new decision, then name the action it directly changes. Find the one old agreement most likely to be affected: a reminder, a measure of progress, a delivery format, or somebody else's plan. Do not rush to make a long list. Ask whether that one agreement still holds, who can answer, and what evidence would settle it.

Then ask AI for one connection you may have missed and one connection that looks relevant but may not need to change. Explain for yourself why the two differ. Check against the original file, the actual process, or a person involved. If you changed the reminder but find that the review still rewards the old behavior, change the review too. If reading still feeds the new weekly work, do not cancel reading simply because the goal changed.

Finally, keep a short record: what changed, which connection was confirmed, and which remains unchecked. It need not be elegant. It only needs to make sense to you next time. When a similar edit comes along, you need not guess from scratch. If an old link no longer holds, you can also say what disproved it. That is what a learning system looks like to me: it keeps its judgments and lets reality revise them.

I would return to the imagined learning plan at the start. Finishing the change does not mean getting AI to describe “make something every week” more beautifully. It means taking out the reminder that still demands pages, the agreement that still expects reading notes, and the monthly scorecard that recognizes only pages. Think of one thing you changed recently. Which neighboring agreement is still running the old version? Find that second change before you decide to speed up again.

## References

- [Shifting Work Patterns with Generative AI](https://arxiv.org/html/2504.11436v4), Eleanor Wiske Dillon et al., body of supplied version dated 2026. Used to distinguish time saved on individual tasks from changes in work patterns; limited to observed early office software activity.
- [Revisiting “Jobs To Be Done” with Clayton Christensen](https://hbr.org/podcast/2020/01/revisiting-jobs-to-be-done-with-clayton-christensen), Harvard Business Review, 2020 replay of a 2016 interview. Used for finding connections beyond product attributes through purchase context; a retrospective account.
- [Do Things that Don't Scale](https://paulgraham.com/ds.html), Paul Graham, 2013. Used for how direct contact with early users exposes missed steps; practitioner observations.
- [Deliberate Erring Improves Far Transfer of Learning More Than Errorless Elaboration and Spotting and Correcting Others' Errors](https://pmc.ncbi.nlm.nih.gov/articles/PMC9902256/), Sarah Shi Hui Wong, 2023. Used for the result of generating and correcting one's own errors in low stakes learning tasks; no engineering safety guarantee.
- [“It makes you think”: Provocations Help Restore Critical Thinking to AI-Assisted Knowledge Work](https://arxiv.org/html/2501.17247v1), Ian Drosos et al., 2025. Used for the potential and limits of brief critiques beside AI suggestions in a small study.
