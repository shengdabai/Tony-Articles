# Abstraction Has to Earn Trust

> 发布日期:2026-08-14 · [中文](../zh/2026-08-14-抽象要先赢得信任.md) | [English](../en/2026-08-14-abstraction-has-to-earn-trust.md)

---

Every new programming abstraction arrives with the same promise: you will no longer have to think about the lower layer.

You will not have to write machine code. You will not have to manage every file by hand. You will not have to translate a business idea into boilerplate. You will not have to remember the syntax. You will not even have to write the code. Just express the intent, and the machine will do the rest.

This promise is powerful because it is partly true.

The history of computing is, in many ways, the history of moving human attention upward. We stopped entering raw numeric instructions and began writing higher-level languages. We stopped editing everything in isolation and built compilers, operating systems, databases, IDEs, version control, tests, package managers, CI pipelines, cloud platforms, and now AI coding agents. Each layer removed some previous burden from the human mind.

But there is a trap in this story. People hear "higher abstraction" and imagine "less need for care." History says the opposite.

An abstraction wins only after it earns trust. And trust is earned not by the beauty of the idea, but by its contact with performance, verification, migration cost, ecosystem fit, and failure recovery.

That is the part we keep forgetting.

## The Dream Is Older Than AI

AI coding feels new because the interface is new. Natural language has walked into the developer workflow. A person can describe a feature, ask for a refactor, request a test, or paste an error message, and the machine responds with plausible code. The emotional effect is strong: the distance between thought and software seems to collapse.

But the dream itself is old.

IBM's history of Fortran describes a world in the early 1950s where programming meant machine language, written by a small specialist class. Fortran was created in 1954 and commercially released in 1957. IBM says it let scientists, mathematicians, and engineers express problems more directly, and that work once requiring as many as a thousand hand-coded instructions could be reduced to 47 Fortran statements.[^1]

That was not a small convenience. That was a change in who could speak to the machine.

The deeper lesson, however, is not "high-level language good." The deeper lesson is that Fortran had to prove itself against the fear of the time: compiled code would be too slow. IBM notes that the team implemented the first optimizing compiler and produced code nearly as fast as handcrafted numerical code.[^1] In other words, the abstraction did not win because it sounded elegant. It won because it paid the performance tax.

This is the recurring pattern.

A new abstraction first looks irresponsible to the people who have been carrying the old layer in their hands. They know exactly what can go wrong. They know where the machine lies, where the workflow breaks, where the invisible cost hides. Their skepticism is not always backwardness. Sometimes it is memory.

To cross the line from toy to infrastructure, the abstraction has to answer the old layer's hardest objection.

## Failed Abstractions Are Still Teachers

After Fortran, the same desire kept returning in different forms.

CASE tools tried to industrialize the software development lifecycle. The programmer's apprentice projects tried to build intelligent assistants from expert knowledge and formal representations. Intentional Programming tried to separate a developer's intent from the textual source code that happened to express it.

These ideas were not stupid. Many of them were early signals of things we still want.

We do want requirements, design, code, tests, and documentation to stay connected. We do want an assistant that can analyze, modify, explain, verify, and document programs. We do want software intent to survive changes in syntax, frameworks, and implementation detail.

The problem was not always the destination. Often it was the path.

Some tools demanded too much migration from the surrounding ecosystem. A programming world built around text had already accumulated its own muscles: editors, grep, diff, patch, version control, code review, build systems, habits, and trust. To tell that world to abandon text was not merely to propose a better representation. It was to ask millions of workflows to leave their ground.

Some systems tried to encode too much human expertise explicitly. They turned intelligence into a handcrafted knowledge base, hoping that enough rules and formal structures would capture what expert programmers knew. But real software is full of context, exceptions, tradeoffs, naming, intent drift, organizational memory, and edge cases that resist clean encoding.

Some tools confused control with understanding. They gave managers diagrams, repositories, and processes, but could not make the messy reality of software obedient to the diagram.

This is why failed abstractions matter. They show us the difference between a correct longing and a workable bridge.

A correct longing says: this lower layer is wasting human life.

A workable bridge says: here is how people can move upward without losing evidence, speed, compatibility, reversibility, or control.

Most revolutions die in the space between those two sentences.

## The Bitter Lesson Helps, But Does Not Finish the Job

Large language models changed the path.

Instead of asking humans to hand-code all the knowledge, modern AI systems learn statistical patterns from large-scale data. The Transformer paper, submitted in 2017, proposed a sequence model based on attention rather than recurrence or convolution, and emphasized parallelizability and training efficiency.[^2] CodeBERT, submitted in 2020, used Transformer-based pretraining for programming languages and natural language, supporting tasks such as code search and documentation generation.[^3]

This fits Richard Sutton's "Bitter Lesson": across AI history, general methods that scale with computation tend to win over approaches that try to bake in human knowledge by hand.[^4]

That lesson explains why today's AI coding tools feel so different from earlier attempts. They do not need someone to enumerate every pattern in a symbolic database. They can absorb mountains of code and language, then produce useful local guesses in places where formal systems were brittle.

But there is a second lesson that is just as important: scalable generation is not the same as grounded correctness.

The model can write code that looks right before it is right. It can satisfy the shape of a solution while missing the reason the solution exists. It can use a familiar pattern in an unfamiliar boundary condition. It can repair a test while damaging an assumption not covered by that test. It can reduce the cost of producing code while increasing the importance of reviewing meaning.

So the abstraction has moved upward again, but the bill did not disappear.

The bill moved from typing to specifying, from syntax to intent, from local implementation to system behavior, from "can this compile?" to "does this still mean what we meant?"

This is why AI coding is not the end of software engineering. It is a new pressure test of software engineering.

## Brooks Was Still Right

In "No Silver Bullet," Frederick Brooks drew a distinction that still matters: accidental difficulties are created by the tools and methods around the work; essential difficulties live in the problem itself.[^5]

Good tools can remove accidental difficulty. They can reduce boilerplate, shorten feedback loops, automate translation, catch errors, and make more of the system visible. This is real progress. It should not be dismissed.

But if a program must coordinate money, identity, permissions, inventory, time, human expectation, failure, abuse, regulation, and changing business rules, then much of the difficulty is not a typing problem. It is a reality problem.

AI can help you move faster through that reality. It cannot make reality stop having edges.

This is where many people get confused. They use AI, feel the speed, and conclude that complexity has been defeated. But often only the first layer of complexity has been flattened. The deeper layer is still waiting: what should happen when two requirements conflict? What is the safe default? Who owns the result? Which failure is acceptable? What should be logged? What must never be inferred? What does the user actually need, not merely request?

Those questions do not vanish because the code appears faster.

Sometimes speed makes them more urgent.

## The Personal Version

For ordinary people, the lesson is not limited to programming.

Every AI tool is an abstraction. It lets you speak at a higher level: write this, summarize that, build this, compare these options, explain this field, make a plan, generate examples, find the error. That is useful. It can make a person stronger. It can also make a person lazy in a very polished way.

The dividing line is whether the abstraction earns trust inside your own workflow.

Do you know what the tool is allowed to decide? Do you know what you still need to verify? Do you have examples of good and bad output? Do you keep the source material close enough to check? Do you preserve the reasoning that matters? Do you know how to roll back? Do you have a way to notice when a smooth answer is hiding a broken assumption?

If not, you are not using abstraction. You are outsourcing attention.

That is the weak version of AI use: let the machine remove friction so I can stop thinking.

The strong version is different: let the machine remove the lower friction so I can think at a higher level, with better standards.

This is why the boring parts matter. Tests matter. Notes matter. Source links matter. Small examples matter. Checklists matter. Version history matters. Naming matters. A clear "done" condition matters. So does a rule that says private material must be abstracted before public writing.

These are not bureaucratic decorations. They are how a new abstraction earns the right to carry weight.

## Higher Is Not Looser

The wrong lesson from AI is that we can be more casual because the tool is more capable.

The right lesson is that we can work at a higher level only if the lower levels become more trustworthy.

Fortran did not eliminate concern for performance. It had to answer performance. Version control did not eliminate concern for change. It made change inspectable. Tests did not eliminate concern for correctness. They made parts of correctness executable. AI does not eliminate concern for intent. It makes intent the new center of the work.

So when you raise the abstraction level, do not lower the standard.

Ask a harder question: what must become visible, testable, reversible, and teachable before I let this abstraction into my real life?

That question is not anti-AI. It is the only way to use AI without becoming softer.

The future will contain more natural language, more agents, more automatic code, more generated media, more invisible execution, more tasks handed to machines. The interface will feel simpler. The underlying responsibility will not.

The people who benefit most will not be the ones who believe every new abstraction immediately. Nor will they be the ones who reject it because the old layer feels safer.

They will be the ones who know how to make abstraction pay its way: connect it to evidence, constrain it with standards, test it against reality, and keep the human mind growing above it.

Abstraction is not an escape from responsibility.

It is a ladder. Every rung has to hold.

[^1]: IBM, "Fortran." https://www.ibm.com/history/fortran
[^2]: Ashish Vaswani et al., "Attention Is All You Need," submitted June 12, 2017. https://arxiv.org/abs/1706.03762
[^3]: Zhangyin Feng et al., "CodeBERT: A Pre-Trained Model for Programming and Natural Languages," submitted February 19, 2020. https://arxiv.org/abs/2002.08155
[^4]: Richard Sutton, "The Bitter Lesson," March 13, 2019. https://www.incompleteideas.net/IncIdeas/BitterLesson.html
[^5]: Frederick P. Brooks, Jr., "No Silver Bullet: Essence and Accidents of Software Engineering," IEEE Computer, April 1987. https://ieeexplore.ieee.org/document/1663532
