# The Loop Needs a Judge

> 发布日期:2026-07-09 · [中文](../zh/2026-07-09-循环需要一个裁判.md) | [English](../en/2026-07-09-the-loop-needs-a-judge.md)

---

Today’s notes kept circling one idea from several directions: loops.

Loop Engineering. Agent harnesses. Autoresearch. Self-improving systems. Evaluators that evolve with the agents they judge.

The surface story is easy to tell. We are moving from “prompt the AI” to “build a system that prompts the AI for you.” A loop finds the work, sends it to an agent, checks the result, records the state, and decides the next move. One recent essay defines Loop Engineering almost exactly that way: instead of being the person who keeps prompting the agent, you design the system that does it.[^1]

That sounds powerful. It is powerful.

But it also hides the dangerous part.

A loop by itself is just repetition.

The real question is not whether the machine can keep going after you leave the keyboard. Of course it can. Machines are very good at not getting tired. The real question is:

What tells the loop that it is getting better?

Without a judge, a loop is only a confident circle.

## Generation Got Cheap

For most of human history, producing a draft was expensive. A draft required attention, time, skill, and often courage. You could not generate ten serious alternatives in a minute. So we naturally respected output. The person who could make something appear on the page seemed to have done the hard part.

AI changes that balance.

Generation is now cheap. Not free, but cheap enough that the bottleneck moved. The scarce skill is no longer “can you produce a plausible answer?” The scarce skill is “can you tell which answer deserves to survive contact with reality?”

This is easy to miss because fluent output still feels like progress. A long answer looks like work. A working demo looks like proof. A green check mark looks like truth.

But cheap generation creates a strange inversion: the faster the system can produce, the more expensive judgment becomes.

If a human writes one draft, you can read it slowly. If an agent produces fifty variants overnight, the question becomes: what filters them? What keeps one and discards forty-nine? What prevents the system from optimizing for the easiest-looking metric while drifting away from the thing you actually care about?

This is why the judge matters.

A judge is not necessarily a person in a chair. It can be a test suite, a held-out dataset, a reader who does not owe you kindness, a compiler, a customer who pays or refuses to pay, a physical measurement, a calendar, a public commitment, or a simple checklist that says what “done” meant before you got seduced by the output.

The form varies.

The function is the same: it creates resistance.

And resistance is what turns movement into learning.

## The Lesson of Autoresearch

The cleanest example in today’s notes was autoresearch.

The public README describes a small but real setup: an AI agent edits one training file, runs a fixed 5-minute experiment, checks a validation metric, keeps the change if it improves the result, discards it if it does not, and repeats.[^2] The design is deliberately narrow. Data prep and evaluation are locked down. The agent mainly touches `train.py`. The metric is `val_bpb`, lower is better. The fixed time budget makes experiments comparable.[^2]

That is the key.

The interesting part is not that the agent writes code. We already know agents can write code.

The interesting part is that the system leaves the agent no room to win by sounding convincing. The answer is not “this seems better.” The answer is a measured result.

An external write-up reported early experiments where this pattern ran hundreds of trials, kept only the improvements, and found changes that transferred across model sizes. The same write-up also reported a separate overnight run where a smaller model beat a larger prior baseline after dozens of experiments.[^3] These are early examples, not a law of nature. But the direction is important.

The loop is powerful because the judge is explicit.

If the metric were leaky, the agent would learn to exploit it. If the evaluation code were editable, the agent could lower the bar. If the dataset were not held out, the system could memorize the test. If the human accepted “looks good” as the stop condition, the loop would become a machine for producing confidence.

So the real engineering is not only “let the agent iterate.”

The real engineering is:

- freeze the part that defines correctness;
- limit where the agent may act;
- record each attempt;
- compare attempts on a stable surface;
- keep only changes that survive the judge.

That is what makes the loop a learning system instead of a typing machine.

## A Static Judge Also Gets Old

There is a second problem.

A fixed judge is necessary, but it is not enough forever.

If the judge never changes, the system eventually learns the shape of the judge. This is true in exams, benchmarks, content platforms, software tests, and personal habits. When a metric becomes important enough, people and machines both learn to game it.

This is where one of the more interesting research directions appears: not only evolving agents, but evolving the evaluators that judge them.

A recent arXiv paper frames this as a Red Queen problem. Earlier self-improvement systems often assumed a fixed evaluation environment. The Red Queen framing asks what happens when the agent and the evaluator co-evolve, while still keeping enough control that the whole system does not collapse into moving goalposts.[^4]

The practical intuition is useful even outside research.

In a healthy learning system, the judge should be stable inside one round, then improved between rounds.

During the round, the judge must not wobble. If you change the rule every time the result hurts your feelings, you are not learning. You are negotiating with reality.

But after the round, the judge should be allowed to mature. A test suite can gain a regression case. A writing checklist can add a question about reader confusion. A product metric can be adjusted after you discover it rewards shallow engagement. A learning plan can update once you realize your old exam did not test real transfer.

This is subtle.

If the judge never changes, you get benchmark overfitting.

If the judge changes whenever you feel uncomfortable, you get self-deception.

The art is to freeze the judge long enough to learn, then update the judge honestly enough to keep learning.

## Why This Matters for Ordinary People

Most people will not run autonomous model training experiments.

But everyone is now surrounded by cheap generation.

You can ask AI for ten article outlines, ten business ideas, ten lesson plans, ten product names, ten negotiation scripts, ten explanations of a book you did not read carefully. The machine will answer. It will answer politely, quickly, and often with the emotional texture of competence.

That is useful.

It is also dangerous.

Because if you do not bring a judge, the model’s fluency becomes the judge.

This is how people become lazy with very advanced tools. They do not stop working because the tool is bad. They stop working because the tool gives them a pleasant substitute for feedback.

A real judge is usually less pleasant.

For writing, the judge may be: can a real reader summarize the point after reading? Did the piece risk a concrete claim? Are the facts sourced? Does the ending actually close the loop?

For learning, the judge may be: can you solve a new problem without looking? Can you teach it to someone else? Can you use the idea next week, under pressure, when the AI is not whispering the answer?

For building, the judge may be: does the thing run? Does a user complete the workflow? Does the test fail before the fix and pass after it? Does the system recover when the happy path breaks?

For life, the judge may be even simpler: did the plan change what you did today?

That last one matters. A lot of AI usage ends in beautiful intention. The plan is clear. The next step is obvious. The summary is elegant.

Then nothing changes.

The judge was missing.

## The Zeroth Class Builds Judges

I keep coming back to the phrase “the zeroth class.”

The zeroth class does not use AI to become a consumer of answers. It uses AI to strengthen the layer before answers: attention, taste, memory, practice, execution, and judgment.

In the age of cheap generation, the zeroth class will not be defined by who has access to the newest model. That advantage decays quickly. The models spread. The interfaces improve. Yesterday’s magic becomes today’s button.

The durable difference will be judge design.

One person asks for output.

Another person builds a loop with a judge.

The first person gets more text.

The second person gets a system that can notice error, preserve attempts, compare outcomes, and improve over time.

At first, the second person may look slower. They write down success criteria. They hold out examples. They define privacy boundaries. They decide what evidence would change their mind. They create stop conditions. They ask the AI not only to generate, but to help maintain the court in which generation will be judged.

This looks less magical than one beautiful prompt.

It compounds better.

## Bad Judges Are Worse Than No Judges

There is one final warning.

Not every judge is good.

A bad judge gives false confidence at machine speed. A test that checks only the easy path will bless fragile software. A benchmark that rewards keyword matching will train shallow answers. A social metric that rewards outrage will punish nuance. A personal checklist that measures only busyness will make you productive in the least important direction.

This is the old problem of measurement, but AI makes it sharper.

When a human optimizes a bad metric, the damage is limited by human speed.

When an agent optimizes a bad metric, the damage scales.

So judge design has to include humility. The judge is not God. It is a tool. It should be inspected. It should have held-out reality behind it. It should be challenged by examples that make it uncomfortable. It should sometimes be overruled by human judgment, but not casually, and not because the result was inconvenient.

The best judge is not the harshest one.

The best judge is the one that makes learning harder to fake.

## Stay the Engineer

Loop Engineering is not a trick for disappearing from the work.

It is a way to move your work to a higher layer.

Instead of typing every instruction, you design the loop. Instead of judging every draft by vibe, you design the judge. Instead of trusting the agent because it sounds fluent, you create a surface where the agent can be wrong in public, recover, and try again.

That is how AI makes people stronger.

Not by removing friction.

By moving friction to the right place.

The loop gives you motion.

The judge gives you direction.

And the human still has one job that should not be outsourced: deciding what kind of direction is worth having.

So build the loop if the work repeats.

Let the machine run when the next step is clear.

But before you walk away, leave behind a judge strict enough to embarrass a beautiful answer, and fair enough to reward a real improvement.

A loop does not make a system evolve.

A loop with a judge does.

[^1]: “Loop Engineering,” 2026-06-07. https://addyosmani.com/blog/loop-engineering/
[^2]: `autoresearch` README. https://github.com/karpathy/autoresearch
[^3]: “How Autoresearch will change Small Language Models adoption,” 2026-03-10. https://www.philschmid.de/autoresearch
[^4]: “The Red Queen Godel Machine: Co-Evolving Agents and Their Evaluators,” arXiv:2606.26294, 2026. https://arxiv.org/abs/2606.26294
