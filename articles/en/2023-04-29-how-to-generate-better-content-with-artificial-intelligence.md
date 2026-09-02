# How to Generate Better Content with Artificial Intelligence

> Published: 2023-04-29 · [中文](../zh/2023-04-29-%E5%A6%82%E4%BD%95%E7%94%A8%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E7%94%9F%E6%88%90%E6%9B%B4%E4%BC%98%E8%B4%A8%E7%9A%84%E5%86%85%E5%AE%B9.md) | [English](../en/2023-04-29-how-to-generate-better-content-with-artificial-intelligence.md)

---

Before sharing, I recommend you follow Li Xiaolai's WeChat Official Account!

[What Is ChatGPT Doing… and Why Is It Useful?](https://mp.weixin.qq.com/s?__biz=Mzg3NTkxMzY2Mg==&mid=2247483879&idx=1&sn=f22871b8d4817d0d46a3f73be73f3be2&chksm=cf3b0936f84c8020cf4838ed03fe9922152014407ca3d9cbff93b29efd190f06e07ed175d274&scene=21#wechat_redirect)

Clicking on the link above will help you understand the underlying principles of ChatGPT, which is essential for grasping the context and challenges we face today. Set aside your previous understanding of artificial intelligence, generative intelligence, and large language models, as most of it has been misinterpreted. Media often spreads negative information because reporting good news is seen as "kissing up," which doesn't align with their own positioning. After reading the article above, you might finally understand where our current environment and challenges come from.

* * *

AI—artificial intelligence—has become a widely discussed topic in 2023. Whether you like it or not, it's already deeply embedded in our lives. Most people might react to its arrival like the Luddites, protesting and striking, or like the indigenous people threatened by Columbus, falling into ignorance.

> Luddism is an ideology and behavior that opposes new technologies and ideas, originating from a 19th-century social movement in Britain. At that time, some textile workers lost their jobs due to the Industrial Revolution and believed machines were the root cause of their plight. They began to destroy textile machines and called themselves Luddites, after a legendary weaver named Ned Ludd. On one hand, Luddism can be seen as a fear and resistance to technological progress, believing that AI could threaten human work, life, and values. On the other hand, Luddism can also be viewed as a critical and reflective stance toward technological progress, arguing that AI must align with human interests, morality, and responsibility. Luddism reminds us to pay attention to the impact of technological change on society, economy, and culture, and how to balance technology with humanity.
>
> Bing AI Assistant

> There's a well-known story about Columbus using a solar eclipse to intimidate the indigenous people. It's said that in 1504, during his fourth voyage, Columbus's fleet was caught in a storm off the coast of Jamaica and couldn't return to Spain. He sought help from the local indigenous tribe, but they were tired of his demands and refused to give them food or water. Columbus knew from a book of astronomy that a lunar eclipse would occur on the night of February 29. He used this opportunity to claim he was a messenger of God, warning the indigenous people that if they didn't obey his orders, he would make the moon disappear. That night, the lunar eclipse occurred as predicted, and the indigenous people, seeing the moon darken, panicked and begged Columbus for mercy, promising to provide everything they needed. Columbus pretended to communicate with God, convincing him to restore the moon's light. After the eclipse, the indigenous people revered and obeyed Columbus until he received the aid he needed to leave the island.
>
> Bing AI Assistant

  * Ignorance and worship often stem from fear and curiosity about the unknown. The indigenous people, unfamiliar with the principles of astronomical phenomena, were easily manipulated by Columbus's actions. Similarly, if humans don't understand the principles and mechanisms of AI, they may fall into blind trust or suspicion rather than rational evaluation and judgment.

  * Ignorance and worship also often result from an underestimation of one's own abilities and an overestimation of external forces. The indigenous people believed they couldn't control natural phenomena, so they easily surrendered to Columbus's threats and temptations. Likewise, if humans believe they can't control or influence the development and application of AI, they may give up their agency and responsibility, rather than actively participating and supervising.

  * Ignorance and worship ultimately lead to the loss of one's own interests and rights. The indigenous people, believing Columbus was a god's messenger, allowed him to take their resources and labor. Similarly, if humans are ignorant and worship AI, they may overlook the risks and challenges it brings, potentially losing their freedom and dignity.

* * *

Once we have a clearer and more accurate understanding of AI, we can then learn how to develop alongside it. I maintain an open attitude toward technology, but I'm tired of the overwhelming media coverage and the various content that sells anxiety. The people who produce such content are likely not long-term thinkers and have never had a correct understanding of facts.

Take ChatGPT, for example. If you read the article recommended at the beginning carefully, you'll understand that ChatGPT's algorithm is designed to generate the next word, trying to express itself as human-like. This means it cannot produce the kind of creativity and innovation we expect. Based on its training data, it can mainly provide descriptions of past events. When we ask for its opinions, it will mimic human expression and generate content that seems insightful, which is actually just its way of making up nonsense.

Once, while I was using ChatGPT to search for literature, it provided well-formatted citations, but when I searched, I found that the literature didn't exist. When I asked it again, it could only apologize silently. Even with the latest version of ChatGPT now having a Browsing feature, allowing it to link to browser searches, its tendency to say things that aren't true remains. This is inherent in the large language model behind it. Remember, it's human-like in speech, but not human. It has some intelligence, but not wisdom.

The above content is based on my reading, learning, and experience with AIGC tools. Please believe that our worries and concerns about AI are not as important as how we can use it to produce the content we need.

**First Question: How to Learn to Communicate with AI?**

This involves a key point: distinguishing between facts and opinions. When asking AI questions, avoid asking for opinions, as its strength lies in stating facts.

 _A fact is something that has already happened or is known to exist and can be proven with evidence._

 _An opinion is a personal view or judgment on a topic and doesn't require proof._

  * Check if there is objective evidence supporting the statement. If there is, it's likely a fact; if not, it's likely an opinion.

  * Check if there are subjective words or emotional tones. If there are, it's likely an opinion; if not, it's likely a fact.

  * Check if there are different perspectives or stances. If there are, it's likely an opinion; if not, it's likely a fact.

Once you understand this key point, your conversations with AI will be more effective.

Secondly, you should learn the operation guidelines for AI. For example, conversational AI and AI with drawing capabilities have different instructions. This involves a term called "prompt," which can be translated as "prompt words."

In AI, a prompt is a method of providing a pre-trained language model (PLM) with input text or a set of vectors, aiming to let the model perform a filling or generation task based on the input and the added prompt. For example, if we want a PLM to perform text sentiment classification, we can add a prompt to its input, such as:

  * Input: I like this movie.

  * Prompt: This movie is ___.

  * Output: Good / exciting / interesting, etc.

In this way, we can judge the sentiment of the input text based on the PLM's output.

The design and selection of prompts are crucial for the performance and effectiveness of PLMs. Some prompts are manually designed, some are automatically learned. Some are discrete, like words or symbols, some are continuous, like vectors or gradients. Some are within the sentence, like fill-in-the-blank prompts, some are before or after the sentence, like prefix or suffix prompts. Prompts are an effective way to use the knowledge a PLM has already learned to solve downstream tasks. They can reduce the need for hardware, data, and parameters, and also improve the model's generalization ability and interpretability.

Here's a simple template:

Clear demand + specific scenario + example / guidance for thinking

You can refer to some well-organized ChatGPT prompt templates at f/awesome-chatgpt-prompts: This repository includes curated ChatGPT prompts to help you use ChatGPT more effectively. (github.com)

I've compiled two sets of video learning content to help everyone understand how to use prompts. Each set takes about an hour to learn. If you can access the links below, you can also learn online.

* * *

First set of courses:

Taught by Isa Fulford (OpenAI) and Professor Andrew Ng, this course will explain how LLMs work, provide best practices for rapid engineering, and demonstrate how to use LLM APIs for various tasks in applications, including:

  * Summarization (e.g., summarizing user reviews for brevity)

  * Inference (e.g., sentiment classification, topic extraction)

  * Text transformation (e.g., translation, spelling and grammar correction)

  * Expansion (e.g., automatically composing emails)

You will also learn two key principles for writing effective prompts, how to systematically design good prompts, and how to build custom chatbots.

All concepts are explained through numerous examples, which can be directly used in a Jupyter environment to quickly gain hands-on experience with prompt engineering.

> Generative AI offers AI engineers many opportunities to build powerful applications that previously required days or weeks in just minutes or hours. I'm happy to share these best practices so more people can take advantage of these revolutionary new features.
>
> Andrew Ng

ChatGPT Prompt Engineering for Developers - DeepLearning.AI

https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/

Here are nine videos totaling one hour. If you can't access the link above, you can watch the videos directly.

Already followed

__

Follow

__ Replay __ Share __ Like

Close __

**Watch more**

More __

__

__

__

_Exit full screen_

[ __](javascript:;)

_Switch to vertical full screen_ _Exit full screen_

Tony Sheng has followed

[ __](javascript:;)

Share video

 __, duration 06:27

0/0

00:00/06:27

Switch to horizontal mode

Continue playing

Progress bar, 0%

 __

[Play](javascript:;)

00:00

/

06:27

06:27

[Speed](javascript:;)

 _Full screen_

 __ Speed playing

[ 0.5x ](javascript:;)[ 0.75x ](javascript:;)[ 1.0x ](javascript:;)[ 1.5x ](javascript:;)[ 2.0x ](javascript:;)

[ HD ](javascript:;)[ Smooth ](javascript:;)

Your browser does not support the video tag

__

Continue watching

How to Use AI to Generate Better Content

Watch more __

Share

,

How to Use AI to Generate Better Content

 __

Tony Sheng has followed

Share Like Comment

 ____ has been synchronized to See More [Write your comment](javascript:;)

 __

[ Video details ](javascript:;)

Already followed

__

Follow

__ Replay __ Share __ Like

Close __

**Watch more**

More __

__

__

__

_Exit full screen_

[ __](javascript:;)

_Switch to vertical full screen_ _Exit full screen_

Tony Sheng has followed

[ __](javascript:;)

Share video

 __, duration 17:35

0/0

00:00/17:35

Switch to horizontal mode

Continue playing

Progress bar, 0%

 __

[Play](javascript:;)

00:00

/

17:35

17:35

[Speed](javascript:;)

 _Full screen_

 __ Speed playing

[ 0.5x ](javascript:;)[ 0.75x ](javascript:;)[ 1.0x ](javascript:;)[ 1.5x ](javascript:;)[ 2.0x ](javascript:;)

[ HD ](javascript:;)[ Smooth ](javascript:;)

Your browser does not support the video tag

__

Continue watching

How to Use AI to Generate Better Content

Watch more __

Share

,

How to Use AI to Generate Better Content

 __

Tony Sheng has followed

Share Like Comment

 ____ has been synchronized to See More [Write your comment](javascript:;)

 __

[ Video details ](javascript:;)

Already followed

__

Follow

__ Replay __ Share __ Like

Close __

**Watch more**

More __

__

__

__

_Exit full screen_

[ __](javascript:;)

_Switch to vertical full screen_ _Exit full screen_

Tony Sheng has followed

[ __](javascript:;)

Share video

 __, duration 13:18

0/0

00:00/13:18

Switch to horizontal mode

Continue playing

Progress bar, 0%

 __

[Play](javascript:;)

00:00

/

13:18

13:18

[Speed](javascript:;)

 _Full screen_

 __ Speed playing

[ 0.5x ](javascript:;)[ 0.75x ](javascript:;)[ 1.0x ](javascript:;)[ 1.5x ](javascript:;)[ 2.0x ](javascript:;)

[ HD ](javascript:;)[ Smooth ](javascript:;)

Your browser does not support the video tag

__

Continue watching

How to Use AI to Generate Better Content

Watch more __

Share

,

How to Use AI to Generate Better Content

 __

Tony Sheng has followed

Share Like Comment

 ____ has been synchronized to See More [Write your comment](javascript:;)

 __

[ Video details ](javascript:;)

Already followed

__

Follow

__ Replay __ Share __ Like

Close __

**Watch more**

More __

__

__

__

_Exit full screen_

[ __](javascript:;)

_Switch to vertical full screen_ _Exit full screen_

Tony Sheng has followed

[ __](javascript:;)

Share video

 __, duration 07:33

0/0

00:00/07:33

Switch to horizontal mode

Continue playing

Progress bar, 0%

 __

[Play](javascript:;)

00:00

/

07:33

07:33

[Speed](javascript:;)

 _Full screen_

 __ Speed playing

**How to Use Artificial Intelligence to Generate Better Content**

Continue Watching

How to Use Artificial Intelligence to Generate Better Content

__

Tony Sheng has followed

Share Like Comment

____ has been synchronized to See More [Write Your Comment](javascript:;)

__

[Video Details](javascript:;)

Followed

__

Follow

__ Replay __ Share __ Like

Close __

**Watch More**

More __

__

__

__

_Exit Fullscreen_

[ __](javascript:;)

_Switch to Vertical Fullscreen_ _Exit Fullscreen_

Tony Sheng has followed

[ __](javascript:;)

Share Video

 __, Duration 12:41

0/0

00:00/12:41

Switch to Horizontal Mode

Continue Playing

Progress Bar, 0 Percent

 __

[Play](javascript:;)

00:00

/

12:41

12:41

[Speed](javascript:;)

 _Fullscreen_

 __ Speed Playing

[ 0.5x ](javascript:;)[ 0.75x ](javascript:;)[ 1.0x ](javascript:;)[ 1.5x ](javascript:;)[ 2.0x ](javascript:;)

[ HD ](javascript:;)[ Smooth ](javascript:;)

Your browser does not support the video tag

__

Continue Watching

How to Use Artificial Intelligence to Generate Better Content

Watch More __

Share

,

How to Use Artificial Intelligence to Generate Better Content

 __

Tony Sheng has followed

Share Like Comment

____ has been synchronized to See More [Write Your Comment](javascript:;)

__

[Video Details](javascript:;)

Followed

__

Follow

__ Replay __ Share __ Like

Close __

**Watch More**

More __

__

__

__

_Exit Fullscreen_

[ __](javascript:;)

_Switch to Vertical Fullscreen_ _Exit Fullscreen_

Tony Sheng has followed

[ __](javascript:;)

Share Video

 __, Duration 06:48

0/0

00:00/06:48

Switch to Horizontal Mode

Continue Playing

Progress Bar, 0 Percent

 __

[Play](javascript:;)

00:00

/

06:48

06:48

[Speed](javascript:;)

 _Fullscreen_

 __ Speed Playing

[ 0.5x ](javascript:;)[ 0.75x ](javascript:;)[ 1.0x ](javascript:;)[ 1.5x ](javascript:;)[ 2.0x ](javascript:;)

[ HD ](javascript:;)[ Smooth ](javascript:;)

Your browser does not support the video tag

__

Continue Watching

How to Use Artificial Intelligence to Generate Better Content

Watch More __

Share

,

How to Use Artificial Intelligence to Generate Better Content

 __

Tony Sheng has followed

Share Like Comment

____ has been synchronized to See More [Write Your Comment](javascript:;)

__

[Video Details](javascript:;)

Followed

__

Follow

__ Replay __ Share __ Like

Close __

**Watch More**

More __

__

__

__

_Exit Fullscreen_

[ __](javascript:;)

_Switch to Vertical Fullscreen_ _Exit Fullscreen_

Tony Sheng has followed

[ __](javascript:;)

Share Video

 __, Duration 12:23

0/0

00:00/12:23

Switch to Horizontal Mode

Continue Playing

Progress Bar, 0 Percent

 __

[Play](javascript:;)

00:00

/

12:23

12:23

[Speed](javascript:;)

 _Fullscreen_

 __ Speed Playing

[ 0.5x ](javascript:;)[ 0.75x ](javascript:;)[ 1.0x ](javascript:;)[ 1.5x ](javascript:;)[ 2.0x ](javascript:;)

[ HD ](javascript:;)[ Smooth ](javascript:;)

Your browser does not support the video tag

__

Continue Watching

How to Use Artificial Intelligence to Generate Better Content

Watch More __

Share

,

How to Use Artificial Intelligence to Generate Better Content

 __

Tony Sheng has followed

Share Like Comment

____ has been synchronized to See More [Write Your Comment](javascript:;)

__

[Video Details](javascript:;)

Followed

__

Follow

__ Replay __ Share __ Like

Close __

**Watch More**

More __

__

__

__

_Exit Fullscreen_

[ __](javascript:;)

_Switch to Vertical Fullscreen_ _Exit Fullscreen_

Tony Sheng has followed

[ __](javascript:;)

Share Video

 __, Duration 02:28

0/0

00:00/02:28

Switch to Horizontal Mode

Continue Playing

Progress Bar, 0 Percent

 __

**The second question: Learn how to choose the right tools?**
From my current usage experience, there's no need to go overboard—mastering a few tools is sufficient. After all, learning always comes with a time cost. You can check out the following two websites to understand various categories of AIGC tools, which basically cover all the tools I've come across. 54+ Best AI Video Generator Tools in 2023. (futurepedia.io) AI Toolset Navigation | 500+ AI Tool Navigation Guide, a comprehensive collection of domestic and international AI tools (ai-bot.cn)

Below are the tools I'm currently using, and the overall experience is quite good.

Information search: Bing AI, WebChatGPT, Monica

Dialogue: ChatGPT, Bard, Claude
Image generation: DALLE, Stable Diffusion, Midjourney, Imagica

Academic literature: ChatPDF, CatalystPlus, Talk to books

Writing output: Notion AI, Office365

Programming: GitHub Copilot

These are basically the tools I use. They are not difficult to use, and with careful reading of the instructions, you can get up to speed quickly. I also recommend trying platforms like AI Playground and Forefront Chat for multi-model synchronous output. By having different models answer the same question, you can more clearly and intuitively understand the application scenarios of each model.

Due to network issues in China, some websites and tools may not be accessible. I recommend these three tools:

Edge browser, by adding plugins, you can achieve various functions. Bing AI allows direct conversation, and according to reports, it uses the GPT-4 model. If the updated Bing lacks the Chat function, it might be due to IP address restrictions. Changing to a foreign IP can resolve this issue, while other functions remain usable.

Notion, as a note-taking software, offers a wide range of templates, especially the AI-assisted features, which are not restricted by network access and provide more efficient content output. Compared to other document software I've used, Notion is an excellent choice.

Hayo, a mobile app, allows you to experience both ChatGPT 3.5 and the Chinese Tsinghua University's ChatGLM-6B model domestically. You can directly use Stable Diffusion for image generation, and there are numerous templates available for direct use. It's relatively convenient to use. If you can't download it, you can scan the QR code to download the Android app I've uploaded to Baidu Netdisk.

Tools require practice. Instead of watching videos, reading articles, or looking at images to learn about various so-called shocking information, it's better to experience them yourself. There's no secret—just use them a lot, and they'll get better with use.

* * *

**Third question: Learn how to discern the authenticity of information?**

Jean Baudrillard was a French postmodern philosopher who critically analyzed contemporary society and culture. He argued that as technology and media have developed, people have increasingly lost their ability to perceive and judge reality. Instead, they are replaced by various symbols and images. These symbols and images are no longer reflections or imitations of reality but have formed an independent, virtual, and hyperreal world that has no connection with the real world, and even replaces it.

Baudrillard used the prefix "hyper-" to describe this hyperreal phenomenon, such as "hyperreality," "hypermarket," and "hypertext." He believed that "hyper-" represents an excessive, surplus, and over-the-top state. It transcends the principles of modern rationality, logic, and order, entering a chaotic, unordered, and meaningless realm.

[Source 1](https://www.promptingguide.ai/)

[Source 2](https://www.youtube.com/watch?v=dOxUroR57xs)

To illustrate this hyperrealistic characteristic, Baudrillard proposed a famous example: Disneyland. He argued that Disneyland is a typical hyperreal space, which creates a completely fictional world through various fantasies, simulations, and entertainment, immersing visitors in it and making them forget the real world outside. Disneyland not only imitates elements of history, culture, and nature but also exaggerates, beautifies, and simplifies them, transforming them into symbols and images rather than real entities. These symbols and images are not meant to convey any information or meaning, but rather to attract visitors' attention and stimulate their consumption desires, thereby generating profit.

Baudrillard believed that Disneyland was not an isolated example, but rather a reflection of contemporary society and culture. He argued that in a hyperreal society, people no longer care about the real or the unreal, but are instead confused and manipulated by various symbols and images. He believed that in a hyperreal society, people no longer possess subjectivity or free will, but have become consumers or producers of symbols and images. He argued that in a hyper, people no longer have a history or a future, but are trapped in an eternal present. Baudrillard strongly criticized and warned about this hyperreal society, believing it to be a dangerous and absurd society that deprives people of their awareness and participation in the real world, leading to the impoverishment and decline of human spirit and culture.

If we give a moreplain-language explanation of "hyperreality," we can understand it as "more real than real." When this theory was proposed in the 1970s, it deeply shocked me, and looking back at history, we always make new discoveries. In today's era of explosive information growth, with the massive amount of AI-generated content, do we really know what is true and what is false?

Bing AI provided me with the following methods to discern the authenticity of information:

  * Browse information from authoritative official websites or media, as they typically have higher credibility and accuracy.

  * View news objectively and don't believe information without factual basis or unknown sources, nor should you blindly spread unverified information.

  * Use online platforms to collect information widely, find information gaps, compare different sources, and analyze the consistency and logic of the information.

  * Sometimes, the truth takes time to reveal itself, so don't rush to draw conclusions when you first receive information. Instead, wait for more evidence and investigative results.

Even so, we will need to spend a lot of time discerning the authenticity of information in the future, because the information we input determines the quality of our output, and it will further influence our minds. Feeding our brains with nutrients is vastly different.

The following images are content that previously sparked heated discussions online.

It wasn't until the third image that the truth was revealed: a fake news story, paired with an image, without any discernment, and a flood of comments. This not only made me feel the current information overload, but also how our precious attention is being ruthlessly consumed. Are there really that many important things we need to worry about?

I recall Li Xiaolai's reminder in his column about the common pitfalls we've all fallen into, and how we can't help but jump back in:

> The first pitfall: "Mysteriously joining the crowd."
>
> The second pitfall: "Hurriedly following the crowd."
>
> The third pitfall: "Worrying endlessly about others."
>
> Li Xiaolai's Dedao column: <The Path to Financial Freedom>

Even if we protect our attention, when we can't avoid certain information, judgment is our self-defense weapon. Improving our judgment is our daily practice, and we need to keep exercising it. I recommend using the model from the book *Principles* to help us think.

We should repeatedly ask ourselves these three questions:

(1) What do you want?

(2) What is the fact?

(3) How can you achieve your goal given the facts?

Keep thinking and recording. As our experience accumulates, our judgment will improve. For example, in my work with video channels and WeChat ecosystem consulting, most of the problem-solving approaches come from my learning, reading, thinking, and practical experience. The more problems I solve, the faster my abilities improve. Moreover, I especially recommend that you share, express sincerely, and convey valuable content.

Li Xiaolai's three stages of development were highly enlightening for me:

(1) Write what I believe.

(2) Write what I want to achieve (since I want to achieve it, it means I believe in it).

(3) Write only what I have achieved.

I am also constantly striving along this path. When my expressions lean more toward what I have achieved, I have stronger persuasiveness, personal experience, and gains, and the judgments I form are relatively more reliable.

The following three articles are my thoughts on artificial intelligence shared in my knowledge planet, hoping they might offer you a little inspiration.

Finally, I invite you to start building a smart home together. As Li Xiaolai said, today is an excellent time for raising children, because the cost of education has greatly decreased, and we can now participate in the growth and education of ourselves and our children with AI. Learning anything has become much simpler.

AI can be your personal learning coach, your resource library, and your content generation assistant...

I look forward to you creating more content with AI, growing together, and continuously evolving!

Sincerely invite you to join our family growth community. Li Xiaolai and I are building a smart home together, experiencing the power of crowdsourcing and collective intelligence, and evolving with 6,000 families!
