# What Survives When the Surface Is Gone

> 发布日期:2026-09-04 · [中文](../zh/2026-09-04-当表面被拿走什么还能留下.md) | [English](../en/2026-09-04-what-survives-when-the-surface-is-gone.md)

---

I recently came across an AI video workflow that begins by doing something counterintuitive: it throws information away.

Instead of giving a model the original video—with its faces, clothing, colors, lighting, and texture—you first reduce the footage to depth. A depth image is not a normal picture. Each pixel is associated with a measurement of the scene's distance from the camera, as [Google's technical explanation](https://developers.google.com/ar/develop/depth) puts it. What remains is shape, spatial relation, and movement. Much of the appearance is gone.

Then the same movement can be rebuilt with a different visual world around it.

This is more than a clever video technique. It reveals a principle of learning that matters far beyond images:

**What makes an experience reusable is usually not its surface, but the structure that survives when the surface changes.**

## Control Often Begins With Subtraction

We tend to assume that more information gives us more control. That is sometimes true. If a model lacks a necessary fact, adding it helps. But a rich reference also bundles together many decisions that we may not want to keep.

A video contains motion, identity, camera position, light, material, background, and mood. An essay contains an argument, examples, rhythm, vocabulary, tone, and cultural references. A successful project contains a method, but also the market timing, team, reputation, and luck surrounding it.

When we hand the whole thing to an AI—or to a learner—we silently ask it to answer a hard question: which parts are essential, and which parts are merely attached?

If that distinction is not made, imitation becomes sticky. The new result carries over the source's clothes along with its bones. We think we have transferred a method, but we have only reproduced an example.

It helps to separate two layers.

The **skeleton** is what must remain stable: sequence, dependency, proportion, decision rule, acceptance condition. The **skin** is what may change: voice, color, tool, setting, metaphor, interface, or medium.

This does not mean the skeleton is always more important than the skin. In art, trust, and human relationships, the surface may carry part of the meaning. The point is narrower: if we want to reuse something, we must decide what kind of sameness we are trying to preserve.

## Expertise Is a Different Way of Seeing

A classic 1981 study asked experts and novices to sort physics problems. The groups did not merely know different amounts. They represented the problems differently. Experts tended to organize them by underlying physics principles, while novices relied more on literal features in the problem statement, according to the paper's [published abstract](https://doi.org/10.1207/s15516709cog0502_2).

A novice sees an inclined plane. An expert is more likely to see a conservation law or a force relationship.

The study was about physics problems, so it should not be inflated into a universal law of expertise. Still, it gives us a useful question: when I study a good result, am I noticing what it looks like, or what makes it work?

Human beings have been building tools for this separation for a long time. Formal dance notation, for example, records choreography as a score so that movement can be preserved and staged again; that is the mission described by the [Dance Notation Bureau](https://www.dancenotation.org/). The score is not the dance. It does not preserve the exact breath, body, stage, or emotion of one performance. Its power comes from deliberate loss. It keeps enough structure for another body, in another place and time, to reconstruct the work.

A map works for the same reason. So does a musical score, a recipe, a software interface, and a mathematical formula. None is a smaller copy of reality. Each is a bet about what can be removed without destroying what matters.

Perhaps learning is not mainly the accumulation of more examples. Perhaps it is the gradual improvement of that bet.

## AI Turns Representation Into a Practical Skill

Before generative AI, separating structure from appearance was useful but slow. You could study several essays, products, or lessons, yet producing enough variations to test your understanding took real time.

Now variations are cheap. That changes what practice can look like.

Suppose I admire an article. I can copy its subject, phrases, and metaphors and produce a pale imitation. Or I can extract a deeper sequence: begin with a familiar observation, expose a hidden contradiction, connect it to evidence, test the strongest objection, and end with a practice the reader can try. Then I can rebuild that sequence around a completely different subject.

If the second article still works, I may have understood something transferable. If it collapses as soon as the original story disappears, I probably extracted decoration rather than structure.

The same distinction appears in many kinds of work:

- In teaching, the skeleton might be diagnosis, example, guided attempt, feedback, and independent attempt. The slides and software are skin.
- In product design, the skeleton might be the change in the user's state and the evidence that the change occurred. The current interface is skin.
- In a personal workflow, the skeleton might be trigger, decision, action, verification, and review. The specific app is skin.

AI can help propose these decompositions, but it cannot relieve us of choosing them. That choice contains the real judgment. A model can generate ten candidate structures in seconds; only contact with reality tells us which structure preserves the cause and which merely sounds tidy.

So the useful instruction is not “give the AI less context.” Sometimes it needs much more. The better rule is: **do not mix invariants and variables into one undifferentiated pile.** Tell the system what must survive, what may change, and how you will judge the difference.

## Every Abstraction Deletes Something

There is a danger in falling in love with clean skeletons.

A depth map loses color and texture, but it can also lose uncertain edges, hidden surfaces, and material cues. A recipe cannot store the cook's senses. A management framework may preserve a process while deleting the power relationships that made it possible. A story stripped to “three-act structure” may keep its outline and lose its life.

Subtraction is not automatically insight. Sometimes it is amputation.

That is why a reusable structure needs at least three tests.

First, the **reconstruction test**: can someone use the representation to make a working instance, rather than merely explain the original?

Second, the **variation test**: can the structure survive a meaningful change of topic, medium, audience, or tool?

Third, the **failure-boundary test**: do we know where the abstraction stops working, and which removed detail becomes necessary again?

These tests prevent a framework from becoming a slogan. A good abstraction does not claim to contain everything. It makes its omissions visible.

This also answers a common objection. If context matters so much, why remove anything? Because transfer is impossible without compression. We cannot carry the whole original situation into the next one. The responsible move is not to avoid loss; it is to make the loss explicit, test it, and restore context when the boundary is crossed.

## Build a Library of Structures, Not a Warehouse of Examples

Most personal knowledge systems are warehouses. We save links, screenshots, prompts, and impressive outputs. The collection grows, but our ability does not necessarily grow with it.

A self-evolving system needs a different unit of storage. For every valuable example, keep four things:

1. **Invariant:** What must remain true for the method to work?
2. **Variable:** What can change without breaking it?
3. **Evidence:** What result showed that the structure actually worked?
4. **Boundary:** Under what conditions did it fail?

Then use the next project to challenge the structure. If it survives, it becomes more trustworthy. If it fails, update the boundary or split one vague method into two more precise ones. The output of one attempt becomes the input to the next.

That is a more demanding use of AI than asking it to make another version. It asks us to become editors of representations: to decide what deserves to persist across versions, and what should be allowed to disappear.

In an age when copying a surface takes seconds, surface resemblance is no longer strong evidence of understanding. The scarce ability is to see which relationships must not move when everything else does.

Remove the face, the color, the familiar story, and the original tool. What is left that can still produce a result?

That is the part you can carry across fields, projects, and years. That is the part that can compound.

Everything else may have been only the skin of an example you once saw.
