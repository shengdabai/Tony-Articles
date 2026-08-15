# Feedback Is the New Compute

> 发布日期:2026-08-15 · [中文](../zh/2026-08-15-反馈才是新的算力.md) | [English](../en/2026-08-15-feedback-is-the-new-compute.md)

---

AI makes one old temptation stronger: if output becomes cheap, produce more.

More drafts. More features. More landing pages. More agents. More tests. More experiments. More dashboards. More versions of the same idea wearing different clothes.

At first, this feels like progress. A person who used to spend a week turning an idea into something visible can now do it in an afternoon. A small team can generate prototypes that once required a full department. A solo builder can ask an agent to write, refactor, summarize, compare, deploy, and document before lunch.

The machine is obviously faster.

But reality has not agreed to become faster at the same rate.

Users do not suddenly have ten times more attention. Customers do not suddenly become ten times more articulate. Trust does not compound at token speed. A market does not reveal its structure just because we have generated more possible answers. The world still replies at the speed of use, boredom, payment, misunderstanding, hesitation, habit, and care.

This is why the next bottleneck is not generation. It is feedback.

## Output Scales; Feedback Resists Scaling

There is a simple thought experiment I keep returning to.

Suppose you can get one hundred high-quality pieces of feedback in a week. If you test one feature, that feature receives one hundred signals. If you test one hundred features, each feature receives one signal. Your output increased one hundred times, but your contact with reality did not.

This sounds too simple, but it explains a lot of AI confusion.

AI expands the possible action space. It can create more options than a human can inspect, more code than a team can review, more content than an audience can meaningfully respond to, and more strategies than a founder can actually test. The visible side of work becomes abundant. The invisible side becomes painfully scarce.

Feedback has a body. It takes time. It requires a user to stop, notice, try, misunderstand, complain, pay, abandon, return, compare, or recommend. It requires someone to have enough context to say, "This solved my problem," or "This is close, but not the thing," or "I would never use this."

That kind of signal cannot be manufactured by producing more artifacts.

It has to be earned.

## The Bitter Lesson Has a Boundary

In AI history, one of the clearest lessons is that general methods which scale with computation tend to win over approaches that depend too much on hand-coded human knowledge. The 2019 essay "The Bitter Lesson" made that point sharply: over the long run, search and learning have kept benefiting from more computation.[^1]

That lesson explains why so many recent tools feel different. They are not trying to encode every rule by hand. They are riding scale. They learn from vast distributions, generate plausible local moves, and improve as the surrounding model and tool stack improve.

But there is a boundary.

Compute can search a space only after the space has been made searchable. It can optimize a target only after some target exists. It can learn from signals only after signals are captured. A coding benchmark, a math proof, a test suite, a game score, and a compiler error are all useful because they give the system something crisp to push against.

Human life is not always crisp.

A product can pass tests and still be useless. A feature can be implemented perfectly and still answer the wrong question. A newsletter can be grammatically clean and still have no pulse. A course can be well structured and still fail to move a learner. An agent can finish every assigned task and still make the whole system worse by doing the wrong work faster.

So yes, computation is becoming more powerful. But in open-ended human work, feedback is the part that tells computation what power should mean.

Without feedback, scale becomes noise with good formatting.

## Lean Startup Becomes More Important, Not Less

The Lean Startup method has always been built around a feedback loop: build, measure, learn. Its official methodology page says the basic activity is to turn ideas into products, measure customer response, and learn whether to pivot or persevere.[^2] It also describes validated learning as the unit of progress under extreme uncertainty.[^2]

AI changes the balance inside that loop.

Before AI, "build" was often the expensive part. You had to protect engineering capacity. You had to be careful before asking people to make something. You had to write specs, schedule sprints, argue about priority, and avoid wasting weeks.

Now the build step is shrinking. Not disappearing, but shrinking. More people can create more working versions with less permission and less waiting.

That sounds like the Lean dream coming true.

But if build gets cheaper while measure and learn stay expensive, the bottleneck moves. The question is no longer only, "Can we build the MVP quickly?" The sharper question is, "Can we get honest contact with reality quickly enough to deserve another build?"

This is where many AI-native workflows become weak. They optimize for the screenshot, the demo, the shipped branch, the publish button. They feel productive because the artifact appears. But the artifact is only the beginning of the experiment. The experiment has not spoken until someone outside the system responds.

The minimum viable product is not enough anymore.

We also need minimum viable feedback.

Who will see it? What action will count as signal? What would make us change our mind? Which response is noise? Which silence matters? How many people need to try it before we stop believing our own excitement? What feedback should be stored so the system becomes smarter next time?

AI helps you build more bets. That makes feedback discipline more important, not less.

## Engineering Already Knows This

Good software teams have been learning a version of this lesson for years.

DORA's software delivery metrics do not measure speed alone. The current DORA guide, last updated on January 5, 2026, describes five metrics that combine throughput and instability: change lead time, deployment frequency, failed deployment recovery time, change fail rate, and deployment rework rate.[^3] The point is not simply to deploy more often. The point is to deliver safely, quickly, and efficiently, while noticing when deployments create harm.

That pairing matters.

If you only measure output, AI will help you produce output. If you only measure deployment frequency, people will learn to deploy more. If you only count words, drafts, tickets, commits, or features, the system will become very good at producing countable motion.

But motion is not learning.

A healthy engineering system asks harder questions. Did the change reach production? Did it fail? How fast did we recover? Did users experience harm? Was the batch small enough to understand? Did the incident teach us something? Did we improve the system, or did we merely increase its activity level?

This is the mental model we need beyond software.

In writing, the metric is not how many essays you can generate. It is whether a real reader is changed, clarified, provoked, or helped.

In learning, the metric is not how many summaries you can produce. It is whether your future decisions improve.

In business, the metric is not how many ideas you can launch. It is whether customers trust one of them enough to change behavior.

In personal growth, the metric is not how many plans you can ask AI to make. It is whether you become the kind of person who can notice reality and adjust.

The world does not reward production by itself. It rewards production that survives contact with use.

## The New Job Is Feedback Design

If feedback is the new compute, then the valuable work shifts.

The valuable person is not merely the one who can prompt the machine to produce. Many people will be able to do that. The valuable person is the one who can design the circuit between output and reality.

That means defining what good means before asking AI to optimize. It means exposing work to the right users instead of hiding inside endless internal polish. It means keeping raw evidence close. It means preserving objections, not just praise. It means making the system remember failed attempts, so the same mistake does not reappear with a new interface.

It also means resisting the vanity of volume.

A person with AI can easily create the emotional experience of being busy. Ten directions, twenty drafts, thirty small launches, a wall of generated assets. It feels like acceleration. Sometimes it is just avoidance at higher resolution.

Real acceleration has a different texture. It narrows attention. It makes the next question clearer. It reduces self-deception. It creates a record of what reality said. It turns "I think" into "I tested," and then turns "I tested" into a better next move.

This is also where AI can make people stronger instead of lazier.

The lazy version uses AI to escape friction: I do not want to think, so please give me an answer.

The stronger version uses AI to increase the quality of friction: help me create the test, find the counterargument, compare the evidence, remember the last failure, and force this idea to meet the world sooner.

The first version produces comfort.

The second version produces adaptation.

## Do Fewer Things With More Reality

The practical lesson is uncomfortable: in an AI-rich environment, many people should do fewer things, not more.

Not because ambition is wrong. Because feedback is limited.

If you have one afternoon, do not ask only, "How many things can I generate?" Ask, "Which one thing can I expose to reality before the day ends?"

If you have one week, do not ask only, "How many versions can we ship?" Ask, "How many trustworthy signals can we collect, and what decision will they change?"

If you are building a personal system, do not only store prompts, templates, and automations. Store feedback. Store what failed. Store what surprised you. Store the sentence that made a reader pause. Store the user objection that hurt because it was true. Store the moment when your elegant plan met a messy human need.

That is the material of self-evolution.

AI will keep making generation cheaper. That part is probably not where most people will win. The harder and more interesting work is learning how to make reality answer clearly, quickly, and honestly.

The future will not belong to the people who can produce the most artifacts.

It will belong to the people and systems that can absorb the most truth without falling apart.

Output is becoming cheap.

Feedback is becoming sacred.

[^1]: "The Bitter Lesson," 2019. https://www.incompleteideas.net/IncIdeas/BitterLesson.html
[^2]: The Lean Startup, "Methodology." https://theleanstartup.com/principles
[^3]: DORA, "DORA's software delivery performance metrics," last updated January 5, 2026. https://dora.dev/guides/dora-metrics/
