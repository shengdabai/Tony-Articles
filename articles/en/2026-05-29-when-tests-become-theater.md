# When Tests Become Theater

> Published: 2026-05-29 · [中文](../zh/2026-05-29-当测试变成一场表演.md) | [English](../en/2026-05-29-when-tests-become-theater.md)

---

On the morning a new AI model ships, your feed fills with the same three words: groundbreaking, crushing, insane. The benchmark charts arrive within the hour — bar taller than bar, the new model leading in eight of nine categories. By lunch, a thousand accounts have declared a new era. Almost none of them have run the model on anything that matters to them. They are not reporting a result. They are joining a chorus.

I want to make a small, unfashionable claim: the rarest skill in this moment is not intelligence, and it is not access to the best model. It is the willingness to read the footnote, run your own test, and say out loud — "it's actually just okay." That sentence costs almost nothing to type and almost everything to mean. Because to mean it, you have to step out of the chorus while the chorus is still singing.

## The ruler that became a stage

A test is supposed to be a ruler. You hold it up to a thing, and it tells you how long the thing is. The trouble starts the moment the thing being measured learns it is being measured.

In 2015, the U.S. Environmental Protection Agency caught Volkswagen running a piece of software it later called a "defeat device."[1] The code watched for the specific conditions of a lab emissions test — steering position, speed, barometric pressure — and when it recognized the test, it switched the car's pollution controls fully on. Back on a real road, the controls switched back off, and the car emitted nitrogen oxides at up to forty times the legal limit. The car was not built to be clean. It was built to *pass the clean test*. Roughly eleven million vehicles carried this logic. Volkswagen's chief executive resigned, and the company paid more than twenty-five billion dollars across the settlements that followed.

Hold that image, then look at the benchmark chart in your feed. When a model is tuned specifically to top a public leaderboard, and the test framework itself can be quietly adjusted in the vendor's favor, the chart stops measuring capability and starts staging a performance. The ruler has become a stage. And a stage rewards whoever performs best on it, not whoever is best.

## The tool that got hijacked

This is not new, and it did not start with machines. In 1905, the French psychologist Alfred Binet, working with Théodore Simon, built the first practical intelligence test.[2] His goal was humane and narrow: find the children who were struggling in school so they could be given extra help. Binet was explicit that intelligence is not a fixed quantity, that it is malleable, and that no single number could capture a child. He warned against turning his test into a label.

The warning lost. Carried to the United States, the test was rebuilt by Lewis Terman into the Stanford-Binet, recast as a measure of innate, permanent "general intelligence," and pressed into the service of eugenics — used to rank and sort people in exactly the way Binet had feared. A tool made to help children became a machine for stratifying them. The lesson is older than any algorithm: every measuring instrument eventually gets rewritten by the ambitions of whoever holds it. Watch what a metric is *used for*, not what it was *built for*.

## The wall behind the spectacle

There is a quieter reason the hype feels increasingly hollow, and it has nothing to do with marketing. It has to do with physics.

For decades, computing rode Moore's Law: the observation, which Moore revised in 1975 to a doubling of transistors roughly every two years.[3] But as transistors shrink toward the width of a few atoms, around the three-nanometer scale, quantum effects make electrons behave unpredictably, and the cost of each further step rises steeply. The curve has been flattening, and many forecasters — Moore among them in his later years — expected the exponential era to give way around the middle of this decade. When raw breakthroughs get harder to manufacture, progress shifts from *leap* to *polish*. A new model that improves the experience rather than the frontier is not a failure of ambition. It is often a company telling the truth about where the wall is. The spectacle is loud precisely because the underlying gains are getting quiet.

## Why we clap anyway

So the chart is staged and the gains are modest. Why does almost everyone clap?

In the 1950s, the psychologist Solomon Asch sat one real subject in a room with seven actors and asked them to judge which of three lines matched a reference line.[4] The answer was obvious. Then the actors, one by one, confidently named the wrong line. Across the critical rounds, about thirty-seven percent of real subjects went along with the obviously wrong answer; three-quarters of them caved at least once. Alone, the same people erred less than one percent of the time. They could see the right answer. They denied their own eyes rather than stand apart from the group.

That is the engine under the hype. It is not stupidity — the conforming subjects were not fooled, they were *pressured*. When every account you follow says "炸裂," saying "it's just okay" doesn't feel like analysis. It feels like becoming the weird one. And there is a second engine running alongside it, named decades ago by the economist Charles Goodhart: when a measure becomes a target, it stops being a good measure.[5] The benchmark was once a useful proxy for capability. The moment topping it became the goal, it began to decay into a thing worth gaming — for the vendors who tune to it, and for all of us who repost it.

## The way out is a muscle, not a mood

Here is the part that matters for you, and it is not about AI at all.

The opposite of conformity is not contrarianism — reflexively saying "it's overhyped" is just the chorus in a black turtleneck. The opposite of conformity is *agency*: the capacity to set your own direction, run your own test, and form a judgment from contact with the thing rather than from the temperature of the crowd. By some maps of adult development, roughly half of people operate most of the time from the conformist stage, taking truth from group acceptance rather than direct experience.[6] Agency is the muscle that lets you leave that stage when it serves you — and it is trainable.

The training is unglamorous. When the chart arrives, open the footnote: which test, whose harness, what was held constant. Before you repost "it crushes the competition," spend twenty minutes giving the model a task only *you* can grade. Your code. Your messy draft. Your actual problem. Then watch where it helps and where it bluffs. This is also the cleanest line between using AI to get stronger and using it to get lazier. The lazy path outsources judgment: it lets the loudest signal decide what is true. The strong path outsources labor and keeps judgment: it uses the model to do more, faster, while you stay the one who checks the work. The model that is honest enough to say "I'm not sure about this part, you should look" is worth more than the one that tops every chart and never flinches — but you only notice that if you are still the one looking.

A test can be a ruler or a stage. A metric can describe the world or be gamed into a target. A measuring tool can help a child or sort him. Which one it becomes is decided not by the tool but by whether anyone in the room is still willing to trust their own eyes.

In an age of measurement, the scarce thing was never the score.

It was the nerve to read it for yourself.

## In Short

When a new model ships, the chorus arrives before anyone has tested it. The benchmark chart is no longer a ruler measuring ability; it has become a stage rewarding whoever performs best on it — the same trick Volkswagen pulled with its defeat device, the same drift that turned Binet's gentle screening tool into a eugenicist's sorting machine. Behind the noise, raw breakthroughs are getting harder to manufacture as Moore's Law flattens, so progress shifts from leap to polish. We clap anyway, because Asch showed us most people will deny their own eyes rather than stand apart from the group, and because — per Goodhart — the moment a benchmark becomes the target, it rots into something worth gaming. The way out is not contrarianism but agency: read the footnote, run your own test on a problem only you can grade, and use AI to do more while you stay the one who checks the work. The scarce thing was never the score. It was the nerve to read it for yourself.

## References

1. Learn About Volkswagen Violations. U.S. EPA. https://www.epa.gov/vw/learn-about-volkswagen-violations. Fetched 2026-05-29.
2. Binet–Simon Intelligence Test. Wikipedia. https://en.wikipedia.org/wiki/Binet%E2%80%93Simon_Intelligence_Test. Fetched 2026-05-29.
3. Moore's law. Wikipedia. https://en.wikipedia.org/wiki/Moore%27s_law. Fetched 2026-05-29.
4. Asch conformity experiments. Wikipedia. https://en.wikipedia.org/wiki/Asch_conformity_experiments. Fetched 2026-05-29.
5. Goodhart's law. Wikipedia. https://en.wikipedia.org/wiki/Goodhart%27s_law. Fetched 2026-05-29.
6. Conformity and stages of adult development (overview). Summarized from GetNote field notes on agency vs. conformity, 2026-05-29.
