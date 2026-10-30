# Before AI Touches the World, Give the World Handles

> 发布日期:2026-08-28 · [中文](../zh/2026-08-28-让世界长出把手.md) | [English](../en/2026-08-28-give-the-world-handles.md)

---

Every new wave of AI brings back the same question: how smart can the model become?

That is an important question, but it is not the only one. Sometimes it is not even the first one.

Anthropic's research preview of the Model Hardware Standard, announced on August 27, 2026, points to a different bottleneck. The issue is no longer just whether an AI agent can reason through a task. The issue is whether the world has been given enough handles for the agent to touch it without breaking it.

MHS is aimed at scientific research and advanced manufacturing. In plain terms, it is a standard interface that lets AI agents operate physical equipment such as microscopes, liquid handlers, robotic arms, and other programmable devices. The project began as a collaboration between Anthropic and HHMI Janelia Research Campus, and it is currently a limited research preview before a planned open-source release.

The interesting part is not that this sounds futuristic. The interesting part is that it is so practical.

MHS is not trying to make hardware magical. It gives hardware standardized drivers. It defines simple actions like reading a device state or writing a new setting. It lets devices advertise what they are, what they can measure, what can be adjusted, and what safety limits must be enforced. It can be accessed through MCP, command-line tools, or APIs.

In other words, it gives the physical world handles.

## A Handle Is Not a Shortcut

A handle is a very ordinary thing. A door handle does not make you stronger. It simply turns a wall into something you can open.

That is the right way to think about AI interfaces.

Before a machine can help with real work, the work has to become readable. What is the current state? What actions are allowed? What actions are dangerous? What counts as success? What should happen when the system sees a strange result?

Without answers to those questions, a more powerful model only gives us a more confident guesser.

This is why MHS matters beyond laboratories. The standard is described as reducing hardware integration work from weeks or months to hours or minutes. In one early example from Carnegie Mellon University, researchers described building MHS drivers and an orchestration layer for multiple lab instruments in about eight hours, compared with the weeks a vendor-built setup might take.

The real win is not "AI did a lab task." The win is that a mess of incompatible machines became a legible system. Once that happens, the cost of trying the next experiment changes. The bottleneck moves from "can we wire this together?" to "what should we test next?"

That shift is subtle, but it is enormous.

## Loops Beat Bursts

Most people still use AI in bursts. Ask a question. Get an answer. Copy the answer somewhere. Maybe ask again.

But real improvement usually comes from loops: act, observe, compare, adjust, repeat.

The early MHS examples are interesting because they show AI entering that loop. Anthropic describes Claude adjusting a laser, watching the result through a camera, learning the relationship between movement and beam position, and then packaging the learned behavior into deterministic code. In Genentech's proof-of-concept work on a BCA protein assay, Claude used experimental readings to tune liquid handling parameters, arriving at different flow rates for water and viscous protein samples. In another partner example, a qPCR workflow used MHS-connected cameras and lab devices to detect bubbles and trigger an automated recovery process.

None of this should be read as "the AI scientist has arrived."

The better reading is this: when the world becomes instrumented, AI can participate in feedback. It can see enough state, take constrained actions, measure consequences, and update the next step.

That is where compounding starts.

If a task is only a prompt, it is consumed once. If a task becomes a loop, every run can improve the next run. The output becomes the next input. Errors become training material. Edge cases become rules. Repeated work becomes a system.

This is one of the most important habits in the AI age: do not just ask AI to finish the current task. Ask what trace this task should leave behind so the next version of the system becomes better.

## The World Pushes Back

The physical world is a useful antidote to AI fantasy.

A text hallucination can be edited. A bad spreadsheet formula can be corrected. A wrong lab action can waste samples, damage hardware, or create a safety problem. The closer AI gets to physical reality, the less tolerance we have for vague confidence.

Anthropic is explicit about this boundary. MHS still requires programmable interfaces. It does not yet work with hardware that has no programmatic way to be controlled. More importantly, Claude's physical and spatial reasoning still needs expert oversight. In the Genentech example, researchers had to guide Claude to understand that bubbles in a liquid sample were a physical failure, not a software problem that could be fixed by simply retrying.

That detail is worth sitting with.

AI often behaves as if the world is made of symbols. The world is not. Liquids foam. Motors drift. Samples degrade. A camera angle lies. A sensor fails. A robot arm occupies actual space.

So the lesson is not "trust the agent." The lesson is "design the boundary."

The more power we give AI, the more explicit the boundary has to become: safety limits, approval points, logs, state visibility, rollback paths, and human responsibility. A strong system is not one where the human disappears. A strong system is one where the human no longer has to do every repetitive motion, but still owns the question, the risk, and the final judgment.

That is the version of AI that makes people stronger instead of lazier.

## Ordinary Work Needs Handles Too

Most of us do not run quantum hardware or automated biology labs. But the same pattern appears in ordinary knowledge work every day.

A small team says it wants AI to help, but the real state of the work lives in scattered chats, half-finished documents, personal memory, and filenames like "final-final-new." A creator says they want AI to write better, but their taste, examples, rejected drafts, and editorial principles are nowhere that an AI can inspect. A founder says they want agents to build products, but there is no definition of done, no user evidence, no acceptance test, and no decision log.

Then the model is blamed for being unstable.

Sometimes it is unstable. But often we have given it no handle.

A personal AI workbench does not begin with a smarter model. It begins with making work legible:

- What inputs matter?
- What does a good output look like?
- Which past decisions are still current?
- What facts are verified, and what is still a guess?
- Where should the AI stop and ask for human judgment?
- What evidence would prove that the work actually helped?

These questions sound boring. That is why they are powerful.

They turn private friction into public structure. They make repeated work teach the system. They let AI operate inside a human standard instead of replacing the standard with statistical fluency.

In that sense, each person can become a tiny standards body for their own work. Your notes, checklists, naming conventions, review rubrics, examples, and tests are not administrative leftovers. They are the handles you give to future intelligence.

## The New Literacy Is Interface-Making

For a long time, expertise often looked like private skill. The expert knew where to look, what mattered, and what to ignore. Much of that knowledge stayed tacit, carried in memory and habit.

AI changes the reward structure.

If execution becomes cheaper, the bottleneck moves upstream. The valuable person is no longer just the one who can do the task. It is the one who can define the task so clearly that people and machines can improve it together.

That means turning judgment into artifacts without flattening it into bureaucracy. It means writing down the few rules that actually matter. It means creating feedback loops that catch errors early. It means preserving context so that the next attempt starts higher than the last one.

This is not about worshiping process. Bad process slows people down. Good handles give people more world to think with.

A handle lets a model act. A measurement lets reality answer. A boundary keeps power from becoming damage. A log lets memory survive the current session. A test lets taste become visible enough to improve.

Put those together, and AI stops being a magic box. It becomes part of a self-evolving system.

## Give the World Handles

The most practical question after reading about MHS is not "when will AI run every lab?"

The better question is smaller and closer:

What part of my own world still has no handle?

Maybe it is a recurring decision that lives only in your head. Maybe it is a workflow that everyone complains about but nobody has mapped. Maybe it is a creative standard you can feel but have never expressed. Maybe it is a review process that depends on mood instead of evidence.

Start there.

Name the state. Define the allowed actions. Write the safety limit. Record the result. Let the next attempt inherit something from this one.

That is not glamorous work. But it is the work that converts AI from convenience into leverage.

The future will not belong only to people with the largest models. It will belong to people who can give messy reality enough handles that intelligence can enter, act, learn, and still remain accountable.

Before AI touches the world, the world needs handles.

And before AI can truly strengthen us, we have to become the kind of people who know where those handles should be.

## Sources

- [Anthropic: Previewing the Model Hardware Standard, August 27, 2026](https://www.anthropic.com/news/model-hardware-standard-research-preview)
- [Model Hardware Standard research preview site](https://modelhardwarestandard.com/)
- [Anthropic: Introducing the Model Context Protocol, November 25, 2024](https://www.anthropic.com/news/model-context-protocol)
