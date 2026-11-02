# Daily AI News Digest

> 发布日期:2026-11-02 · 类型:AI 热点日报

---

## 1. LongCat-2.5 targets longer agent tasks

Meituan's LongCat team has released LongCat-2.5, a native multimodal model designed for extended agent tasks. It has 1.6 trillion total parameters, with roughly 48 billion activated per token, and builds on its predecessor's visual understanding and agent coding capabilities. Combining those capabilities in one model could make it useful for workflows that involve both images and code. The announcement alone does not establish how reliably it will perform on a particular task; that requires evaluation in the intended setting. [Source](https://www.ithome.com/1/020/873.htm)

## 2. GDPx measures agents across professional domains

SemiAnalysis and 14 specialist reinforcement-learning environment partners have introduced GDPx, a benchmark spanning 11 fields, including chip design, cybersecurity, biology, finance, law and software engineering. The report's headline says the best model scored 12%. The benchmark is relevant because an agent that performs well on a general test may still struggle with a demanding professional task. Readers should interpret the reported score in the context of GDPx's own tasks and scoring method, rather than as a universal measure of AI capability. [Source](https://newsletter.semianalysis.com/p/gdpx-measuring-frontier-model-capabilities)

## 3. DeepSeek releases a coding-agent prototype

The DeepSeek Harness team has released dsh-superagent v0.1.0 under the MIT license. The coding-agent prototype is designed for a single GitHub repository: it can listen for GitHub requests and, optionally, Feishu requests, then create tickets for parallel work. The project offers a concrete example of how an agent system can divide incoming development work among concurrent tasks. It is an early prototype, so its usefulness and reliability still need to be assessed against the requirements of a real repository. [Source](https://www.marktechpost.com/2026/11/01/deepseek-dsh-superagent-router-worker-coding-agent/)

## 4. EditAgent uses measurements to assess image edits

Adobe Research and the University of California San Diego propose EditAgent, a system that breaks an editing request into steps and generates candidate results in parallel. A language model then compares the candidates using evidence that includes close-ups, change maps, and brightness and color measurements. The approach matters because an image-editing agent needs a way to judge what actually changed, not just restate the user's request. The report describes a research method; it does not establish that the system is available as a finished product. [Source](https://the-decoder.com/adobe-is-testing-how-well-ai-agents-can-use-editing-tools-like-a-photoshop-professional-would/)

## 5. StreamVibe explores when a video assistant should speak

Google and collaborating researchers have introduced StreamVibe to study when a video assistant should offer help. The system is intended to distinguish explicit requests from needs that are unstated or change during a task. The researchers report improvements in response timing and quality, while also finding that tested models generally struggled more with timing after videos exceeded five minutes. That limitation matters for practical use: even a helpful suggestion can interrupt work if it arrives at the wrong moment. [Source](https://the-decoder.com/google-wants-video-ai-to-understand-what-people-need-as-they-workgoogle-researchers-are-teaching-a-video-assistant-when-to-offer-help/)

## 6. AI companies adopt a training-crawl opt-out standard

OpenAI, Google, Microsoft and Anthropic have announced adoption of a standard intended to let publishers express a preference against AI training crawls to multiple companies at once. The proposed mechanism is integrated into a website's robots.txt file. For publishers, a common expression of preference could reduce the work involved in managing requests from different AI companies. Its practical significance will depend on how broadly the standard is adopted and how consistently participating crawlers honor those preferences. [Source](https://www.ithome.com/1/020/837.htm)

## 7. Aramco plans to acquire 49% of HUMAIN

HUMAIN says Saudi Aramco will acquire a 49% stake in the AI company, while Saudi Arabia's Public Investment Fund will retain 51%. Aramco plans to contribute key AI assets and approximately 9.9 billion Saudi riyals, with the aim of using HUMAIN's infrastructure to bring advanced AI capabilities into industrial applications. The planned transaction connects investment in AI infrastructure with a large industrial user's application plans. The announcement describes the intended investment and ownership structure; it does not itself demonstrate future results. [Source](https://www.ithome.com/1/020/863.htm)

## 8. HackerTube turns historical comments into video recommendations

HackerTube is a project that used Claude to identify 6,454 repeatedly recommended videos from roughly 43 million Hacker News comments spanning 20 years. It illustrates how a model can help organize a large collection of public discussion into a browsable set of resources. The selection is based on recommendations found in comments, however, so inclusion should not be treated as independent verification of a video's quality or accuracy. The reported project took approximately two hours to build. [Source](https://x.com/karpathy/status/2116957135661945283)

Which of these developments would be most useful to test in your own work?
