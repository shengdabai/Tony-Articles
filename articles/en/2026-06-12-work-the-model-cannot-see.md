# The Work the Model Cannot See

> 发布日期:2026-06-12 · [中文](../zh/2026-06-12-最值钱的工作藏在模型看不见的地方.md) | [English](../en/2026-06-12-work-the-model-cannot-see.md)

---

Every few months, the AI world rediscovers the same fear in a new vocabulary.

This time the phrase is "thin wrapper." If the model keeps getting better, then any product built on top of the model looks temporary. Today's clever app becomes tomorrow's system prompt. Today's workflow becomes a built-in feature. Today's startup becomes a screenshot in a model lab's launch post.

That fear is not stupid. It is half right, which is why it is dangerous.

The half that is right is simple: anything that can be clearly measured, cheaply verified, and generally accessed will be pulled toward commoditization. If the answer is public and the grading is cheap, models will compete there until the price falls. Open models will attack from below. Frontier labs will absorb the scaffolding from above. The middle layer gets squeezed.

But the other half matters more: not all valuable work is visible from the outside.

Some truth is private. Some correctness can only be established inside a company's real files, a team's real workflow, a doctor's real decision path, a law firm's real matter history, a founder's real operating rhythm, or a teacher's real classroom judgment. A smarter model does not automatically get access to those places. It does not sign the contract. It does not carry the liability. It does not own the relationship. It does not know what this specific human, in this specific context, will accept as good.

So the question is not "Will AI eat everything?"

The better question is: what part of your work can AI see, and what part of your work is still locked inside reality?

## What Gets Eaten First

Software engineering is a clean example because it has unusually good feedback loops.

SWE-bench, one of the best-known coding benchmarks, evaluates whether AI systems can resolve real GitHub issues. The benchmark gives a system an issue and a repository, then checks the proposed patch against tests.[^1] This is why coding agents improved so quickly there. The task is hard, but it has a relatively clear evaluation path: edit code, run tests, see whether the patch works.

When Devin was first introduced in 2024, Cognition reported a 13.86% success rate on a sampled SWE-bench evaluation, far above earlier baselines at the time.[^2] That number already felt impressive, and since then coding-agent scores have kept climbing. The broader direction is obvious: if a task can be represented as an issue, a codebase, and a test suite, model improvement will keep pressing on it.

That does not mean software engineering is finished. It means the visible part of software engineering is becoming cheaper.

There is a difference.

The testable part is the part the model can fight. The rest sits downstream: deciding what should be built, understanding why the old system is strange, knowing which customer promise cannot be broken, noticing that a technically correct patch creates an operational risk, reviewing the change, integrating it into a messy organization, shipping it without causing damage, and then maintaining trust after the release.

The benchmark can tell you whether tests pass. It cannot tell you whether the business should accept the risk.

That gap is where a lot of real value lives.

## Writing Code Is Not Shipping Software

A recent working paper on AI coding tools makes this gap visible in numbers. The study looked at more than 100,000 GitHub developers and compared generations of AI coding tools. The headline is striking: autonomous coding agents were associated with about 180% more commits. But that effect dropped sharply across the production chain, to about 50% more projects and only about 30% more actual releases.[^3]

In plain English: AI helped people produce much more code, but far less of that gain turned into shipped software.

That should not surprise anyone who has built anything real.

Writing is not shipping. A commit is not a product. A product is not adoption. Adoption is not trust. Trust is not a one-time event.

The same pattern appears outside code. AI can generate a proposal, but it cannot automatically make the client believe it. It can summarize a meeting, but it cannot know which sentence in the room changed the politics. It can draft a learning plan, but it cannot feel where the learner is pretending to understand. It can create a beautiful dashboard, but it cannot decide which number the team is allowed to ignore and which number must wake someone up at midnight.

The machine is strong where the world has been converted into text, tests, labels, interfaces, and repeatable feedback.

The machine is weaker where the world still lives as permission, trust, tacit judgment, relationship, taste, timing, and responsibility.

And most serious work contains both.

## Private Truth Is Not Just Private Data

People often hear "private data" and think the answer is simply to collect more files.

That is too shallow.

Private data matters, but private truth is bigger than private data. A folder full of documents is not yet a working system. A chat history is not yet judgment. A CRM export is not yet a sales process. A pile of lesson notes is not yet a teacher's eye. A codebase is not yet an engineering culture.

The valuable work is the translation layer.

Someone has to arrange messy reality so a model can act on it. Someone has to decide which documents matter, which names must be hidden, which tool is allowed to touch which file, which step needs human approval, which failure should stop the workflow, which output is "good enough," and which output is dangerous even if it looks polished.

That work is not glamorous. It looks like naming things carefully. It looks like writing checklists. It looks like building small scripts. It looks like cleaning old folders. It looks like creating logs, review points, rollback paths, and simple dashboards. It looks like sitting with a person's actual work for long enough to notice where the friction really is.

But that is exactly why it is hard to copy.

A model lab can improve the general model. An open-source project can improve the tool. But neither can walk into your life and automatically know your constraints, your taste, your deadlines, your trust boundaries, your old mistakes, your weird folder structure, your half-formed goals, and the things you will never put into a public prompt.

That is not a reason to reject AI. It is a reason to use AI at the right layer.

Do not ask AI only to produce more visible output. Use it to help you make the invisible structure of your work explicit.

## The Real Product Is the Local Operating System

This is why I have become more interested in local AI workstations than in generic AI tips.

Most people do not need another list of prompts. They do not even need another tool first. They need a working environment where their own reality has been mapped into a system.

Where are the notes? Which files are safe to publish? Which customer details must never leave the machine? Which repeated task should become a script? Which decision needs a human checkpoint? Which folder is the source of truth? Which output should be bilingual? Which workflow should leave an audit trail? Which task is urgent because it creates external proof, and which task is just internal polishing?

Once those questions are answered, AI becomes much more powerful. Not because the model suddenly got smarter, but because the world around the model became legible.

That is the part many people skip.

They want the agent before the operating system. They want automation before boundaries. They want speed before definitions. Then they are surprised when AI produces a lot of motion and very little durable progress.

The order should be reversed.

First, define what counts as done. Then define what must not happen. Then expose the right materials. Then add the model. Then let the system record what happened. Then improve the loop.

That is engineering, but it is also a philosophy of learning.

You are not using AI to avoid thinking. You are using AI to move your thinking into a higher-resolution environment.

## A Small Test for Your Own Work

If you want to know whether your work has an "untrainable" part, ask four questions.

First: what do I know that is not public?

Not secret in a dramatic way. Just context. History. Taste. Personal standards. Local constraints. The reason a simple-looking task is actually fragile.

Second: where does correctness require permission?

If the model needs access to private files, customer context, internal tools, student history, production systems, or money-moving workflows, intelligence alone is not enough. Permission becomes part of the work.

Third: where does the answer require accountability?

Who signs off? Who gets blamed if it fails? Who decides that "resolved" really means resolved? The person who owns that judgment owns more value than the person who merely generates an answer.

Fourth: what feedback loop can I build?

If a task matters, do not leave improvement to vibes. Capture examples. Store decisions. Write down rejection reasons. Make a small benchmark of your own. The public benchmark belongs to the public. Your private benchmark becomes your compounding asset.

These questions are not only for startups. They are for anyone trying to stay strong in the AI age.

A teacher can turn repeated classroom judgment into a learning system. A creator can turn scattered observations into a writing machine. A small business owner can turn daily operational pain into a local assistant. A developer can turn undocumented project memory into checkable constraints. A learner can turn confusion into a personal curriculum.

The pattern is the same: do not compete with AI in the visible layer where everything is cheap. Use AI to help you climb into the layer where your reality becomes structured, testable, and reusable.

## The Door Is Still Yours

The comforting story says humans will keep the "creative" work and machines will do the boring work.

I do not trust that story. Machines are already good at many things we used to call creative. And many things we call boring are actually where responsibility hides.

The stronger story is this: machines will keep eating what can be made visible. So the human job is not to guard a romantic mystery called creativity. The human job is to keep moving toward the part of reality that has not yet been made explicit, then make enough of it explicit that machines can help without taking over the judgment.

That is a more demanding future, but also a better one.

It means the valuable person is not the one who refuses AI, and not the one who blindly generates the most output. The valuable person is the one who can stand inside a messy private reality and turn it into a working system without betraying what made it private in the first place.

AI can help you write, code, search, summarize, translate, test, and automate.

But it cannot automatically know what your world means.

That door still has to be opened from the inside.

[^1]: SWE-bench describes the benchmark as testing whether AI systems can solve real GitHub issues by generating patches that pass tests: https://www.swebench.com/original.html
[^2]: Cognition's 2024 SWE-bench technical report reported Devin resolving 79 of 570 sampled issues, a 13.86% success rate: https://cognition.ai/blog/swe-bench-technical-report
[^3]: The working paper "Writing Code vs. Shipping Code" reports large gains in commits that attenuate to smaller gains in projects and releases: https://lmusolff.com/
