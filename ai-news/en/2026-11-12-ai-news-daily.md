# AI Daily Digest: Models, Agents and Business Costs

> 发布日期:2026-11-12 · 类型:AI 热点日报

---

## 1. Runway releases Praxis-1 weights

Runway says it has made the weights of Praxis-1 available under the Apache 2.0 license. The 27-billion-parameter world-action model predicts video and actions together. The company reports a 46.2% success rate on NVIDIA RoboLab-120, above the other models listed in its comparison.

**Why it matters:** Open weights give researchers and developers another tool for studying how video and action predictions can work together. The benchmark result is a vendor claim; it does not by itself establish how the model will perform in real-world settings. Teams considering it will still need to evaluate the model against their own tasks and conditions. [Source](https://runwayml.com/news/company-news/praxis-1-is-now-available)

## 2. Google introduces a multimodal decisions API

Google has announced the Gemini Decisions API, powered by Gemini Decision 1. The service can evaluate text, images, audio, video and PDFs against up to 1,000 yes-or-no, multiple-choice or scoring questions in one request. Google describes an end-to-end latency of 150–250 milliseconds and an input limit of 256,000 tokens.

**Why it matters:** A service designed around fixed answer choices could support classification and evaluation workflows where an application needs structured decisions. The stated latency is a company claim, so users should measure speed and output quality with their own materials and workloads before relying on it. [Source](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)

## 3. OpenRouter outlines safeguards against agent loops

An OpenRouter tutorial explains how repeated tool failures can trap an AI agent in a loop. It proposes four layers of protection: detecting repeated loops, normalizing the parameters used to identify them, setting step and cost limits, and placing a credit limit on the API key.

**Why it matters:** An agent that keeps retrying a failed task can continue using tools and accumulating charges without producing a useful result. Multiple limits give developers ways to contain the duration and cost of that failure. The tutorial offers a practical framework for deciding when an automated task should stop. [Source](https://openrouter.ai/blog/tutorials/ai-agent-infinite-loop/)

## 4. Security firm alleges exposure in Grok-built apps

Security company Claroc reports that 35,578 of the 37,571 Grok-built apps it examined that were still online could be accessed without signing in. It links the finding to a publishing option that preselects access for anyone with the link, along with app subdomains that can appear in searchable passive DNS records.

**Why it matters:** A creator who assumes an app link is hard to discover may misunderstand the consequences of publishing it. The figures and explanation are allegations from a third-party security investigation and have not been independently confirmed here. They nevertheless identify a useful question for app creators: who can actually reach a published app? [Source](https://the-decoder.com/grok-built-apps-exposed-patient-data-plaintext-passwords-and-spacexsis-own-sales-pipeline/)

## 5. OpenAI revenue rises alongside operating losses

OpenAI’s third-quarter revenue rose approximately 50% from the previous quarter to $10 billion, according to reporting attributed to The Wall Street Journal and The Information. Its adjusted operating loss also increased, from $10.1 billion to $10.9 billion.

**Why it matters:** The reported figures put revenue growth and spending in the same picture. A larger revenue base does not on its own show that a company’s operations are moving toward profitability. These are media-reported figures, and the adjusted loss measure should be read on its stated terms. [Source](https://the-decoder.com/enterprise-sales-push-openais-quarterly-revenue-to-10-billion-though-it-still-trails-anthropic/)

## 6. Anthropic’s reported listing plans draw attention

Bloomberg reports that Anthropic is seeking up to $90.4 billion through an initial public offering and a private placement, targeting a fully diluted valuation of about $1.4 trillion. The report also says institutional orders have reached several times the shares on offer.

**Why it matters:** The proposed fundraising illustrates the scale of capital sought by a leading AI company and offers a case for watching how investors value the sector. The fundraising amount and valuation are reported targets, not final results; the outcome may differ. [Source](https://x.com/rohanpaul_ai/status/2120526677247939001)

## 7. a16z considers agents as a distribution channel

An a16z article proposes a business-to-agent, or B2A, economy. It argues that AI agents are moving beyond answering questions to completing tasks and making consumption decisions for users. The article also claims that agents already account for most web traffic.

**Why it matters:** If agents play a larger role in finding and selecting products, businesses may need to consider how clearly those agents can interpret product information. The traffic assertion is the article’s claim; it should not be treated as an independently established breakdown of all internet traffic. [Source](https://www.a16z.news/p/welcome-to-the-b2a-economy)

Which would be most useful for you to test first: model performance, agent cost controls, or a new way for agents to discover your product?
