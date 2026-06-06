# The Person Closest to the Problem Should Build the Tool

> 发布日期:2026-06-07 · [中文](../zh/2026-06-07-离问题最近的人才该造工具.md) | [English](../en/2026-06-07-closest-to-problem-builds-tool.md)

---

For a long time, software had a quiet class system.

There were the people who had problems, and there were the people who were allowed to build tools. The first group wrote tickets, filled in requirement documents, explained the same workflow again and again, waited for engineering capacity, compromised on scope, then adjusted their lives around whatever finally shipped. The second group translated those problems into systems.

This arrangement made sense when software required years of specialized training. It was not unfair by design. It was just expensive. Code was a high-friction medium, so the right to turn pain into tools naturally concentrated in the hands of people who could speak that medium.

AI is changing that boundary. Not because everyone will suddenly become a professional engineer. They will not. But because the first working version of a tool no longer has to begin inside an engineering team. It can begin with the person who is tired enough, specific enough, and close enough to the problem to describe exactly what hurts.

That sounds small. It is not.

## The old bottleneck was translation

Most bad internal tools are not bad because engineers are careless. They are bad because every tool built for someone else passes through a translation layer.

The user says, "I need to know which customer needs attention today." The product spec says, "Create a dashboard showing account risk and engagement signals." The engineer builds, "A table with filters, sortable columns, and status labels." None of these sentences is wrong. But something gets lost at each step. The original problem was not a dashboard problem. It was a morning anxiety problem. The real tool might be a dashboard, a daily email, a Slack message, or a two-line note attached to the next meeting.

The person closest to the problem usually knows this. They know which field is technically available but practically useless, which "small" exception quietly eats an hour, and what the tool must not do because they have lived with the damage caused by the current workaround.

But in the old system, that person often had no direct path from pain to prototype. They could only explain, and explanation is lossy. AI reduces that loss. A person who cannot write production code can now describe a workflow, ask for a small script, test it against their real day, notice where it breaks, and iterate. The output may be rough. It may need review. It may never deserve to become company infrastructure. But for the first time, the problem-holder can touch the shape of the solution directly.

That is not just efficiency. That is a transfer of agency.

## This has happened before

The idea that non-programmers create software is not new. Spreadsheets have been doing this for decades.

A spreadsheet is a strange thing. To one person it is a grid. To another it is a database. To another it is a budgeting app, a pricing engine, a hiring tracker, or a tiny operating system for a business process. Computer scientists call this end-user programming: people who are not professional developers creating or modifying software for their own needs.

The National Science Foundation once put it plainly: if you have written a spreadsheet formula or automated a repetitive task in email, you have done a kind of programming. You may not call yourself a programmer, but you have instructed a machine to do work.

That is why spreadsheets became so powerful. They gave toolmaking power to people who would never ask permission to become software engineers first. But spreadsheets also show the danger. When end users build tools, they often build without tests, version control, documentation, security review, or a clear mental model of failure. A spreadsheet can save a business. It can also quietly become the business's most fragile production system.

So the lesson is not "everyone should code now." The lesson is more precise: the first mile of tool creation belongs closer to the problem, but the last mile still needs engineering discipline.

AI makes the first mile cheaper. It does not make the last mile optional.

## The nurse in the basement

One of my favorite examples of problem-near invention comes from medicine.

In the 1960s, hospital staff responding to emergencies often had to gather equipment from different places. The delay was not a philosophical problem. It was a drawer problem, a hallway problem, a "where is the thing we need right now" problem.

An emergency department nurse named Anita Dorr built a prototype of what became the modern crash cart in 1967. She did not begin from a grand theory of hospital logistics. She began from repeated exposure to a specific failure: in an emergency, people were losing time because the needed tools were not already together. That is what proximity does. It gives you details a remote expert has to reconstruct from interviews. It also gives you emotional pressure. You are not merely studying the inefficiency; you are tired of watching it happen.

The crash cart is not powerful because it was technically complex. It is powerful because the solution matched the grain of the problem. Put the critical items together. Put them on wheels. Make them visible. In retrospect, it feels obvious. Most great operational tools do.

AI will create more of these basement moments. Not because everyone will invent something as consequential, but because more people can move from "this keeps hurting" to "let me build a small thing that changes it."

The revolution is not that code becomes magical. The revolution is that irritation becomes executable.

## A recent AI version of the same pattern

Anthropic recently published a story about a sales employee who joined without coding experience and used Claude Code to rebuild parts of his own workflow. He created a Gmail-based drafting tool, later worked on a sales plugin, and Anthropic says that within months roughly 80 percent of its sales organization was using that plugin.

The number is less important than the pattern.

The useful tool did not begin with a generic question like, "How can AI improve sales?" It began in the mess: too many customers, too many product updates, too many places to search, too much time lost translating technical information into useful replies. The builder understood the pain because the pain was his calendar.

This is why the phrase "nontechnical builder" slightly misses the point. The person may lack formal coding experience, but they are deeply technical in the domain itself. They understand the hidden machinery of the work: timing, tone, exceptions, priorities, handoffs, trust, and failure.

AI does not replace that domain knowledge. It gives it a new outlet. Many people think the new superpower is "AI can write code." That is only the surface. The deeper superpower is that the person who understands the work can pressure-test that understanding as a working artifact.

A prototype is thinking made tangible. Once it exists, people can argue with it, use it, reject it, improve it, and find the next problem underneath it.

## But closeness is not enough

There is a trap here, and it matters.

Being close to a problem gives you better taste for the problem. It does not automatically give you system judgment.

The first version of a tool is often built for one person, one workflow, one set of assumptions, one happy path. That is fine. But the moment a tool spreads, the risk changes. Personal automation becomes shared dependency. A clever script becomes operational infrastructure. A prompt becomes policy. A shortcut becomes a standard.

This is where the builder needs humility.

If your AI-built tool helps only you, the standard is simple: does it save time without fooling you? But if other people begin to rely on it, a different set of questions appears.

What happens when the input is wrong?

What happens when the model invents a detail?

Who can see the data?

How does someone know whether the output is current?

Can the tool be turned off?

Who owns it when you leave?

These are not bureaucratic questions. They are the questions that separate a useful hack from a trustworthy system.

Apollo did not reach the Moon because one brilliant person had a clever idea. At its peak, the program involved about 400,000 people and support from more than 20,000 firms and universities. What made it possible was systems engineering: interfaces, constraints, verification, responsibility, and endless attention to how parts fail together.

Most of our little AI tools do not need Apollo-level process. But they do need a small dose of Apollo thinking. Define the boundary. Name the failure modes. Keep a human checkpoint where judgment matters. Make the tool observable. Write down what it assumes. Do not confuse "it worked once" with "it is safe to depend on."

The future belongs neither to pure coders nor pure domain experts. It belongs to people who can stand between pain and system.

## The new literacy is problem architecture

If I had to name the skill underneath all this, I would not call it coding. I would call it problem architecture: the ability to look at recurring pain and separate the real job, important inputs, human judgments, repeatable steps, expensive failure points, and deliberately manual parts.

This is different from asking AI to "build me an app." That sentence usually hides the problem. A stronger sentence is: "Every Friday I spend two hours collecting these five pieces of information from these three places, then turning them into this decision. Help me make the repeatable parts visible."

The second sentence is less glamorous. It is also much more powerful.

Most people do not need to become software engineers. But many people do need to become clearer owners of their own workflows. Stop treating repeated pain as weather. If something repeats, it can be studied. If it can be studied, it can often be shaped. If it can be shaped, some part of it can become a tool.

This is the real meaning of using AI to become stronger. Not asking the machine to do your thinking, but using it to turn your lived experience into a system you can inspect.

## Toolmaking as self-respect

There is a quiet dignity in building a tool for your own problem. It says: my irritation is data; my workflow is worth improving; I do not have to wait for someone else to notice what is broken in my day.

Of course, not every irritation deserves a tool. Some things should be ignored. Some should be solved by a conversation. Some should be handled by existing software. Some should be left manual because the friction is where the thinking happens.

But when a problem repeats, when the cost is real, when the current workaround keeps stealing attention, the person closest to it should no longer be limited to complaining, requesting, or waiting. They should be able to sketch, test, and build.

That is the shift.

AI is not merely making programmers faster. It is widening the circle of people who can participate in toolmaking. The important question is not whether these people are "technical." The important question is whether they are close enough to the problem, honest enough about the failure modes, and disciplined enough to turn a private fix into a reliable system only when it deserves to become one.

The best tools do not start with technology. They start with a person who has suffered a problem long enough to understand its shape.

In the old world, that person had to explain the pain to someone else and hope the translation survived.

In the new world, that person can begin.
