# Why AI Forecasts Need Loops, Not Arrows

> 发布日期:2026-09-08 · [中文](../zh/2026-09-08-很多 AI 预测，都错在只画了一根箭头.md) | [English](../en/2026-09-08-ai-forecasts-need-loops.md)

---

This morning, I put three predictions from the beginning of the year next to each other.

AI will kill SaaS. AI will reduce the number of programmers. AI will make degrees less valuable.

Each sentence sounded reasonable. If software becomes cheap to build, why keep paying for it? If one programmer can produce ten times as much, why hire as many programmers? If AI can help anyone create polished work, why care about credentials?

Yet the signals I collected over the following months did not move neatly in those directions. Established software companies were absorbing AI instead of simply disappearing. Demand for some kinds of technical work was growing even as entry-level work came under pressure. And when résumés, assignments, and portfolios became easier to polish, employers did not stop screening. They searched for harder-to-fake signals of trust.

I do not think the lesson is that the opposite predictions must now be true. Six months of evidence cannot settle a decade-long transition.

The more useful lesson is that all three predictions made the same structural mistake: they drew one arrow.

AI lowers the cost of producing software, therefore software companies shrink. AI raises output per programmer, therefore fewer programmers are needed. AI makes polished work cheap, therefore credentials lose value.

The first arrow may be correct. The conclusion can still be wrong, because the people and institutions at the other end of the arrow do not stand still.

## A tool changes the system that uses it

When a technology makes an activity cheaper, people often do more of that activity. When it makes one signal easy to imitate, decision-makers search for another signal. When it removes one bottleneck, work piles up at the next one.

That turns an arrow into a loop.

Consider programming. A coding assistant may reduce the time needed to generate a working block of code. But cheaper code makes previously uneconomic projects worth attempting. More projects create more integration, review, security, maintenance, and product decisions. The scarce resource moves. It does not necessarily disappear.

This is why measurements that appear to conflict can all contain part of the truth. In a controlled GitHub experiment, 95 professional developers were asked to build the same JavaScript HTTP server; the group using Copilot completed the task [55 percent faster](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/). In a different randomized study, 16 experienced open-source developers worked on 246 real tasks in repositories they had known for years. With early-2025 AI tools, they took [19 percent longer](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/).

Neither result tells us that AI “works” or “does not work.” They describe different loops. A bounded greenfield task has little inherited context and a clear finish line. A mature repository contains conventions, hidden dependencies, review expectations, and the cost of checking plausible mistakes.

By February 2026, the same independent research group believed newer tools were probably speeding developers up, but it refused to give a confident number. Developers who valued AI most were increasingly unwilling to join a study that sometimes prohibited it, while parallel agent use made time harder to measure. The researchers explicitly called the new estimate [an unreliable signal](https://metr.org/blog/2026-02-24-uplift-update/).

I find that intellectual honesty more valuable than another dramatic percentage. The tool changed. The users adapted. The experiment itself became harder to run. Even the act of measurement had entered the loop.

## Speed does not vanish; it arrives somewhere else

In one case I examined today, a team could produce an extraordinary amount of code with agents, only to discover that review and quality control could not absorb it. A commercial telemetry report covering 22,000 developers across 4,000 teams found larger pull requests alongside more bugs, incidents, churn, and a [fivefold increase in median review time](https://www.faros.ai/research/ai-acceleration-whiplash). It is a vendor report, not a universal law, but the pattern is worth testing in any team using AI heavily.

The naive metric is lines of code produced. The system metric is time from a real need to a change that survives review, reaches users, and keeps working.

If generation becomes ten times faster while review becomes the queue, celebrating generation is like widening the entrance to a bridge while leaving the exit at one lane. More cars enter. The traffic jam looks like growth until you ask how many arrived.

The same thing happens outside software.

If AI makes every job application cleaner, the immediate result is better-looking applications. The next result is that appearance becomes less informative. Employers then spend more on verification, referrals, work trials, or trusted records. AI may weaken one credential while strengthening the value of another. “Credentials will disappear” misses the response of the evaluator.

If AI reduces the cost of building a small software product, one project may need fewer hours. But thousands of people and small firms that could not previously afford software can now commission it. Demand expands into places where no software project existed before. The current U.S. Bureau of Labor Statistics projection does not prove what will happen, but it is a useful counterweight to the simple replacement story: it projects software-developer employment to grow [15.8 percent from 2024 to 2034](https://www.bls.gov/opub/ted/2026/artificial-intelligence-information-technology-and-employment-2024-34.htm), partly because more products will contain software.

This is not a promise that every job will be protected. The same projection expects several administrative occupations to contract as AI spreads. A task can disappear while demand for an occupation grows; an occupation can shrink while its industry expands. “Will AI replace programmers?” mixes at least three different units—tasks, roles, and total employment—and then asks for one yes-or-no answer. Before drawing a loop, we have to say which level we are trying to predict.

Efficiency changes price. Price changes behavior. Behavior changes demand. Demand creates a new bottleneck. That is the loop the straight-line forecast leaves out.

## This has happened before, but history is not a shortcut

Economists studying general-purpose technologies noticed a similar shape long before generative AI. Electricity and computers did not create their full productivity gains the moment they appeared. Organizations first had to redesign processes, develop complementary tools, and teach people new ways to work. During that investment period, measured productivity could stagnate or even fall before rising later. Researchers described this as a [productivity J-curve](https://www.nber.org/reporter/2024number1/economics-generative-ai).

The useful connection is not “AI is exactly like electricity.” It is not. AI changes faster, works through language, and can participate in decisions in ways an electric motor cannot.

The connection is narrower: a general-purpose capability only becomes productive through complements. Installing the tool is the beginning of system redesign, not the end of it.

This also explains why both optimism and pessimism can be early. The optimist sees the new capability and assumes the surrounding system has already adapted. The pessimist sees the temporary disorder and assumes adaptation will never happen.

Both freeze a moving system.

## A four-box test for the next big AI claim

I now use a simple test when I encounter a confident prediction. It takes five minutes and fits on one page.

- **Direct effect and level:** What exactly becomes cheaper, faster, or easier—a task, a role, a product, or an entire market?
- **Behavioral response:** What will users, workers, competitors, and institutions do because of that change?
- **New bottleneck:** When the old constraint weakens, where will time, trust, money, or risk accumulate next?
- **Observable reversal:** What evidence, by what date, would show that my conclusion is moving in the wrong direction?

Take the claim “AI will reduce the need for programmers.” The direct effect is faster code generation. The response may be more software projects and much larger batches of changes. The new bottleneck may be problem definition, review, integration, or accountability. An observable reversal might be that total technical hiring rises while the mix of roles changes.

This method does not guarantee a correct prediction. Feedback loops can easily become a clever way to explain anything after it happens. That is why the fourth box matters. Write the expected signal and the date before reality answers. Otherwise, “systems are complex” becomes an elegant excuse for never being wrong.

My position is simple: in the AI era, judgment is not the ability to produce the boldest final answer. It is the ability to keep a model of reality open long enough for reality to push back.

The next time someone says AI will eliminate a product, a profession, or an institution, do not begin by asking whether the first arrow is plausible. It probably is.

Ask what moves after the arrow lands.
