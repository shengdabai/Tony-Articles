# The Unfinished Work Is the Moat

> 发布日期:2026-09-06 · [中文](../zh/2026-09-06-真正让人回来的，是那件没做完的事.md) | [English](../en/2026-09-06-unfinished-work-is-the-moat.md)

---

Most AI products greet us with an empty box.

Type something. Receive something. Copy it. Leave.

This is a remarkably useful transaction, but it has a structural weakness: it ends at the moment it succeeds. Once the answer has been copied, the product has no necessary place in what happens next. A cheaper model, a better prompt, or a new interface can replace it tomorrow.

That is why I have started to think that the most important object in an AI product is not the prompt or even the output. It is the unfinished work.

An unfinished novel, a course still being learned, a piece of software still being shaped, or a business process still being improved gives tomorrow somewhere to begin. If an AI system can preserve the state of that work—not merely store a transcript—it can become more useful every time we return. It stops behaving like a vending machine and starts becoming a workshop.

The distinction matters for product builders. It matters even more for anyone trying to use AI to become stronger rather than merely faster.

## A vending machine is optimized for exit

A generator is built around a transaction: request in, result out. Its cleanest success case is also its goodbye.

A workshop is different. The central object is still on the bench when you leave. Around it are sketches, discarded attempts, measurements, tools adjusted to your hand, and small decisions that would be hard to reconstruct from scratch. You return not because the room demands attention, but because something you care about is still alive there.

Sudowrite offers a useful example of this design shift. According to its own account, it was founded in 2020 by two science-fiction writers who had run a writing group together. Instead of building a general text generator, they organized the product around fiction as an ongoing practice. Its Story Bible holds genre, style, synopsis, characters, worldbuilding, and outline, then supplies that context to later stages such as scenes and draft prose. The important design choice is not any single generation feature. It is that the unit of work is the evolving book, not the latest prompt. ([Sudowrite overview](https://sudowrite.com/blog/how-sudowrite-works/), [Story Bible documentation](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/what-is-story-bible/jmWepHcQdJetNrE991fjJC))

This case does not prove that workflow depth guarantees a successful product. Distribution, reliability, price, and output quality still matter. But it reveals a better question than “What can the model generate?”

What can the user continue?

## A transcript is not continuity

Most AI systems already save conversations. That looks like memory, but a chronological pile of messages is rarely the current state of a project.

Real continuity has at least three layers.

- **Artifact state:** What exists now? Which chapter, prototype, argument, or process is the latest usable version?
- **Decision state:** What has already been tried, rejected, or changed—and why?
- **Judgment state:** What does “good” mean here? Which trade-offs, constraints, and tastes should guide the next move?

Without the first layer, we restart the work. Without the second, we repeat old mistakes. Without the third, the AI may produce plausible material that slowly pulls the project away from what we meant to make.

This resembles an old idea from philosophy of mind. In the 1998 paper *The Extended Mind*, a notebook is used to argue that an external resource can participate in cognition when it is reliably available and habitually integrated into action. Whether or not we accept the strongest version of that thesis, the practical insight is powerful: a tool becomes part of how we think when we can depend on it to carry relevant state from one moment into the next. ([The Extended Mind](https://www.alice.id.tue.nl/references/clark-chalmers-1998.pdf))

An AI workbench can do more than remember facts. It can preserve the trail of judgment that produced the current work. For a learner, that means keeping predictions, mistakes, corrections, and open questions—not just summaries. For a writer, it means preserving the argument, the abandoned structures, and the reason a certain voice was chosen—not just paragraphs. For a small team, it means carrying forward constraints, decisions, tests, and consequences—not just meeting notes.

The system becomes more useful because the work has become more legible. At the same time, the person becomes more capable because their judgment is being made explicit. That is a real self-improving loop: the artifact teaches the system, and the revised system helps the person make a better artifact.

## Keep the large work unfinished, but finish small loops

There is an obvious objection. Unfinished work can become a swamp. Many people have folders full of drafts, half-built tools, and abandoned courses. Why would preserving more incompletion create value?

It does not—unless the system helps close small loops.

A well-known study of the “IKEA effect” found that people valued things they had built themselves more highly, but the effect depended on successful completion; failed or destroyed creations did not produce the same result. Effort alone was not enough. ([The IKEA Effect: When Labor Leads to Love](https://doi.org/10.1016/j.jcps.2011.08.002))

This gives us a useful design rule. The large work may remain unfinished for years, but each session should complete something real:

> return → recover the state → make a judgment → finish a small unit → record what changed

A chapter can remain inside an unfinished book. A tested feature can remain inside an unfinished product. A corrected misconception can remain inside an unfinished education. The point is not to keep people psychologically hooked by an open loop. The point is to lower the cost of resuming meaningful work while giving each return a visible ending.

For builders, this changes what deserves to be designed. A serious AI workbench needs more than prompt templates. It needs a durable project object, a clear current state, a record of decisions, editable criteria for quality, and a clean way to export the work. The best place to begin is often a task you perform frequently enough to notice its hidden friction. Repeated use supplies the feedback that imagination alone cannot.

The same test works for personal AI systems: after ten sessions, is the eleventh merely faster, or is it better informed?

## Compound the work; do not capture the user

There is also an ethical line here. When a product holds months of someone’s work, switching costs naturally rise. A company may call that a moat. But if the user stays only because their work is trapped, the moat is really a hostage situation.

Continuity should deepen usefulness without weakening ownership. The product should help users export not only final documents but also the structure that makes those documents intelligible. Sudowrite, for example, documents ways to export individual files, whole projects, and Story Bible sections. Portability does not destroy the value of continuity; it tests whether that value is genuine. ([Exporting Files](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/exporting-files/3NtVWXcnwYaRCmPW2iwcCB))

Persistent context has another danger: it can preserve bad assumptions as efficiently as good ones. A system that always remembers may become an echo chamber with excellent recall. So a mature workbench also needs revision, contradiction, expiration, and forgetting. Sources should be separable from interpretations. Old decisions should carry dates and reasons. Standards should be editable. The user must be able to say, “That was what I believed then; it is not what I believe now.”

This is where human judgment remains central. AI can reduce the cost of restarting, comparing, drafting, and testing. It cannot decide which unfinished work deserves another year of our life.

The strongest AI relationship is therefore not dependence. It is continuity with increasing agency.

When we leave a good AI system, the work should be clearer than when we entered, and we should be slightly more capable of judging it. When we return, we should not face an empty box. We should meet the latest version of the work—and the evidence of how we ourselves have changed.

The unfinished work is not a flaw in the workflow. It is the thread that lets a person, a tool, and an idea grow together across time. That thread, not another button labeled “Generate,” is the moat worth building.
