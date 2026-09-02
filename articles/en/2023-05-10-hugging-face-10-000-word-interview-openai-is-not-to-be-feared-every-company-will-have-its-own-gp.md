# Hugging Face 10,000-word Interview: OpenAI is Not to Be Feared, Every Company Will Have Its Own GPT-4

> Published: 2023-05-10 · [中文](../zh/2023-05-10-HuggingFace%E4%B8%87%E5%AD%97%E8%AE%BF%E8%B0%88OpenAI%E4%B8%8D%E8%B6%B3%E4%B8%BA%E6%83%A7%E6%AF%8F%E4%B8%AA%E5%85%AC%E5%8F%B8%E9%83%BD%E4%BC%9A%E6%9C%89%E8%87%AA%E5%B7%B1%E7%9A%84GPT-4.md) | [English](../en/2023-05-10-hugging-face-10-000-word-interview-openai-is-not-to-be-feared-every-company-will-have-its-own-gp.md)

---

Recently, Hugging Face founder Clem Delangue participated in an interview, during which he discussed several key issues:

* The Founding Story of Hugging Face
* How will large model AI evolve in the future?
* Will closed-source strategies of big companies affect the open-source community?*
* What drives the progress of large models?
* Is there a difference in advantages and disadvantages between general-purpose large models and specialized small models?
* How to start a more competitive AI business at this stage?

Hugging Face is the world's largest AI open-source community, known as the GitHub of the AI field, founded in 2016, with a team of nearly 170 people, headquartered in New York.

Currently, the platform has over 20,000 open-source datasets, more than 100,000 demos, and over ten thousand companies using open AI technologies from the platform. Hugging Face's official introduction is: building the future AI community.

Clem Delangue is the CEO & Co-founder of Hugging Face. He worked for 8 months at eBay as early as 2010, and his first startup experience was in 2011 at Moodstocks——building machine learning for computer vision. The company was acquired by Google. In 2013, he moved to New York, USA to lead the mention marketing and growth department. In 2016, he founded Hugging Face. He has been working in artificial intelligence for about 15 years.

**01**

## **The Origin of Hugging Face's Startup**

**Elad Gil: First, tell us about the origin of Hugging Face and how you got involved in it, what it was like at the beginning, and how it evolved into what it is today?**

**Clem Delangue** ：As you said, I have actually been working on AI-related work for a long time. Before today it became so popular and hot, the three founders of Hugging Face gathered together to build a new paradigm of technology, and we were very excited about it. When we founded the company, we wanted to do something scientifically challenging, because one of our co-founders, Thomas, had the relevant technical background, but also something fun.

We initially created an AI virtual pet, similar to an entertainment version of ChatGPT.

At that time there were Siri and Alexa, but we thought focusing solely on productivity was very boring, and we worked on this project for nearly three years. We raised our first seed round funding based on this idea, and many users really loved it. They chatted with this pet billions of times, but this happened naturally, and I can tell this story later.

We have transitioned from that project to the current state, which is the most popular open-source AI platform.

**Elad Gil: How did you first become interested in AI? Artificial intelligence has gone through different trends over the years, and AlexNet's convolutional neural network model sparked many new developments, such as CNN (Convolutional Neural Network) and RNN (Recurrent Neural Network), etc. You've been working in this field for 15 years, did you start getting interested in it before that or not?**

**Clem Delangue** ：At that time, we hadn't even referred to it as artificial intelligence or machine learning.

The first startup company I worked for was called Mood Stocks, where we applied machine learning to computer vision on devices. We built a technology that allows users to take photos of objects with their phones and identify them. For me, realizing how artificial intelligence can truly unlock new capabilities was when I met the founder of this startup company.

At that time I was working at eBay, they told me that the company you acquired named Red Laser, which is used to recognize barcodes and pull up eBay pages, you're too weak, you should use machine learning. Don't recognize barcodes, actually you can recognize the objects themselves.

I thought they were crazy back then, it was impossible. You couldn't do this with traditional software, but they were actually using some form of machine learning to achieve this. So at that time I realized, wow, you could do many new things with this new technology. This actually brought me to where I am today.

**Elad Gil: So you started Hugging Face's startup, and you wanted to create an AI virtual pet. I find it interesting that back then when you talked about artificial intelligence, people would scoff and say, "No, that's machine learning." Now, with what some systems can do, the term has come back to artificial intelligence. What was it that made you decide to go in a direction completely different from the original vision for Hugging Face?**

**Clem Delangue** ：This is a very natural thing that happens. Stripe's founder Patrick Collison once said that what's important isn't just starting a company, but having moments of entrepreneurial breakthrough that change the course of the company.

For us, this is thanks to one of our co-founders, Thomas Wolf, who suddenly mentioned the BERT model introduced by Google on a Friday night, which based on TensorFlow didn't perform very well, and Thomas wanted to try transplanting it onto PyTorch.

We told him to just enjoy himself.

Monday he told us he had finished it and released the project on GitHub, we posted a tweet and Dedaoed 1000 likes.

At that time we were just unknowns. We were confused as to why people would like such a niche and technical tweet about PyTorch porting BERT. There must be some reasons for that.

We decided to continue trying, trying to add some other models to GitHub. Gradually, the community began to take shape, and people started to report bugs and fix vulnerabilities in our GitHub repository, adding other models, such as the first GPT model. Next, the speed of adding models increased rapidly, eventually, we ended up with the most popular AI GitHub repository. This is the reason for our transformation from the initial idea to where we are now.

**Elad Gil：Could you describe to everyone what Hugging Face is today, how it is used, the importance of its products and platforms as well as its ecosystem?**

**Clem Delangue** ：It's great that we are now the most commonly used open-source AI platform among everyone, **you can imagine it as a GitHub for AI.**

Just like GitHub is a platform for hosting code, collaborating on code, sharing code, and testing code, we are the same but focused on machine learning. Over 1 million repositories are hosted on the Hugging Face platform, most of which are open-source models. So you might have heard of stable diffusion, T5, BERT, Whisper, and so on. There are over 20,000 open datasets available on the platform. There are also demos, with over 100,000 demos hosted on the platform. More than 15,000 companies are using the platform to integrate AI into their features, products, or workflows.

**Elad Gil：Among the many questions we've collected, the most frequently asked question is about Hugging Face's future direction. Considering Hugging Face's current impressive achievements, there are many possible directions to explore: B-end customization, B-end hosting, tool-based products, or other types of products. Currently, what directions are you mainly focusing on for your products?**

**Clem Delangue** ：We are currently pursuing two main directions. First, **we see artificial intelligence moving from some narrow technologies that solve specific problems, toward becoming the default paradigm for building all technologies.**

For us, this means expanding from the text, audio, and text-to-image models currently being used on the platform, to every field.

For example, last week we started to see the first open-source text-to-video model, and we also began to see many time-series models on the platform, such as those used for financial forecasting, estimating urban traffic conditions, etc. We also saw an increasing number of biochemical models. Therefore, ensuring that we support these wide-ranging AI use cases is the first step.

**Step two is to make it easier for everyone to build AI, including software engineers.**

In the past, our platform was primarily designed for machine learning engineers and those who truly train, optimize, and evaluate models. However, now we are seeing, especially with the emergence of AI APIs, that everyone wants to do AI, even complex software engineers, product managers, and infrastructure engineers. Therefore, one of our focuses is to lower the barrier to entry for using our platform. Because ultimately, we believe every company or team should be able to use open source to train their own models.

Today everyone is talking about ChatGPT, GPT-4. But I think, in a few months or even a few years, every company will build their own GPT-4 and train them in the same way. If every company has its own codebase, the number of codebases will be as numerous as the number of companies.

We believe that tomorrow, every company will have its own model, its own machine learning capabilities, rather than outsourcing them to others, but truly possessing these capabilities to enable them to differentiate themselves, catering to their specific audiences or specific use cases.

**02**

## **AI's Progress Today**

**It's due to open source**

**Elad Gil** ：Every time a platform iterates, you'll find that three or four things have changed. The way the system handles input and output has changed in some aspects, or at least the data types you process have changed. User accessibility and the UI have also changed. The way you interact with mobile devices versus desktop devices is different. The scale and impact of this transformation are huge. If we consider artificial intelligence as a new platform, how do you view the idea that everyone will have their own GPT-4 as you mentioned.

It seems that the nature of programming itself might change at certain times, and we can set the whole issue aside, without discussing whether we have also created a digital species, perhaps we will finally discuss this issue at the end.

**But what role does Hugging Face play in this massive platform transition?**

**Clem Delangue** ：Yes, the way we look at problems is that we really like Andrej Karpathy's Software 1.0 metaphor, which is how we've built technology over the past 15 years.

**Now artificial intelligence is the Software 2.0 era.**

This is a new approach, a new way to build all technologies. This is a new paradigm, a new paradigm for building all technologies. If you consider this, you need better tools, more adaptive tools to do this. You need a better community, a way of teamwork, the entire ecosystem needs a way of cooperation.

This is the kind of tool we want to provide, a new tool, a new collaboration platform, to better build artificial intelligence. We also try to build a future that excites us. I think many people are now afraid of artificial intelligence, worried about its potential and risks. The question we are thinking about is, if you can build a future where everyone can understand and build artificial intelligence, you can eliminate many of these risks.

For example, you reduce the possibility of systems with bias. You provide regulators with tools to actually implement safeguards, and you give companies the capability to use and provide systems to users and customers that align with their values. In the end, you hope Stripe can say, "This is our values, so this is how we build artificial intelligence based on these values." So this is also an important thing we are working on. Sometimes we say our mission is democratized machine learning, and we are striving for this because we believe it is important for the world.

**Elad Gil：It feels like Hugging Face has always been very consistent, hoping to have ethical AI or clear alignment. Many companies, such as Anthropic, have adopted the constitutional AI approach, basically providing a set of rules that tell the model what it should follow to manage its activities or actions. What methods do you think are most effective, and what do you hope people will do more in terms of alignment?**

**Clem Delangue** ：Alignment is a complex term, because it means different things to different people.

It can be viewed from an ethical perspective, that is, the alignment between values and systems. Many people use it today as a more accurate improvement. Honestly, when they perform some alignment work, they actually make the model more accurate through reinforcement learning from human feedback. So this issue is somewhat difficult to argue about.

I think, overall, humans cannot control, improve, and align with systems they don't understand. Therefore, the main thing we are trying to push on Hugging Face is a more transparent way to build these systems, such as what data they are trained on, what limitations they have, what biases they have, etc. I think if we create more transparency in this area, users can almost create a system with a more ethical core. So this is the biggest issue we are focusing on.

**Elad Gil：What is your biggest concern about open-source artificial intelligence being misused?**

**Clem Delangue** ：AI has many risks, due to its distribution through API or open source, the biggest risk is dual use. Although the model builder defines the correct usage, the user wants to use it in an incorrect way.

Therefore, we have been trying new model licensing forms, which is an early attempt and may not solve all the problems. We have been supporting a project called Rail and Open Rail, which is a responsible AI licensing form aiming to become an open licensing that allows everyone to use the model, but it defines some usage methods that are prohibited from the perspective of the model author, thereby creating a legal challenge to prevent people from using it in the wrong way. This is the approach we have taken to mitigate some of the risks of AI's dual use.

**Elad Gil** ：In the early days, many industrial research laboratories, Google, and OpenAI would actually release the architecture of their models when publishing models. They would publish detailed papers explaining how the models work, and the original Transformer paper was quite explicit. Now they are starting to limit the amount of information they disclose about the models.

**Do you think this will have a negative impact on open source? How do you see the future, especially in the area of large language models?**

**Because when I saw the image generation models, they are often cheaper and more reliant on open source. However, for foundational models that require large-scale scalability and computational power, this could become an issue.**

**Are you worried about the lack of public information? How do you view the difference between open-source and closed-source large foundational models?**

**Clem Delangue** ：Yes, this is a challenge. At present, I think we need to remember that: everything we have today is thanks to open-source knowledge and open-source code. Now, each model is built on the shoulders of giants.

**If there were no research papers on BERT, T5, Transformers, GPT, etc., we might have needed another 50 years to achieve today's accomplishments.**

It is exactly this open source that promotes a positive cycle, making the progress of artificial intelligence faster than anything people have seen before. If we stop doing this, it will slow down, and we may need more time. As the proverb says, life cannot be born in a vacuum; it needs basic materials to reproduce and thrive.

If some companies start reducing their investment and contributions to open source, other organizations will take their place and benefit from it. For example, recently announced organizations such as EleutherAI, Alen AI from Seattle, and Stability AI.

I think we will eventually see various different organizations contributing to open source. Traditional software prefers closed source and closed code, but open science does not, because most scientists' goal is to contribute to society, not just to do things that make companies profit. So maybe the open source companies will change recently, but I don't worry about that.

One very clear proof is that, **in the past few months, the number of open-source models, open-source databases, and demo demonstrations on Hugging Face has been increasing continuously.**

We may have some weaknesses in the text field, which is one of the areas where private technology leads open source.

However, you can see the audio, the best Whisper is open-sourced; text-to-image, Stable Diffusion is very powerful. In fields such as biology, chemistry, and time series, open-source models are also very powerful.

**OpenAI is making astonishing achievements, but open source will gradually catch up, sometimes leading ahead, sometimes falling behind, which is a normal technical cycle.**

**Elad Gil：Yes, I agree. In fact, if we look at the technical iteration cycle, for example the passive technology cycle, those that usually appear as truly successful large open source solutions, will always have major commercial companies behind them to compete with other companies' commercial products, which is almost a brand strategy. For example, the biggest sponsor of Linux is IBM, used to counter Microsoft; Webkit is supported by Apple and Google. Do you think who will be the main supporters of the open source model? Will it be Amazon, to counter Google, Microsoft, and OpenAI's collaboration? Or Nvidia or Oracle? Or a coalition of multiple commercial companies, will the government get involved in this?**

**Clem Delangue** ：Many large tech companies have a good relationship with open source. Amazon, NVIDIA, and Microsoft are examples; I think there may be some support coming from these companies. I'm also very interested in government participation in open source computing. In fact, the BLOOM open-source large model we previously participated in was collaborated with research institutions, and we received support from the French JeanZay supercomputer.

I think providing computational power to universities, independent organizations, and non-profit organizations to avoid the concentration of power and create more transparency is also a way to have a positive impact on society.

**03**

## **Training capability is the current state of large models**

**Development Bottleneck**

**Elad Gil：What do you think is the biggest driving factor for the current large predictive models—computation, data, algorithms, or something else?**

**Clem Delangue** ：In the scientific community, there is a growing consensus that data is not just about the quantity of data, but rather that the quantity of data begins to matter more than blind expansion of computation.

But I think there are still some important things to remember, namely that training a very good large model is still an art.

This is not just a simple recipe, for example, you have good data, and a lot of computing power. You might be able to train a good model. This is still a very difficult and hard-to-understand training process. It's almost like alchemy, very few people can do it today, right? **Perhaps there are only 20 people, or maybe 50 people in the world who can do it today. It's a very small number.**

I think people sometimes fail to realize this. Therefore, I believe there is still significant room for improvement in the technical approaches to training a good model beyond computation and data.

**Elad Gil：Why would the number of people be so low?**

**Clem Delangue** ：This might be a billion-dollar answer, if the answer were so easy to figure out, maybe everyone could train large models. I think it requires a mixed ability of technical capability, scientific capability, and project management capability, involving a comprehensive understanding of when to launch a project, when to release, how to optimize, and how to re-optimize three months or six months later.

**Elad Gil：What do you think is the most exciting AI research area right now? Or which areas would you like more people to work on?**

**Clem Delangue** ：I'm very interested in text processing. I've just been in this field for a short period of time.

But I think it's especially interesting and important now to work on more technically challenging problems in other fields. For example, I'm very interested in biology. How can we apply artificial intelligence to biology? How can we apply artificial intelligence to chemistry? This can create a positive impact on the world, but it can also make oneself stand out and build a more technically challenging artificial intelligence stack. So these are some of the things I'm currently interested in.

**Elad Gil：Now there are two views about large models: one is the general-purpose model, and the other is the specialized model. Some people believe that by continuously expanding the model to make it more general, it can eventually do anything. On the other hand, some people think that focusing on small models and targeting specifically what you are trying to do can efficiently complete tasks without waiting for large-scale generalization. What do you think we will be like in three to four years?**

**Clem Delangue** ：**I plan to give up making predictions in the field of artificial intelligence, because it's too difficult. Sometimes after predicting something, the situation is completely opposite three months later, which makes me look like a fool.**

Usually I don't make too many predictions, but I usually try to observe the past and data. Since the release of ChatGPT, developers have uploaded over 100,000 models to Hugging Face, right?

They won't do this just for fun.

Another interesting data point is that if you look at all the models on the Hugging Face Hub, the most commonly used are actually models with 5 million to 5 billion parameters. I think the reason is that when you Dedao more customized spatial models, you Dedao some things that are easier to understand and iterate on. The speed of getting results is generally faster in most cases, sometimes you can even run them on a phone or specific hardware, which is also cheaper, and can provide better accuracy for your specific use case.

When you specifically customize for some applications, for example, to create a chatbot for customer service, and the customer is asking about invoice matters, you may not need the chatbot to tell you the meaning of life or the weather in San Francisco. You just need it to be very good at your specific use case. What we are saying is that more specialized, smaller models tailored for this purpose are usually more appropriate.

However, some use cases, for example, if you are Google, wanting to build a general-purpose search engine to answer all these questions, obviously, a larger general-purpose model is meaningful.

In the end, I think there will always be various different models, just like there are various different codebases, right? Today you wouldn't say my codebase is better than yours. You wouldn't say Stripe's codebase is better than Facebook's codebase, right? **They just do different things and answer different questions. It's the same with models; there's no one model that is better than another. More importantly, what model suits your use case, and how do you optimize it for your specific use case?**

**
**

**04**

## **Entrepreneurs should go build AI**

## **But Not Just Simply Using AI**

**Elad Gil：How do you think about the commercialization of Hugging Face, and which directions are you heading towards?**

**Clem Delangue** ：I think open source gives you superpowers and some things you can't do without it. For us, we are just some pretty laid-back French people, and without the community, contributors, the people who helped us with open source, and those who shared their models, we wouldn't be here today.

Therefore, it also creates new capabilities; when you have an open platform like Hugging Face, the usual way to commercialize is by providing enhanced versions or customized versions of some open-source models. We now have 15,000 companies using our product, with 3,000 companies paying for our services. Usually, they pay for additional features, such as enterprise-level features. For example, some companies need security, user management, or they need computational power, such as running on faster hardware, or running inference and training on the platform, etc.

We have created a great balance; if you are a company that contributes to the community and ecosystem, you can release your open-source model, which will always be free. If you are a company that makes more use of this platform, you will contribute in different ways, such as financially. We are still in the early stage of commercialization, but we have found this difference, which allows us to continue working for the community, continue making open-source contributions, stay aligned with our values and what we want to do, while making it a good business, a sustainable business, and also enables us to scale and increase our influence.

**Elad Gil：I think Hugging Face is one of the most popular products and communities in the AI field. What specific strategies did you take in building the community, or what do you think was particularly important in the early days?**

**Clem Delangue** ：I just want to say that using the emoji of a hugging face (🤗) as the company's logo is enough to win the favor of Dedao community.

However, the thing we are most satisfied with in all the things we have done is that we have never hired any community managers, which seems a bit counterintuitive, but in reality, every member of Hugging Face is contributing to the community and communicating with community members. Our Twitter account allows any member to post tweets, which was a bit scary at first, but as we have grown, we haven't encountered any issues so far.

**Elad Gil：What kind of AI work do you hope more startup founders will focus on?**

**Clem Delangue** ：I have some biases about this. I hope more entrepreneurs build AI, rather than just simply using AI. There is a big difference between the two. In the early stage of software development, you can use APIs, and quickly build a website using software like WordPress, which is a fast way to get started. However, the real competitiveness comes from users writing code and building their own technology. This is the same for AI. You can quickly do some things, **but if you really want to take this seriously, you need to understand how models work, how to train and optimize them, which will give you the opportunity to become a truly great startup and create truly great products.**

Runaway announces their text-to-video generation feature, which is a truly AI-native startup company, they are genuinely training models, building models, and truly building AI, rather than just simply using AI.

If you are just using AI, you need to be clear about your model and strengths, especially in the early stage, without focusing on technical capabilities, but rather more on how to acquire more users.

**Audience Question: How do you view OpenAI's response to open-source? They have not disclosed any information about GPT-4 and will not open-source it, as they are concerned about safety.**

**Clem Delangue** ：I respect everyone's way, different organizations have different technical development paths. But I have a different view, **if we look back at the development of technology, we can find that the biggest security risks usually come from the concentration of power or closed-door technological development.** If building a product under an open-source model, it's actually adding a sustainable path to technology, allowing non-governmental organizations, civilians, etc., to participate and play a supervisory role.

Our starting points are very different, but for the ecosystem, I think it's not a big issue. Different organizations can have different views, as long as what the company does aligns with its values.

**Audience Question: You mentioned that data is important for optimizing large models, and many companies are facing the challenge of how to enhance model capabilities while protecting data privacy—should they adopt open-source models or federated learning? What's your view on this?**

**Clem Delangue** ：We have been researching distributed or decentralized training, but it is still difficult to achieve at the moment, and we also hope more people can participate in this work. We launched an initiative called BigCode, releasing the largest open codebase so far. Users can train their own models based on this, and users can also choose to give up some data during model training. Everyone hopes for greater transparency in data, but a challenge we face is that many models are opaque in terms of how they are trained, because there is no transparency. We hope for more transparency so that we can know what data is used and what the models are doing, and then we can find possible solutions to address people's concerns about data privacy.

**Elad Gil：Do you think the pattern of websites providing robots.txt for search will end? Will there be something like ai.txt in the future to declare that they don't allow AI to collect data?**

**Clem Delangue** ：I think there will be, we definitely need to establish regulations around data collection for AI, which is very important for content creators. Because value feedback is very important, we hope contributors can be rewarded by Dedao. But I think there is currently no good solution. **The current search interface similar to a chat window is unable to provide incentives for content creators.** If I built a website, I could previously earn money by advertising based on website traffic. Now, the content appears only in the chat window, and users no longer visit the website. As a content creator, where is the motivation for me to create content? People will therefore stop content creation and building websites, because they cannot get returns from their content. This is a very important issue, and we have only touched the surface of the problem; there are still many important issues to be resolved.

* * *

Follow Founder Park, we will continue to release more comprehensive and in-depth discussions and reports on large models.

**If you have the idea of starting a big model startup, welcome to join our big model related field exchange group, to together explore the consensus and understanding of entrepreneurship in the era of big models.**

* * *

**More Reading**[ AI Godfather Hinton & MIT 10,000-word Interview: Humans May Just Be a Transitional Stage in the Evolution of AI](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247487084&idx=1&sn=3e1cff12b43aa73bedb1344dbe6b3ffc&chksm=c00ae850f77d614610824c9b5bd0a60978fd7d9c235e78e0bb3a4a09461ec861cb224cf7abf7&scene=21#wechat_redirect)
[Elon Musk talks about young people's education, community management, and life happiness, Buffett strongly recommends watching](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247487041&idx=1&sn=de8711050f10347786093d4f360d9c91&chksm=c00ae87df77d616b6f3d66fd17b6048bdd9b0c445a5584f98fd8440ff118f48edc8f361867ef&scene=21#wechat_redirect)
[OpenAI and Google will lose to whom?](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247487025&idx=1&sn=bdef3eea9794c5b488d3abeb38fe7d19&chksm=c00ae80df77d611b89cb12583976b30e10b61093127b7f497317217db16424cb408cddd8d28a&scene=21#wechat_redirect)[Americans really start to fear AI](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247486913&idx=1&sn=702cce6c3eca6e95417c332024c5a11b&chksm=c00aebfdf77d62ebfedeca525c4c109d444679c8bf0011adfad0dc354ef2b875a86ce0d7611e&scene=21#wechat_redirect)[GitHub Chief Engineer: Don't force users to chat with AI anymore!](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247486807&idx=1&sn=4862074e78e63056eb2733fed1a82114&chksm=c00aeb6bf77d627d946482571bd732d78205ff6b6da96881d7ccd19c4ffa86ea462844b4f673&scene=21#wechat_redirect)

Please cite the original article by adding WeChat: geekparker
