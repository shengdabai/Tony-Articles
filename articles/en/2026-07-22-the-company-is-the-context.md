# The Company Is the Context

> 发布日期:2026-07-22 · [中文](../zh/2026-07-22-公司本身才是上下文.md) | [English](../en/2026-07-22-the-company-is-the-context.md)

---

The easiest mistake in enterprise AI is to think the model is the product.

It is not.

The model is an engine. Sometimes a brilliant engine. Sometimes a noisy one. Sometimes too expensive, sometimes surprisingly cheap. But in a real organization, the engine is rarely the thing that determines whether AI creates value.

The harder question is: what can the engine actually touch?

Can it see the history of decisions? Can it read the messy documents where judgment is hidden? Can it know which rule is official and which rule is just a habit? Can it distinguish a reversible suggestion from an irreversible action? Can it ask for help at the right moment? Can someone later inspect why it did what it did?

If the answer is no, a stronger model does not solve the problem.

It only produces more impressive guesses.

This is why I think the next serious phase of AI is not about adding agents to companies. It is about turning the company itself into context.

That sounds abstract, but the pain is very concrete.

Many teams already have AI tools. People use them to write, summarize, translate, code, search, analyze, and draft. The individual gains are real. A person who knows how to use AI can move faster than before. A small team can attempt work that used to require more hands.

But when the work moves from personal productivity to organizational results, the magic often weakens.

One employee has useful prompts in a private account. Another has a folder full of half-cleaned data. A manager remembers why a workflow exists, but that reason was never written down. A senior person knows which edge cases can be ignored and which one will destroy trust, but that judgment lives only in conversation. A process crosses five systems, three approvals, two informal exceptions, and one person everyone secretly depends on.

Then someone says: "Let's add an agent."

The agent arrives and discovers that the company is not a system. It is a collection of memories trapped inside people, files, chats, habits, permissions, and unspoken exceptions.

So the agent behaves like a tourist.

It can describe the city. It cannot run the city.

Recent public research points in the same direction. McKinsey's 2025 State of AI survey found that 88 percent of respondents said their organizations regularly used AI in at least one business function, up from 78 percent the prior year. But only about one-third reported that their companies had begun to scale AI programs, and just 39 percent reported enterprise-level EBIT impact.[^1] The gap is not adoption. The gap is operational absorption.

Stanford's 2026 AI Index says organizational AI adoption reached 88 percent, which sounds huge.[^2] Microsoft, looking at its own productivity signals and a 20,000-worker survey, framed the issue even more sharply: in many cases, people are ready, but the systems around them are not.[^3]

That sentence is worth sitting with.

People are ready. The systems are not.

This explains why many AI conversations feel strangely upside down. We keep asking whether the model is intelligent enough, when the practical question is whether the organization is legible enough.

Legible to whom?

To the people doing the work. To the people reviewing the work. To the next person who inherits the work. And now, to the machines we expect to help with the work.

An AI system does not merely need data. It needs usable context.

Data says: here are the documents.

Context says: this document is old but still legally binding; that one is recent but only a draft; this customer promise overrides the generic policy; this number looks wrong because finance changed the classification last quarter; this approval step is ceremonial except when the amount crosses a threshold; this task is safe to automate, but that decision needs human sign-off.

Data is stored.

Context is organized judgment.

Most companies have more data than they can use and less context than they need. That is why AI often performs well in demos and poorly in production. A demo is a clean room. Production is a living house. The house has old wiring, hidden doors, family rules, and a chair nobody moves because someone once got hurt there.

The model can enter the house only if the house teaches it how to behave.

This is also why "AI native organization" is a dangerous phrase when used too early. It can seduce people into chasing a label instead of doing the ordinary work of redesign.

The goal is not to look AI native.

The goal is to make work computable without making people stupid.

That second half matters.

There is a lazy version of AI transformation. It says: let the agent do more so humans can think less.

There is a stronger version. It says: let the agent handle the repeatable parts so humans can move their judgment to a higher level.

The lazy version replaces work with output. The stronger version converts hidden judgment into a system. That conversion is slow, unglamorous, and extremely valuable.

I like to think of it as four layers.

The first layer is memory.

Not "we have a knowledge base." That is too easy. A folder full of documents is not memory. Memory means the organization can retrieve the right piece of history at the moment of action.

Why did we choose this vendor? Why did we stop using that metric? What failed last time? Which exception was accepted once but should not become policy? Which customer complaint changed the standard?

If these answers live only in people's heads, AI will either miss them or force the human to repeat them every time. The system has no compound interest.

The second layer is workflow.

A workflow is not a diagram in a slide deck. It is the actual path by which intention becomes result. If that path depends on copy-paste, private messages, undocumented approvals, and "ask that person because they know," then the agent cannot really join the work. It can only stand beside it.

To bring AI into a workflow, the workflow must become explicit enough to be inspected. What triggers the task? What inputs are trusted? What outputs are acceptable? Where does uncertainty go? Which steps are rules, and which steps are judgment?

This is why simply inserting AI into an old process often disappoints. The old process was designed around human memory, human improvisation, and human tolerance for ambiguity. The machine exposes that debt.

The third layer is permission.

Permission is not only security. It is product design for trust.

What can the agent read? What can it draft? What can it change? What must it never touch? When does it need approval? How do we revoke access? How do we audit its path?

An agent with no permission is a chatbot. An agent with too much permission is a risk. The useful zone is in the middle: enough access to do real work, enough boundary to make the work reversible and reviewable.

The fourth layer is evaluation.

This is where many projects become theater.

People ask, "Is the answer good?" But in an organization, good is not a feeling. Good means the task moved closer to an outcome. A customer got a correct answer faster. A report reduced a decision cycle. A draft preserved the tone and legal constraints. A support case was routed with enough context for a human to finish quickly. A repeated process became cheaper without becoming more fragile.

Output is what the model gives you.

Outcome is what the system can rely on.

The distance between the two is the real work.

There is a useful warning in the MIT NANDA State of AI in Business 2025 report. It argued that despite heavy enterprise investment, most organizations were seeing no measurable return, and that many custom systems stalled because of brittle workflows, poor contextual learning, and misalignment with daily operations.[^4] You do not have to accept every number in a report as destiny to see the pattern. The failure mode is not mysterious: companies buy intelligence before making themselves readable.

That order is backwards.

Before asking "Which agent should we deploy?" ask "Which part of our work can be made visible, bounded, and measurable?"

Before asking "Which model is best?" ask "What judgment are we trying to preserve?"

Before asking "How do we automate this?" ask "What should still require a human, and why?"

Before asking "How many tasks can AI replace?" ask "What learning should return to the organization after each task is done?"

This last question is the most important one to me.

A good AI system should not merely finish work. It should make the organization better at future work.

If an agent handles a support case, the organization should learn which missing document caused confusion. If an agent drafts a proposal, the organization should learn which examples were reusable. If an agent analyzes a report, the organization should learn which metric definition created friction. If an agent fails, the failure should improve the boundary, the checklist, the retrieval, or the approval rule.

Otherwise the company is just renting intelligence by the minute.

Renting intelligence is useful, but it is not transformation.

Transformation begins when every run leaves the system slightly more capable than before.

This is where the idea of a self-evolving system becomes practical instead of poetic. It does not mean the machine magically improves itself while humans disappear. It means the organization creates loops where work, feedback, correction, and memory reinforce one another.

The loop can be simple.

A task is defined. The agent works inside a boundary. The output is reviewed. The review changes a rule, a template, a source, a permission, or a test. The next run starts from a better system.

Do this once and it feels small.

Do it every day and the organization changes shape.

For an individual, this is also the right way to use AI.

Do not only ask AI to help you finish today's thing. Ask what part of today's thing should become tomorrow's system. A checklist. A reusable prompt. A script. A note. A decision rule. A better folder. A clearer standard. A small tool.

This is how AI makes a person stronger rather than lazier.

Laziness consumes capability.

Strength metabolizes capability into structure.

The same is true for companies.

The winners will not simply be the organizations with the most agents, the largest model budget, or the loudest AI strategy. They will be the organizations that turn their work into context, their context into workflows, their workflows into learning loops, and their learning loops into compounding advantage.

In the end, an agent does not transform a company from the outside.

It reveals what kind of company was already there.

If the company is a pile of hidden exceptions, the agent will amplify confusion. If the company is a set of clear loops, the agent will amplify learning.

So maybe the first AI question for any organization is not technical at all.

Can our work explain itself?

If it cannot, start there.

Because the company is the context.

And without context, even intelligence has nowhere to stand.

[^1]: McKinsey, "The State of AI: Global Survey 2025." https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
[^2]: Stanford HAI, "The 2026 AI Index Report." https://hai.stanford.edu/ai-index/2026-ai-index-report
[^3]: Microsoft WorkLab, "2026 Work Trend Index: Agents, Human Agency, and the Opportunity for Every Organization." https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization
[^4]: MIT NANDA, "The GenAI Divide: State of AI in Business 2025." https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
