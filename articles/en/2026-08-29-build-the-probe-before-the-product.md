# Build the Probe Before the Product

> 发布日期:2026-08-29 · [中文](../zh/2026-08-29-先造探针再谈产品.md) | [English](../en/2026-08-29-build-the-probe-before-the-product.md)

---

The most dangerous word in the AI era may be "product."

Not because products are unimportant. They are the only way a private idea becomes useful to someone else. But the word product is heavy. The moment we call something a product, we start imagining polish, launch plans, pricing, onboarding, screenshots, user acquisition, retention, app stores, documentation, support, security, analytics, and a name good enough to survive public judgment.

That imagination is not wrong. It is simply too early.

Before a product, there should often be a probe.

A probe is not a worse product. It is a different object. A product exists to serve a user repeatedly. A probe exists to answer a question. A product should be maintained. A probe may be thrown away. A product asks, "Can this create value at scale?" A probe asks, "Is the world shaped the way I think it is?"

That distinction matters much more now, because AI has made the probe dramatically cheaper.

For most of software history, even a small experiment had a real cost. You had to set up a project, choose a stack, write boilerplate, search documentation, debug errors, and decide whether the uncertainty was worth a day, a week, or a month. Because experiments were expensive, people substituted meetings, speculation, decks, and confidence. We sat around trying to reason about the world instead of pushing a small instrument into it.

AI changes that ratio. A concrete question can now become a tiny working thing in hours or days. Not a complete business. Not a robust platform. Not something you should immediately sell. But enough to make reality answer.

This is why the old software engineering idea of a "spike" feels newly important. In Extreme Programming, when a team could not estimate a story because some technical or design uncertainty was blocking it, the team could run a short, focused investigation. The point was not to ship the spike. The point was to learn enough to decide what the real work should be. The old C2 wiki puts it very plainly: spikes are useful when you are limited by knowledge, not merely by time.

That sentence describes a large part of modern life.

Most people are not only time-limited. They are knowledge-limited. They do not know whether the idea is technically possible. They do not know whether the data exists. They do not know whether the user can tolerate the interaction. They do not know whether the model fails gracefully or stupidly. They do not know whether a boring workflow can actually be automated end to end. They do not know whether the thing that sounds elegant in a note will survive contact with a real screen, a real file, a real camera, a real customer, or a real afternoon.

The AI-native response should not be to ask the model for a longer plan. It should be to build a sharper probe.

I felt this recently while working on a small visual-recognition helper for a very concrete physical puzzle. The interesting part was not that AI wrote code. That is already becoming ordinary. The interesting part was that the problem could be broken into questions that reality could answer.

Can a camera capture enough information without making the user perform an awkward ritual? Can an existing model family recognize the relevant pieces? If the model is not perfect, can the interface show uncertainty and let the human correct the remaining errors? Can the output be useful before the whole thing becomes beautiful? Can a desktop version prove the interaction before anyone thinks about phones, stores, accounts, sync, billing, and support?

Those are probe questions.

A few years ago, I might have tried to answer them by reading more, searching more, or arguing with myself. Now the healthier move is often to build a disposable version. Make a small dataset. Wire together the rough pipeline. Force the tool to look at messy inputs. Watch where it breaks. Write down what was learned. Then decide whether the next step is product work, another probe, or a clean stop.

This is also where many people fool themselves.

When AI helps you produce a working demo quickly, it is tempting to conclude that the hard part is over. Usually it is not. The demo answered one class of uncertainty. It did not answer distribution, maintenance, edge cases, trust, cost, performance, onboarding, support, or whether anyone besides you cares enough to return next week. The last mile of a product is not decoration. It is where many invisible debts become visible.

This is why "AI can code" is too small a conclusion. A more useful conclusion is: AI lets us move uncertainty earlier.

That is a very different promise.

If we use AI merely to generate more finished-looking artifacts, we may become lazier with judgment. We will ship slides that look like strategy, prototypes that look like businesses, and apps that look like products. We will confuse appearance with evidence.

But if we use AI to build probes, we become harder to fool. We can test more assumptions. We can expose weak language. We can turn "I think" into "I tried." We can discover which parts of a problem are easy only because they were abstract, and which parts become hard the moment they touch the world.

This is one reason old fundamentals have not disappeared. In a public AI Engineer talk, Matt Pocock argued that software fundamentals matter more, not less, in AI coding. The point is not nostalgia for hand-written code. The point is that AI increases output speed, and faster output punishes weak feedback loops. If the system has no shared language, no tests, no clear interfaces, no small steps, and no one responsible for design judgment, AI does not remove the mess. It multiplies it.

The same is true beyond software.

If you are a creator, a probe might be a single essay angle sent to a small group before you write the book. If you are a teacher, it might be one exercise that reveals whether learners can actually use a concept. If you are a small business owner, it might be one automated workflow for a repeated document task before you buy a full platform. If you are learning a new skill, it might be a real output that makes your ignorance visible in public enough to correct it.

The structure is simple:

First, name the uncertainty that can kill the idea. Not the uncertainty that is fun to discuss. The one that matters. "Can users understand this?" "Can the model handle messy files?" "Can this be done without private data?" "Will I still care about this after the first dopamine hit?" "Is the manual correction step acceptable?" "Does this save judgment, or only shift work into cleanup?"

Second, build the smallest instrument that can answer that uncertainty. The probe should be narrow enough to finish quickly, but real enough to encounter friction. A mockup can answer taste questions. A script can answer data questions. A recorded walkthrough can answer communication questions. A working but ugly prototype can answer interaction questions.

Third, decide in advance what result would change your mind. This is the part people skip. They build a prototype, fall in love with it, and then reinterpret every failure as "just a detail." A good probe has exit criteria. If the model fails on normal inputs, stop or change approach. If users cannot understand the first action, revise the concept. If the cost curve explodes, reduce scope. If the result is useful even while ugly, continue.

Fourth, do not promote the probe too quickly. Some throwaway code should be thrown away. Some rough workflows should be rebuilt once the shape is known. Some clever demos should remain demos because they answered the question and nothing more. The discipline is not only to build quickly. The discipline is to avoid turning every successful experiment into a permanent obligation.

This is where learning becomes production, and production becomes learning. Not in the slogan sense. In the mechanical sense. You produce something small enough to finish. The world reacts. That reaction becomes the input to your next move. Over time, the loop improves both the maker and the system.

Royal Road is a useful public reminder from a different domain. Its community history records that it began around a very specific reader need: fan translation around a Korean web novel, before evolving into a broader fiction platform. Whether you are building software, writing, teaching, or designing a small tool, the lesson is not "copy Royal Road." The lesson is that durable things often begin as narrow answers to real demand. Platform language comes later.

AI makes this pattern available to more people. That is the exciting part. The less exciting, more important part is that availability does not remove responsibility. In fact, it raises the standard. If it costs less to test, then testing less becomes harder to excuse.

The people who become stronger with AI will not be the people who ask it to remove all difficulty. They will be the people who use it to increase contact with reality. More probes. Faster feedback. Better questions. Cleaner stops. Fewer fantasies protected by a lack of evidence.

So before you build the product, build the probe.

Not because ambition is bad. Because ambition deserves evidence.

The probe is a promise to yourself: I will not worship my idea merely because it is mine. I will give the world a chance to answer. I will learn from the answer before I add polish, scale, and story. I will not let AI make me lazy by making things look complete too early.

A product is how you serve the world.

A probe is how you let the world teach you what is worth serving.

## References

- [Agile Alliance: Extreme Programming and spikes](https://agilealliance.org/glossary/xp/)
- [C2 Wiki: Spike Solution](https://c2.com/xp/SpikeSolution.html)
- [AI Engineer: Software Fundamentals Matter More Than Ever](https://ai.engineer/talks/software-fundamentals-for-ai-coding)
- [Royal Road forum: site history discussion](https://www.royalroad.com/forums/thread/35187?page=1)
