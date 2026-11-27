# AI News Digest | Chip Shipments, Data Rules, and Creative Tools

> 发布日期:2026-11-27 · 类型:AI 热点日报

---

## Nvidia reportedly pauses server shipments to four Southeast Asian countries

TechCrunch, citing The Wall Street Journal, reports that Nvidia told manufacturing partners to pause server shipments to Malaysia, Singapore, Thailand, and Indonesia while it assesses whether regional partners meet U.S. export requirements. The reported pause concerns server deliveries. For cloud providers awaiting new equipment, the immediate question is when they can bring additional capacity online. Customers planning around that capacity may also need to revisit project schedules, especially if they were counting on new GPUs for a launch or a training run. [source](https://techcrunch.com/2026/11/26/nvidia-hits-pause-on-chip-shipments-to-southeast-asia/)

## China seeks public comment on data rules for AI

China’s National Data Administration opened a consultation on draft rules that support using lawfully obtained data for AI training and inference. The draft proposes clarifying how rights to hold, use, and commercially operate data can be exercised. It also encourages AI companies to pay for high-quality data and calls for controls on output risks, incident response procedures, and channels for user complaints. For teams acquiring datasets, the consultation provides a concrete set of questions about how they document permissions and who handles complaints once a system goes live. [source](https://www.ithome.com/1/033/054.htm)

## State attorneys general seek to block a sale of Character.AI chats

A coalition of 42 state attorneys general is trying to block the sale of user data in Character.AI’s Chapter 11 bankruptcy proceedings. The coalition alleges that a proposed auction would cover private chats from more than 21 million U.S. accounts, including more than 2.1 million accounts registered to minors. It also alleges that the proposed sale lacks safeguards. The dispute raises a practical question for anyone who shares sensitive information with a chatbot. How much control users retain over old conversations may depend on what happens to those records when a service changes hands. [source](https://www.theverge.com/policy/1042620/character-ai-sale-state-ags-block-selling-users-chats)

## OpenAI fixes GPT-6.2 usage accounting

OpenAI corrected an error that had applied an unintended discount to GPT-6.2 usage during the initial rollout, according to the report. For the same workload, users now reach their limits 40% faster on Astra and 25% faster on Sol than before the fix. The figures describe how quickly usage counts toward a cap. Teams that estimated how many jobs they could finish within an allowance during launch week may need to measure a representative batch again before scheduling longer runs or offering the same capacity to more users. [source](https://www.ithome.com/1/033/138.htm)

## Tencent releases DFly2 to accelerate text generation

Tencent open-sourced DFly2, a speculative decoding component that proposes upcoming tokens for the main model to verify. The component reuses the main model’s attention cache and selected context positions, so it can operate without maintaining a separate cache for its drafts. Tencent reports a peak speedup of 4.2 times for Hy4 flash in an individual test. For teams serving long prompts, the design is worth evaluating on their own traffic. Useful measurements would include generation speed and memory use when several requests run at once. [source](https://mp.weixin.qq.com/s/d1HMHrSEChCJiBRZ0tNOyg)

## Doubao Work adds an official Jianying video editing plugin

The desktop integration lets users describe editing tasks in a chat, such as trimming a talking-head video or adding subtitles. Users can request another pass in the conversation or open the resulting multitrack project in Jianying for manual adjustments. The plugin requires the latest version of Jianying. For a small production team, the editable project is a practical part of the release. An editor can use the initial cut as a starting point, then check whether a trim changed the meaning of a sentence or a subtitle needs correcting. [source](https://www.ithome.com/1/033/208.htm)

## Kimi offers free API credits to selected research teams

Moonshot AI opened applications for Kimi for Science, a program for research teams around the world working on theoretical or experimental projects in basic science and engineering. Selected teams can receive free API credits, access to the latest models, and opportunities for longer-term collaboration. The first application round closes December 8. For a group with a limited budget, credits could make it possible to run a small pilot, check whether the model’s outputs can be evaluated reliably, and estimate what a larger study would cost before committing its own funds. [source](https://x.com/Kimi_Moonshot/status/2126154696947871760)

If you could test one change from today’s digest next week, what would you measure to decide whether it merits a change to your workflow?
