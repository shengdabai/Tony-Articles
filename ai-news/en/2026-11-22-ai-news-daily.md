# AI News Digest | Inference Privacy, Local Models, and GPU Verification

> 发布日期:2026-11-22 · 类型:AI 热点日报

---

## OpenRouter tightens zero data retention eligibility

OpenRouter says it removed three inference providers and revoked zero data retention eligibility for 125 endpoints after security researchers reported data handling problems at some providers. The company says it found no evidence that OpenRouter itself was compromised. The response matters for teams that use a single gateway to reach several model providers. The endpoint that actually processes a request determines which provider’s retention policy applies, so a change in endpoint eligibility can affect whether an existing route still meets a team’s requirements for sensitive data. [source](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/)

## Signal restricts screen capture on mobile

Signal reportedly updated its iOS and Android apps to block in-app screenshots and screen recordings by default. The change aims to reduce the chance that system-level AI assistants can read private conversations through the screen without the user’s knowledge. It addresses a stage of the conversation that matters even when messaging is encrypted. Once a device displays a message, its contents can potentially enter a separate system through screen capture. The default changes how the app handles that exposure while the message is on screen. [source](https://www.ithome.com/1/030/517.htm)

## TensorLean checks compiled GPU kernels

Researchers from Columbia University and CertiK introduced TensorLean, a framework that uses the Lean proof assistant to verify GPU kernels at the PTX instruction level. It can check for conflicting memory accesses, prove termination, verify that outputs fall within a specified tolerance, and check that designated memory stays unchanged. This gives developers a way to assess whether compiled instructions satisfy the mathematical requirements of a tensor operation. A proof can cover cases that individual test runs miss, provided the specification captures the behavior the application requires. [source](https://www.marktechpost.com/2026/11/21/columbia-certik-tensorlean-formal-verification-gpu-kernels/)

## Thinking Machines releases Inkling 2 Mini weights

Inkling 2 Mini has 26.4 billion parameters, with roughly 3.4 billion active per token. The model reuses some of its layers during processing, and the reported weight file is about 20 GB. The release coverage says the model can run on a Mac with 32 GB of memory. That gives teams with existing hardware a way to assess local inference before buying dedicated equipment. For an application that keeps inputs on the device, the practical test is whether response time and memory use remain acceptable on its actual workload. [source](https://www.marktechpost.com/2026/11/21/thinking-machines-inkling-2-mini-looped-transformer/)

## Smart glasses put exam screening under scrutiny in South Korea

South Korea’s education minister reportedly resigned after a controversy over measures to prevent AI-assisted cheating on the national college entrance exam. Exam centers assigned staff to check for AI glasses. Authorities identified 111 candidates carrying prohibited smart devices, including one case of cheating with smart glasses. The distinction between carrying a prohibited device and using one to cheat matters for exam design. The two counts describe different outcomes, and tracking them separately can help administrators evaluate checks at the entrance and supervision inside the exam room. [source](https://www.ithome.com/1/030/558.htm)

## ByteDance researchers test a three-step training process

ByteDance and researchers from several US universities published a paper arguing that a model can be trained in three steps. They released an open model that they describe as competitive to support that argument. The result gives other teams a concrete process to test. As training pipelines accumulate stages, reproducing them becomes more expensive and isolating the contribution of each stage takes more work. A shorter process can make those comparisons easier and help researchers determine whether the approach holds across other models and workloads. [source](https://the-decoder.com/bytedance-argues-most-ai-training-phases-are-unnecessary-and-backs-it-up-with-a-competitive-open-model/)

## Amazon reportedly nears a deal for Decart

Amazon is reportedly close to acquiring AI startup Decart for about $7.5 billion, compared with Decart’s most recent reported valuation of $4 billion. The deal remains unconfirmed. Decart received early access to Trainium3, and Amazon claims the chip runs Decart’s real-time video model four times as fast as GPUs at half the cost. Those figures reflect a vendor comparison for a specific workload. The reported deal matters because the economics of a real-time video service depend on how the model and chip perform together under the service’s latency and cost requirements. [source](https://x.com/rohanpaul_ai/status/2124294348712092061)

If your application handles sensitive data, would you first verify the cloud endpoint’s retention policy or test whether a local model meets your latency requirements?
