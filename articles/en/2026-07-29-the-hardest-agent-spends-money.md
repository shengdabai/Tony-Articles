# The Hardest Agent Spends Money

> 发布日期:2026-07-29 · [中文](../zh/2026-07-29-最难的Agent是那个会花钱的.md) | [English](../en/2026-07-29-the-hardest-agent-spends-money.md)

---

For the past year, the loudest AI story has been the coding agent.

That makes sense. Code is a beautiful place for agents to arrive first. The environment is textual. The work can be decomposed. The toolchain already has compilers, tests, logs, package managers, version control, and rollback. A coding agent can be wrong in public. It can break a test, read the error, patch the file, and try again. Even when the agent fails, the failure often leaves evidence.

But today’s notes pointed to a rougher frontier.

The next difficult agent is not the one that writes code. It is the one that spends money.

A marketing agent sounds, at first, like a copywriting machine. Give it a product, ask for ten hooks, twenty headlines, three short videos, a few ad variations, maybe a landing page. That is useful, but it is not the real shift. The real marketing agent is not a content generator. It is a growth loop.

It studies real users, turns the findings into creative, sends that creative into the world, pays for distribution, reads the performance data, kills what fails, amplifies what works, and repeats.

That last part changes everything.

When an agent writes code, the cost of a bad guess is often a failed build, a broken branch, or a few hours of cleanup. When an agent runs marketing, a bad guess can burn budget, damage trust, confuse customers, violate platform rules, or teach the system to optimize for a metric that makes the business worse.

This is why marketing is a harder interface than code.

Code mostly argues with machines.

Marketing argues with markets.

## Growth Is Not a Prompt

The naive version of AI marketing is easy to imagine: ask a model for better ads.

That will become table stakes. The interesting work is not asking for better ads. The interesting work is building a loop where better or worse has a meaning outside the model.

McKinsey estimated in 2023 that generative AI could add $2.6 trillion to $4.4 trillion in annual economic value, and that roughly three quarters of the value would fall across customer operations, marketing and sales, software engineering, and R&D.[^1] The giant number is not the useful part. Giant numbers are usually too large to think with.

The useful part is the clustering.

Marketing and sales sit next to software engineering because both are becoming more system-shaped. Software is no longer only written by people typing code into an editor. It is increasingly planned, generated, tested, reviewed, deployed, observed, and repaired through loops. Marketing is moving in the same direction: research, creative, launch, measurement, budget allocation, iteration.

But marketing has a brutal difference.

In software, the compiler does not have an opinion about your brand. The test suite does not get tired of your message. The dependency manager does not change behavior because your competitor launched a discount campaign. A market is messier. People have moods. Platforms have incentives. Competitors react. Attribution is partial. A campaign can look successful while training the wrong customers to click for the wrong reason.

So the question is not, "Can AI make marketing assets?"

Of course it can.

The better question is: can a human design a growth loop that AI can run without quietly making the business stupid?

## The Infrastructure Is Already Half Built

This is not science fiction.

The advertising platforms have been moving in this direction for years. Meta’s Marketing API gives developers a programmatic way to create and manage campaigns, ad sets, ads, and reporting workflows.[^2] Google’s Performance Max is officially described as a goal-based campaign type that uses Google Ads inventory from a single campaign and optimizes toward conversion goals across channels.[^3]

In other words, the rails already exist.

You can create campaigns through code. You can pull performance data. You can automate bidding and budget decisions inside platform constraints. You can generate creative. You can connect customer data, product data, web analytics, and campaign results. The missing piece is not imagination. It is control.

This is where many people will get the order wrong.

They will see the demo and ask for full automation.

The better builder asks for a smaller, harder thing: reliable automation.

Reliable automation has inputs that are clean enough to trust. It has permissions narrow enough to survive mistakes. It has human gates where the cost of error is high. It has logs that let you reconstruct what happened. It has a budget ceiling. It has a kill switch. It has a definition of failure written before the system starts spending.

A growth agent without these things is not an employee.

It is a slot machine with a dashboard.

## Money Makes the Feedback Real

There is one reason marketing agents are exciting despite the mess: money makes feedback real.

A lot of AI work gets stuck in taste theater. The answer sounds good. The interface looks polished. The strategy document feels complete. Everyone nods. Nothing has touched reality yet.

Marketing is harder to fake. Not impossible, but harder.

Someone clicked or did not click. Someone bought or did not buy. A cost went up. A conversion rate went down. A cohort retained or disappeared. A message brought qualified users or cheap noise. The loop may be noisy, but it is not imaginary.

This is why growth work matters for small teams and one-person companies. The hard part of building is no longer only "can you make something?" AI has pushed that question downward. More people can now build a prototype, a tool, a page, a lesson, a small app, or a service package. The next wall appears immediately after creation:

Can anyone find it?

Can the right people understand it?

Can trust form quickly enough?

Can the offer survive contact with a real buyer?

Can the system learn from a failed attempt without turning the founder into a full-time dashboard watcher?

That last question is the real promise of a marketing agent. Not "press a button and get growth." That is fantasy. The real promise is that a small operator can build a loop that keeps learning while the human stays focused on judgment.

The human should not be manually dragging every lever forever. But the human also should not disappear.

The human moves upward.

Goal. Constraint. Taste. Ethics. Budget. Positioning. Customer understanding. Exception handling.

These are not decorative human touches. They are the control layer.

## The Dangerous Metric Will Look Like Success

The scariest failure will not look like failure at first.

The obvious failures are easy. The ad spends money and gets no conversions. The creative is ugly. The platform rejects it. The cost per acquisition is absurd. These failures hurt, but at least they announce themselves.

The dangerous failure is when the metric improves while the business weakens.

The agent finds a cheaper audience that will never retain. It writes more aggressive copy that lifts clicks and lowers trust. It learns that discounts drive conversion, so it trains customers to wait. It optimizes for leads and floods the sales process with unqualified names. It discovers that controversy produces attention, and slowly turns the brand into something the founder would not have chosen consciously.

This is why "data-driven" is not enough.

Data does not tell you what kind of company you are willing to become. Data does not know which customers you should refuse. Data does not understand when attention is too cheap because it is purchased with dignity, clarity, or long-term trust.

The market is a judge, but it is not the only judge.

A healthy marketing agent needs several judges at once:

- performance metrics, because sentiment without revenue is theater;
- brand constraints, because revenue without trust becomes debt;
- customer quality, because not every buyer improves the business;
- budget limits, because learning should not become bleeding;
- human review, because some decisions are too identity-shaping to delegate.

The point is not to slow everything down. The point is to make speed survivable.

## The New Growth Role

If marketing agents become real, the growth role changes.

The old operator spent a lot of time doing tasks: writing variations, checking dashboards, changing bids, building reports, watching accounts, copying numbers into slides. Much of that work can be compressed by AI.

But compression does not remove responsibility. It exposes it.

The new growth person is less like a pair of hands and more like a systems designer. They decide what the loop is allowed to optimize. They define the audience boundary. They choose what counts as a meaningful conversion. They inspect anomalies. They ask whether a winning campaign is attracting the right kind of customer. They keep the system from confusing "more activity" with "better business."

This is close to the broader AI lesson I keep returning to: AI should make people stronger, not lazier.

If a marketing agent only lets a mediocre operator spray more mediocre content across more channels, it has made the world noisier. If it helps a serious operator test sharper hypotheses, preserve evidence, learn from the market, and spend attention on judgment instead of repetition, it has made the person stronger.

The same tool can do both.

The difference is the loop around it.

## Build the Brake Before the Engine

I do not think the first useful marketing agent for most small teams will be fully autonomous.

It will probably be boring in the right way.

It will read customer language from approved sources. It will generate hypotheses, not final truth. It will propose creative, but wait for approval before publishing. It will start with tiny budgets. It will pause campaigns automatically when spend crosses a threshold without enough signal. It will summarize what changed, what it tried, what it learned, and what it recommends next. It will keep a memory of failed angles so the team does not pay to rediscover the same lesson every month.

That sounds less exciting than "an AI marketing department."

It is also much closer to what trust looks like.

Every powerful automation should be introduced with a question that sounds almost anti-ambitious:

What must this system never do?

Never spend beyond this ceiling. Never publish without approval in these categories. Never change positioning without review. Never target this kind of customer. Never hide uncertainty. Never treat a short-term metric as proof of long-term value.

These are not limitations on intelligence.

They are the skeleton that lets intelligence stand up.

The future of AI growth work will not belong to the people who can generate the most assets. Asset generation is becoming cheap. It will belong to the people who can connect user truth, creative judgment, platform mechanics, business economics, and human boundaries into a loop that compounds without losing its soul.

That is a very different skill from "prompting."

It is closer to building a small institution.

One person may run it. A swarm of agents may do the repetitive work. But the institution still needs law, memory, budget, rituals, review, and consequences.

This is why the hardest agent spends money.

Money forces the system to meet reality. It makes learning expensive enough to matter. It reveals whether the offer is alive. It also punishes sloppy automation quickly.

So I am not waiting for the magic marketing agent that grows a company while the founder sleeps.

I am more interested in a humbler machine: one that can spend a little, learn honestly, stop quickly, preserve evidence, and make the human sharper after every round.

Growth is not a button.

Growth is a loop with a budget, a memory, and a conscience.

Build those first.

Then let the agent run.

[^1]: McKinsey, "The economic potential of generative AI: The next productivity frontier," 2023. https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier
[^2]: Meta for Developers, "Marketing API." https://developers.facebook.com/documentation/ads-commerce/marketing-api
[^3]: Google Ads Help, "About Performance Max campaigns." https://support.google.com/google-ads/answer/10724817?hl=en
