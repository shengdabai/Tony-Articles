# The First Project Is Infrastructure

> 发布日期:2026-08-04 · [中文](../zh/2026-08-04-第一个项目不是产品是基础设施.md) | [English](../en/2026-08-04-the-first-project-is-infrastructure.md)

---

The first project is usually judged in the wrong way.

We ask: Did it work? Did it make money? Did it get users? Did it become the thing we imagined when the idea first looked bright?

Those are fair questions. A product eventually has to meet the world. It cannot live forever as a private exercise with beautiful folders and no customers.

But for a solo builder, especially in the age of AI, the first project has another job that is easier to miss:

It should become infrastructure for the second project.

That sounds less exciting than "launch a product." It also sounds slower than the fantasy sold by many AI stories: describe the app, let the model code it, publish it, wait for the money.

But the fantasy hides the part where most people actually lose. They do not lose because AI cannot generate code. They lose because every attempt begins from zero.

A new idea means a new folder, a new stack, a new payment setup, a new deployment checklist, a new analytics setup, a new SEO plan, a new launch list, a new set of mistakes, and a new emotional collapse when the first week is quiet.

That is not building.

That is amnesia with a domain name.

## Code Is Cheaper, Continuity Is Scarce

The easy story is that AI has made building cheap.

There is truth in it. GitHub's Octoverse 2024 report said public generative AI projects on GitHub grew 98% year over year, and contributions to those projects rose 59% in 2024.[^1] SWE-bench, one of the better-known software engineering benchmarks, evaluates models on real GitHub issues, and its Verified subset contains 500 problems that real software engineers confirmed were solvable.[^2]

So yes, the machine is getting better at turning intent into code.

But code is not the whole product.

The product also includes: how a user finds you, what they understand in the first ten seconds, whether the result solves one painful job, whether the cost structure works, whether the payment path survives disputes, whether the logs tell you what broke, whether you can update without panic, and whether a failed experiment leaves anything useful behind.

Those are not glamorous. They do not look like a viral demo. They look like small checklists, reusable components, boring notes, naming conventions, recovery plans, saved prompts, launch records, customer questions, and a list of websites where real users might actually discover the thing.

But that is exactly where the compounding begins.

AI lowers the cost of producing another version. It does not automatically lower the cost of remembering what happened last time.

If a builder does not build memory into the process, AI can make the forgetting faster.

## The First Project Has Three Outputs

A beginner thinks the first project has one output: the product.

A more experienced builder tries to leave three outputs.

The first is a template.

Not a perfect framework. Not a giant internal platform. Just a repeatable starting point that knows your defaults: pages, auth, payment, database, deployment, analytics, error reporting, privacy text, update notes, and the small UI pieces you always need but hate rebuilding.

The value of a template is not that it saves typing. AI already saves typing.

The value is that it saves decisions.

Every project contains hundreds of tiny choices. Which form library? Where do logs go? How do errors appear to the user? What happens when an API call fails? What does the empty state say? How do you name environment variables? How do you test a payment flow without touching real users?

If none of these choices are preserved, each new project burns attention before the real problem even begins.

The second output is a channel map.

Most first projects die in silence. The builder ships, posts once, refreshes analytics, and quietly learns that the internet does not care about effort.

That lesson is painful, but it is also useful if captured correctly.

Where did the first users come from? Which communities ignored the post? Which directories accepted the submission? Which search terms seemed real but brought the wrong people? Which article, comment, email, or message produced an actual user instead of a polite like?

A channel map is not a magic growth hack. It is a memory of contact with reality.

The third output is a risk map.

This is the least romantic and maybe the most valuable.

What broke? Which dependency was unreliable? Which cost could explode? Which policy was unclear? Which account, API, or payment path had no backup? Which part of the product was legally, operationally, or emotionally too heavy for one person to carry?

The first project teaches you where the floor is weak.

If you write that down, the second project starts wiser.

If you do not, the second project merely starts newer.

## Failure Should Leave Assets

The brutal truth is that many first projects will not work.

Not because the builder is stupid. Not because the idea was shameful. Often the market is too small, the channel is wrong, the timing is bad, the value is unclear, the product is too hard to explain, or the person simply did not yet have enough repetitions.

The question is not how to guarantee success.

The better question is: if this fails, what remains?

If the answer is "nothing," the project was a lottery ticket.

If the answer is "a deployment checklist, a working payment pattern, five reusable pages, a list of launch channels, three hard lessons about user behavior, and a clearer sense of what I should not build next," then the project was also a training facility.

This is where AI changes the psychology of practice.

Before AI, building was expensive enough that people often tried to make the first attempt perfect. They spent too long choosing the stack, polishing the brand, redesigning the homepage, and imagining future scale.

Now the danger is different. Building feels so cheap that people start too many things without learning from any of them.

Both are forms of waste.

The old waste was over-preparation.

The new waste is under-digestion.

You do not need every project to win. You need every project to teach the next one how to begin.

## Give AI a Long-Term Job

One phrase from today's notes stayed with me: give the AI model a long-term job.

That is a better frame than "use AI to build an app."

A task-based AI waits for instructions. A long-term AI job accumulates context, constraints, defaults, and memory. It does not merely produce today's code. It helps turn today's friction into tomorrow's starting point.

After each project, ask the model to do work that is easy to skip:

What should become a template?

Which prompts were actually useful?

Which setup steps were repeated?

Which bugs appeared more than once?

Which assumptions about users were wrong?

Which distribution attempts created real signals?

Which parts should be deleted before they become clutter?

This is not glamorous AI. It will not impress anyone in a demo video. But it is the kind of AI that makes a person stronger.

It turns experience into structure.

It turns structure into speed.

It turns speed into more attempts.

And more attempts, if they are digested, become judgment.

That last condition matters. More attempts alone can also become noise. A person can launch ten things and learn almost nothing if each launch is treated as an isolated event.

The compounding only starts when the projects can talk to one another.

## The Hidden Opponent Is Reset

The enemy of the solo builder is not only competition.

It is reset.

Reset is what happens when every Monday starts from a blank page. Reset is what happens when lessons stay in memory instead of becoming defaults. Reset is what happens when a failed product is deleted before its bones are studied.

AI can make reset feel painless because it can always generate another beginning.

But beginnings are not the scarce resource.

Continuity is.

Google Cloud's DORA 2024 report made a useful point about AI in software teams: AI adoption can increase individual productivity, flow, and job satisfaction, but it can also hurt delivery stability and throughput if the surrounding system is weak. The same report emphasizes stable priorities, continuous learning, user focus, and strong engineering fundamentals.[^3]

That finding belongs far beyond large teams.

For a solo builder, the message is simple: personal speed is not enough. The system around the speed determines whether the speed becomes progress.

If AI helps you code faster but your projects leave no templates, no channel memory, no risk map, and no clearer judgment, you are not compounding. You are sprinting in circles.

If AI helps you preserve and reuse what each attempt taught you, even small projects begin to stack.

## The Real First Product

This changes how I think about a first project.

The visible product may be a small tool, a website, a public page, a newsletter experiment, a tiny automation, or a service prototype.

But the real first product is the builder's operating system.

Can you move from idea to test without chaos?

Can you ship a small version without pretending it is finished?

Can you find one real channel instead of waiting for the whole internet?

Can you watch a user fail and improve the path without taking it personally?

Can you keep the parts that should repeat and throw away the parts that should not?

Can you let a failed attempt pay rent by becoming infrastructure?

That is the point.

The first project does not have to become the business.

It has to raise the floor.

When the floor rises, the second project is not just another try. It begins with a little more code, a little more taste, a little more market contact, a little more patience, and a little less superstition.

That is how a person gets stronger without pretending to be lucky.

Not by asking AI to replace the work.

By asking AI to help the work remember.

[^1]: GitHub, ["Octoverse: AI leads Python to top language as the number of global developers surges"](https://github.blog/news-insights/octoverse/octoverse-2024/), October 29, 2024, updated October 28, 2025.
[^2]: SWE-bench project README, ["SWE-bench: Can Language Models Resolve Real-world Github Issues?"](https://github.com/SWE-bench/SWE-bench), including the August 13, 2024 note on SWE-bench Verified.
[^3]: Google Cloud DORA, ["Accelerate State of DevOps Report 2024"](https://dora.dev/research/2024/dora-report/).
