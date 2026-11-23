# Daily AI News | Proof Checking, Agent Evaluations, and Open Medical Models
> 发布日期:2026-11-23 · 类型:AI 热点日报

---

## A proof of the Riemann hypothesis reportedly passes formal verification

IT Home reported that a mathematician interviewed about the result considered the proof developed by a mathematician working with Claude to be correct, citing formal verification in Lean and independent checks. Lean is a proof assistant that checks whether a formal argument follows from its stated definitions and assumptions. Researchers can rerun that check themselves. A further task is to explain the argument in a form other mathematicians can read, so they can see which ideas do the work and where those ideas might apply elsewhere. [source](https://www.ithome.com/1/030/677.htm)

## Coding agents finish fewer than one in ten tasks at a simulated company

The Decoder reported on an experiment that placed coding agents in a simulated software company with coworkers, project boards, and chat histories. Claude Opus 5.5 and GPT-6 Astra each fully completed fewer than one in ten assignments in that setting. The figure describes performance in the simulation. For teams evaluating agents, the study gives a reason to measure complete assignments that require finding context and handling handoffs. A code change can pass its tests while the wider assignment still has outstanding work. [source](https://the-decoder.com/ai-coding-agents-ace-isolated-tests-but-complete-fewer-than-one-in-ten-tasks-in-a-simulated-workplace/)

## METR warns that safety evaluations may struggle to keep pace

In its November update on AI capabilities, research organization METR warned that public evidence leaves open the possibility of a sharp acceleration in AI research over the next few years. The concern is that experts could have too little time to evaluate new systems reliably as capabilities improve. The timing matters for release decisions. If a system changes materially between assessments, a release schedule needs to account for the time it takes to repeat the relevant tests and interpret the results. [source](https://the-decoder.com/ai-is-getting-better-faster-than-experts-can-reliably-test-whether-new-systems-are-safe-metr-warns/)

## Ant announces an open-source family of health models

Ant announced that it would open-source a family of health models spanning language, real-time audio and video, risk prediction, and safety safeguards. The company says the lightest version can run on a single laptop. The release could give healthcare teams more options for testing models locally on specific tasks. An imaging team, for example, could check how often draft reports omit a finding present in the original image. Deployment requirements and performance on that task would need to be measured for the version under consideration. [source](https://www.ithome.com/1/030/784.htm)

## Amazon is reportedly in talks to buy Decart for about $7.5 billion

IT Home, citing the Financial Times, reported that Amazon was in advanced talks to buy the AI startup Decart in a deal valued at around $7.5 billion. The report put the earliest possible agreement at the start of the week and said the talks could still fall apart. If a deal is signed, customers will have a concrete question to track as terms emerge. They will want to know whether Decart's products will remain available on their own or be sold through Amazon's services. [source](https://www.ithome.com/1/030/797.htm)

## Gemini API previews on-demand tool definitions

Google is previewing Tool Retrieval in the Gemini API. A model initially receives each tool's name and a short description, then retrieves the full parameter definition when needed. Applications with large catalogs can use that approach to spend less of each request on definitions the model may never use. The practical test is whether the descriptions reliably point the model to the right tool, particularly when two tools sound similar but accept different inputs or produce different results. [source](https://www.marktechpost.com/2026/11/22/google-gemini-api-tool-retrieval/)

## Perplexity launches an API for monitoring web changes

Perplexity's Monitor API checks web content on a schedule and sends a webhook, an automated message to another application, when it detects a relevant change. A team that routinely checks for revised public notices could use the API to turn those checks into notifications. The benefit depends on how promptly the service catches meaningful revisions and how often it flags irrelevant changes. Those two measures can help a team decide whether to route the alerts into an existing workflow. [source](https://the-decoder.com/perplexitys-new-monitor-api-turns-web-search-from-a-one-off-query-into-a-nonstop-watchdog/)

If you could add one acceptance check to an AI workflow this week, what would you measure and what would count as a pass?
