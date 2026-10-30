# AI Daily · 2026-08-18

> 发布日期:2026-08-18 · 类型:AI 热点日报
>
> 中文版: [AI 圈过去 24 小时 · 2026-08-18](../zh/2026-08-18-AI圈过去24小时.md)

---

The strongest signal from the past 24 hours is that AI is moving beyond model capability into infrastructure redesign. Agents need hard security boundaries. Coding tools are moving into collaboration and deployment. Compute is being tied to land, power, and long-term customers. Robotics and open data pipelines are pushing intelligence out of the screen and into the physical world.

**1. Google uses ADK to show zero-trust agents, moving safety beyond the prompt**

Google Developers Blog published a zero-trust agent example built with Agent Development Kit and Gemini. The key point is blunt: system prompts are soft constraints, not a production security boundary. The proposed design puts three hard layers outside the LLM context: cryptographic signatures for state-changing writes, gVisor sandboxing for dynamically generated code, and deterministic semantic gateways for validating business rules. Why it matters: once an agent can issue refunds, modify databases, or execute code, it is no longer a chatbot. It is a component that mutates production state. The real engineering shift is from “trust the model to behave” to “assume the model can be tricked, and still keep the system contained.” [source](https://developers.googleblog.com/build-zero-trust-ai-agents-with-googles-agent-development-kit)

**2. Cursor launches Origin Code Hosting, extending AI coding tools into the collaboration layer**

Cursor's changelog introduces Origin Code Hosting as an early code-hosting capability with repositories, code browsing, pull requests, GitHub sync, and integrations with Vercel, Depot, and Buildkite. Why it matters: AI coding tools used to live mostly inside the editor. Now they are expanding into where code is hosted, reviewed, synchronized, deployed, and eventually handled by agents. For small teams, the product choice may become less about autocomplete quality and more about whether the tool gives them an end-to-end path from idea to running service. [source](https://cursor.com/changelog/origin-code-hosting)

**3. NVIDIA and SB Energy secure PORTS-Pike capacity, with OpenAI as the AI factory tenant**

NVIDIA's official blog says it is partnering with SB Energy to secure large-scale land, power, and shell capacity at the PORTS-Pike Technology Campus in Ohio for NVIDIA AI factories, with OpenAI as the tenant. The initial deployment is expected to provide 4.25 gigawatts of AI factory capacity, and NVIDIA frames the site as a long-lived location where successive generations of compute can be upgraded over time. A related X post points to the same official article. Why it matters: the center of AI competition is shifting from “who has the model” to “who can secure land, power, data centers, GPUs, and durable customer demand.” Stronger intelligence still has to run inside physical constraints. [source](https://blogs.nvidia.com/blog/securing-the-infrastructure-of-intelligence)

**4. Unitree says it will list on Shanghai's STAR Market on August 19**

IT Home reports, citing company announcements, that Unitree's shares will list on the Shanghai Stock Exchange STAR Market on August 19, 2026. The offering price is listed as RMB 150.80 per share, implying a market value of about RMB 60.993 billion, with proceeds directed toward intelligent robot model research, robot body development, new product development, and manufacturing capacity. Why it matters: humanoid robotics is not just another hardware category. It is where model capability, control systems, manufacturing, supply chains, and real-world feedback meet. Over the long run, robotics tests whether AI can turn data into action in the world. [source](https://www.ithome.com/0/990/812.htm)

**5. inclusionAI open-sources ConceptEdit, a data pipeline for image editing**

The inclusionAI GitHub repository presents ConceptEdit as an image-editing data generation project. Its pipeline has three stages: use a VLM to generate edit instructions, run the edits with FLUX, and use VQA evaluation to score, keep, discard, or recaption outputs. The repository also links to an arXiv paper, Hugging Face datasets and benchmarks, and is released under the MIT License. Why it matters: multimodal progress depends not only on model architecture, but also on high-quality, measurable, reusable data systems. Connecting generation, editing, and automated judging turns visual AI data production into something closer to a self-improving workshop. [source](https://github.com/inclusionAI/ConceptEdit)

**6. A guide to disabling intrusive AI shows why defaults are now a trust issue**

librarian.net updated a practical guide for people who want less intrusive AI in their technology environment. It covers products and platforms including Adobe, Android and Gemini, Apple Intelligence, Chrome, Edge, Firefox, Google Workspace, Slack, WhatsApp, and Windows 11 Copilot. Why it matters: this is not simply anti-AI sentiment. It is a product trust signal. The more AI features are inserted by default, the more users need clear switches, understandable permissions, and genuine control. AI that makes people stronger should put users in command, not force them to learn how to escape it. [source](https://www.librarian.net/notoai/)

**Today's takeaway:** The next stage of AI is not only about what models can say. It is about the security systems, toolchains, power contracts, data workshops, and user permissions that determine where models can safely act. The question worth asking is whether your current AI setup strengthens your work system or merely adds another unstable button inside it.
