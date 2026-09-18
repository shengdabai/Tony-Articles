# Before You Break Down the Task, Separate the Layers

> 发布日期:2026-09-18 · [中文](../zh/2026-09-18-复杂问题，先别急着拆任务，先拆层.md) | [English](../en/2026-09-18-separate-the-layers.md)

---

Today I was organizing an old note about self-learning when one distinction stopped me.

A large task can be divided in two ways.

We can break it sideways into smaller tasks. We can also cut it vertically, separating the different layers tangled inside it.

Most productivity advice emphasizes the first kind. If writing a book feels too large, outline the chapters. If building a product feels intimidating, turn it into a backlog. If learning a skill feels overwhelming, make a daily plan.

That helps, but only when all the smaller tasks belong to roughly the same layer.

Sometimes they do not.

Imagine someone trying to build a small AI assistant. The assistant gives unreliable answers, so the person rewrites the prompt. Then they change the model. Then they reorganize the documents. Then they add another tool. After a week, almost everything has changed, but nobody can say what actually fixed or broke the system.

The task was divided into many tickets. It was not separated into layers.

Source quality, retrieval, reasoning, presentation, and evaluation were treated as one problem called “the AI is not good enough.” The list got longer. The problem stayed tangled.

This is the distinction I want to keep: when a complex task remains hard after being broken into pieces, stop making the pieces smaller. Ask whether the pieces belong to different layers.

## A long list is not the same as a complex structure

Twenty independent facts may be tedious to memorize, but each can be handled on its own. Three ideas can be much harder if understanding any one of them requires holding the other two in mind.

Learning researchers call this **element interactivity**. A 2023 review of cognitive load research argues that experienced complexity depends not simply on the number of elements, but on how many must be processed together—and on what the learner already knows. The same word can be one familiar unit to an expert and several unfamiliar marks to a beginner. [[Research](https://link.springer.com/article/10.1007/s10648-023-09782-w)]

This explains why “break it into smaller steps” sometimes disappoints us.

The steps may be shorter while their dependencies remain untouched.

A beginner learning to publish a website can receive a neat checklist: choose a framework, write the interface, connect a database, configure authentication, buy a domain, set up deployment, and monitor errors. Each item sounds manageable. Together they mix at least five layers: the user’s need, the product rules, the program’s behavior, the infrastructure, and the standard for deciding whether it works.

When an error appears, the beginner does not know whether the idea is wrong, the code is wrong, the environment is wrong, or the test is wrong. Every failure feels like one verdict: “I cannot do this.”

But that verdict contains almost no information.

The useful question is narrower: **At which layer did the result first stop matching the expectation?**

That question turns a judgment about the person into a diagnosis of the system.

## Horizontal decomposition gives motion; vertical decomposition gives clarity

Horizontal decomposition answers: “What smaller jobs must be completed?”

Vertical decomposition answers: “What kind of problem am I dealing with at this moment?”

I find five layers useful for many learning and AI projects:

- **Purpose and standard:** What change do I want, and what would count as good?
- **Knowledge and data:** What facts, examples, context, and boundaries does the work require?
- **Method and process:** In what order should the material be transformed or the decision be made?
- **Tool and execution:** Which model, application, code, or person will perform each operation?
- **Verification and delivery:** How will I detect errors, and where must the result arrive to become useful?

These are not universal laws. They are labels for separating conversations that should not happen all at once.

Suppose an AI-generated article feels weak. “Improve the writing” mixes several possible failures. Perhaps the evidence is thin. Perhaps the main claim is vague. Perhaps the reasoning jumps. Perhaps the voice feels borrowed. Perhaps the article is good but formatted for the wrong channel.

Changing the prompt may alter the prose while leaving the real failure untouched.

A layered diagnosis is different. Freeze the evidence and test the claim. Freeze the claim and test the structure. Freeze the structure and test the voice. Freeze the content and test the delivery format. Each experiment changes one layer and leaves the others stable enough to learn from the result.

This is ordinary engineering, but it is also a way of protecting self-confidence. A person who mixes every layer experiences every bug as a personal inability. A person who separates layers can say, “The source is fine; the retrieval failed,” or, “The reasoning is sound; the acceptance test is missing.”

The second person has not magically become smarter. They have made the failure local.

## AI can multiply a tangled problem

AI is excellent at horizontal decomposition. Ask for a plan and it can produce ten steps in seconds. Ask for subtasks and it can produce fifty.

That speed creates a new risk: a detailed plan can look like a clear model of the problem even when its layers are still mixed.

You can now execute a confused decomposition very quickly.

This is why I do not think the best first request is always “Give me a step-by-step plan.” A better request is often:

> Do not propose a plan yet. Separate this problem into layers. For each layer, state its input, output, assumptions, failure signal, and what must remain fixed while it is tested.

The answer will not automatically be correct. Layer boundaries are hypotheses, not facts. Real systems are coupled. A product decision can change the data requirement; a tool limitation can change the process; a failed test can reveal that the original goal was poorly defined.

The point is not to pretend that every system can be pulled apart cleanly.

A 1962 paper, “The Architecture of Complexity,” used the idea of **near decomposability**: many complex systems have parts whose internal interactions are stronger than their interactions with other parts. That partial separation—not perfect independence—makes the system easier to describe and understand. [[Paper](https://www.jstor.org/stable/985254)]

That is a useful limit for this method. We are not looking for sealed compartments. We are looking for boundaries stable enough to run one informative experiment.

## A fifteen-minute layer map

The next time a task feels “too complicated,” try this before making another checklist.

Write the desired result in one sentence. Then write the current failure in one sentence. Avoid personality judgments. “I am bad at building products” is not a failure description. “A first-time user cannot finish the setup without help” is.

Now list everything involved and sort it into the five layers: standard, knowledge, process, execution, and verification. If two items keep moving together, draw the connection between them. If one item appears in several layers, rename it more precisely.

Then choose one layer to test. Freeze the others as much as possible.

If you are learning a technical skill, use a known working example so that the environment is temporarily fixed. Change one concept and predict what will happen before running it.

If you are improving an AI workflow, keep the model and prompt fixed while testing the source material. Then keep the source material fixed while testing retrieval. Do not change the whole stack and call the final output an experiment.

If you are writing, separate research, judgment, structure, voice, and formatting. Do not ask a rough paragraph to prove all five at once.

Finally, record the interface between layers: what exactly must leave one layer before the next can begin? A research layer may need a source table, not “enough reading.” A reasoning layer may need a claim with a counterexample, not “deeper thought.” A delivery layer may need a file that opens on the reader’s device, not merely text that exists somewhere.

There is a simple test for whether the map is useful:

**When something fails, can you name the layer that failed and the evidence that showed it?**

If not, the work is still tangled.

AI keeps making execution cheaper. That does not make layered thinking less important. It makes it more important, because confusion can now travel faster and produce more convincing output.

The people who become stronger with AI will not be the ones who generate the longest task lists. They will be the ones who can isolate a layer, preserve the right constraints, run a small test, and carry what they learned into the next layer.

So when I feel stuck now, I want to delay one familiar question: “Which tool should I use?”

There is a better question to ask first.

**Which layer am I actually in?**
