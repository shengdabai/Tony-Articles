# Before You Ask AI to Change Anything, Write Down What Must Not Change

> 发布日期:2026-09-09 · [中文](../zh/2026-09-09-让 AI 动手前，先写下什么不能改.md) | [English](../en/2026-09-09-write-what-must-not-change.md)

---

This morning, I was sorting through two notes about a new image model. One detail made me stop.

The model was not merely better at generating an image. It was better at changing only the thing a person asked it to change, while leaving the rest alone.

That sounds modest until you have tried editing an image with AI.

You ask it to change a jacket, and the face quietly changes too. You remove an object from a room, and the light moves. You fix one line on a poster, and the type, spacing, or brand treatment drifts with it. The requested edit may be correct, yet the image as a whole becomes less yours.

OpenAI describes this preservation ability as one of the central improvements in [ChatGPT Images 2.5](https://openai.com/index/introducing-chatgpt-images-2-5/): focused edits can keep the surrounding subject, composition, and treatment more stable, even across several rounds. Its own creation guide now tells users to specify both [what should change and what should stay the same](https://openai.com/academy/image-generation/).

Most of the attention will naturally go to what the model can now change. I found myself thinking about the other half of the sentence.

What can it leave untouched?

The more I thought about it, the more this felt like a general rule for working with AI—and perhaps for changing ourselves.

The ability to change something is power. The ability to preserve what matters while changing it is maturity.

## Every edit has a hidden second request

When we ask for a change, we usually state only the visible half of the job.

“Make this article shorter.”

“Add a login flow.”

“Automate my weekly planning.”

Each sentence contains a second, mostly unspoken request.

Make the article shorter, but do not flatten the uncertainty that makes the argument honest. Add login, but do not expose private data or break the path that already works. Automate the week, but do not fill every quiet hour with another task.

The first half names the delta. The second half names the invariants.

Humans often recover the second half from context. A good editor knows that tightening a paragraph does not grant permission to replace the author’s position. A careful colleague knows that improving a process does not mean silently changing who makes the final decision.

AI has no reliable way to recover every hidden invariant. It sees instructions and available context, not the full history of why something became important to us. When we omit the preservation brief, we are not giving it freedom so much as making it guess.

And as AI gets faster, the cost of that guess rises.

One careless edit used to affect one paragraph or one file. An automated agent can repeat the same misunderstanding across a hundred pages, a customer workflow, or a month of scheduled work before a person notices. Cheap change creates a new scarcity: confident preservation.

## Progress is not maximum change

Software engineers already have a name for one version of this problem: regression.

The [NIST definition of regression testing](https://www.nist.gov/glossary-term/30681) is wonderfully plain. After a change or new feature, you check that behavior which worked before has not been unacceptably altered or stopped.

In other words, a feature is not complete merely because the new thing works. The old promises still have to hold.

Living systems offer a different, useful lens. In physiology, allostasis is often described as achieving stability through change. The body does not preserve a frozen state. It adjusts breathing, circulation, temperature regulation, and many other processes so that essential functions remain viable as conditions move. A review in the biomedical literature explains allostasis as [changing defended levels when adaptation requires it](https://pmc.ncbi.nlm.nih.gov/articles/PMC4166604/).

Software and bodies are not the same thing. But they reveal the same shape: useful change needs a reference point. Without something to defend, “improvement” has no direction.

This matters in personal growth too.

Suppose I use AI to write faster. If output rises but I can no longer explain the central judgment in my own article, I have improved throughput while weakening authorship.

Suppose I use AI to build software beyond my current technical ability. That can be genuine leverage. But if I cannot trace what happens to a user’s data, recognize a failure, or return to a working version, I have gained capability and lost control at the same time.

Suppose I ask AI to optimize my day. It may remove empty spaces because empty space looks inefficient on a calendar. Yet those gaps may be where I read slowly, notice a weak signal, or change my mind. A schedule can become more optimized and less intelligent.

Not everything that survives a change deserves to survive. Old habits, weak assumptions, and obsolete rules can hide behind the language of “core values.” Preservation can become fear wearing a respectable coat.

So the answer is not to create a sacred list that never moves. It is to choose a small set of invariants for this particular change, then review them when the evidence changes.

An invariant is not “never change this.” It is “do not change this accidentally.”

## Give every AI task three fields

I now think many AI instructions need three fields, not one:

- **Change:** What should be different when the work is done?
- **Preserve:** What must not drift as a side effect?
- **Prove:** What evidence will show that both happened?

The third field matters. “Preserve my voice” is too vague to inspect. “Keep the first-person scene, the stated uncertainty, the three source links, and the final judgment” can be checked.

If I ask AI to revise an essay, the brief might look like this:

**Change:** Cut the opening by about a third and make the conflict visible sooner.

**Preserve:** The first-person observation, every verified number and date, the distinction between fact and inference, and the conclusion I actually believe.

**Prove:** Compare the claims and sources before and after; read both openings aloud; flag any sentence whose confidence became stronger.

For a small software change:

**Change:** Add a way for a returning user to resume an interrupted task.

**Preserve:** Existing saved data, current permissions, visible error states, and a path back to the previous working version.

**Prove:** Resume one successful task, trigger one failure deliberately, verify access as the wrong user, and perform one rollback.

For learning:

**Change:** Use AI to help me complete something I cannot yet build alone.

**Preserve:** My ability to explain the main causal chain, notice when the result is wrong, and reproduce one important step without assistance.

**Prove:** Before accepting the result, explain it in plain language, predict one failure mode, then test that prediction.

This takes a few extra minutes. That is precisely why it works. It moves the difficult thinking to the beginning, before cheap generation produces a large surface area of plausible mistakes.

## The protected core should be small

There is one more trap here.

If the preserve list becomes too long, nothing meaningful can change. A team can call every old behavior “compatibility.” A writer can call every favorite sentence “voice.” A person can call every comfortable routine “identity.”

The protected core has to be small enough to protect.

For each item, I find three questions useful:

- If this changes, what real value is lost?
- Who would notice the loss, and how?
- What evidence would make me willing to revise this invariant later?

If I cannot answer the first two, I may be defending familiarity rather than value. If I cannot answer the third, I may have turned a working assumption into a belief that evidence cannot reach.

This is why the preserve list belongs beside the task, not in a permanent monument. Different changes threaten different things. Editing a photograph may need to preserve identity and composition. Editing a business process may need to preserve consent and accountability. Editing a life may need to preserve relationships, attention, or the reason the work mattered in the first place.

AI is making the editable surface of the world much larger. Images, code, documents, schedules, and decisions can all be revised at a speed that used to be impossible.

That is real progress. It also changes our job.

We used to spend most of our effort making change possible. Increasingly, our harder work will be deciding which changes count as improvement—and naming what must survive them.

Before your next AI task, try adding one line: “While doing this, do not accidentally change…”

The quality of that sentence may tell you more about your judgment than the prompt that comes before it.
