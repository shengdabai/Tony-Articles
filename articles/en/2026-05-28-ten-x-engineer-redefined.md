# The 10x Engineer Just Got Redefined — And Most People Missed It

> Published: 2026-05-28 · [中文](../zh/2026-05-28-十倍工程师的定义变了.md) | [English](../en/2026-05-28-ten-x-engineer-redefined.md)

---

There's a sentence buried in my notes from this week that I keep coming back to:

> The definition of a 10x engineer has shifted. It's no longer "the one who writes code fastest." It's "the one who builds the best review pipeline."

I wrote that line at 6:57 AM on a Thursday, sandwiched between two cups of coffee. At the time I thought it was just a clever reframe. Three days later I'm convinced it's the single most important thing I've understood about engineering in the AI era.

And almost nobody is talking about it.

## The old game is over

For twenty years, the productivity ceiling for an engineer was "how fast can you turn an idea into working code." Speed of typing. Speed of debugging. Speed of recall. Speed of decomposition. Stack Overflow as a reflex. Copy-paste as a craft.

That entire game is over. Not slowing down — *over*.

When Claude, Codex, and Cursor can each take a spec and spit out 800 lines of plausible TypeScript in twenty seconds, the bottleneck has moved. It has moved so completely that engineers who keep optimizing for "how fast can I produce code" are sprinting on a treadmill that's been unplugged.

The new bottleneck — the only bottleneck that matters — is:

**How do you tell, in the next 90 seconds, whether the 800 lines of plausible code in front of you are actually correct, actually maintainable, actually safe to ship?**

That is a completely different skill. And it's the skill almost nobody has been training.

## A 19th-century answer to a 21st-century problem

The first time I tried to articulate this to a friend, he pushed back: "You're describing code review. We've had code review forever. What's new?"

Here's what's new. Code review used to be one human reading another human's code. Slow on both sides, but symmetric. The reviewer roughly understood how the code got written, because they themselves could have written it. Trust was bounded by mutual comprehensibility.

That symmetry is gone. The thing producing the code now is faster than you by a factor of fifty, occasionally hallucinates with full confidence, and has no stake in whether the product works in production six months from now. Reviewing its output is not the same activity as reviewing a colleague's pull request. It's closer to something the scientific community figured out 360 years ago.

In 1665, the Royal Society of London started a strange practice: before a scientist could publish a discovery, several other scientists — chosen for independence, not friendship — had to read the manuscript and try to break it. They invented peer review because they realized that as the volume of claimed discoveries grew, no single editor could vet them all. The only scalable defense against confident-sounding nonsense was *structured cross-checking by independent experts.*

Three and a half centuries later, *Nature* receives about 10,000 submissions a year and publishes fewer than 700. Roughly 4 million peer-reviewed papers ship globally each year. The system is slow, expensive, frustrating, occasionally captured — and it is still the best mechanism humanity has invented for distinguishing real findings from compelling-sounding garbage.

That mechanism is what engineering needs now. Not because AI is dumb. Because AI is *confidently fluent at scale*, and that combination is exactly what peer review was designed to defeat.

## What "building a review pipeline" actually looks like

I have a friend named Lawson who runs a small engineering team. Last month he stopped letting his developers ship anything that hadn't passed through three independent AI reviewers: a Claude sub-agent that checks logic, Codex examining the same diff fresh, and Cursor's Bugbot looking for security issues. Three models, three independent passes, no shared context between them.

The first time he showed me the setup I thought it was overkill. The third time I saw it catch a subtle race condition that would have silently corrupted user data in production, I stopped thinking that.

This is the Roman Triumvirate principle applied to software. When Caesar, Crassus, and Pompey formed the First Triumvirate in 60 BC, the whole point of the arrangement was *mutual constraint*. Each one had independent power; none could act unilaterally without the other two noticing. The system held until Caesar consolidated power and broke it — and then Rome collapsed into civil war.

If you let a single AI model ship code unchecked, you are betting your product on a Caesar with no Crassus and no Pompey. The model has no incentive to flag its own hallucinations, because from its perspective they aren't hallucinations — they're just the next plausible token.

So you stop trusting any single model. You build a pipeline. The pipeline becomes the product. The pipeline is now what you ship.

## The Therac-25 problem

If you think this is paranoid, let me tell you about Therac-25.

Therac-25 was a radiation therapy machine built by Atomic Energy of Canada Limited in the early 1980s. Between 1985 and 1987, it gave at least six patients radiation doses roughly one hundred times higher than prescribed. Four people died. Two more were permanently maimed.

The cause was not the radiation hardware. The cause was that the engineers had inherited code from the previous machine, Therac-20, which had relied on physical hardware interlocks to prevent overdoses. When they built Therac-25, somebody decided the software was reliable enough that the hardware interlocks weren't needed. Cheaper that way. Faster that way. The software would do the safety work.

There was a race condition. If an operator entered a specific keystroke sequence within eight seconds, the safety check was bypassed silently. No error, no warning. Just a fatal dose of radiation.

The investigation found that AECL had never submitted the code for independent third-party review. They never ran combined hardware-software stress tests. They were confident. They saved time. The savings cost lives.

I keep this story close because every shortcut argument I hear about AI-generated code is some local version of it. *"This is a small tool, we'll review later." "This is just an internal script, it doesn't need scrutiny." "The model probably got it right."* These sentences are the linguistic ancestors of "the software interlocks are sufficient."

The Therac-25 engineers were not stupid. They were under deadline pressure, surrounded by code that mostly worked, in a culture that treated review as a tax on velocity. Sound familiar?

## Why this requires unlearning, not learning

Here is the part most engineers will resist, and it's the part I want to be honest about: the muscle this new game requires is almost the opposite of the muscle we spent a decade building.

For most of our careers, being a great engineer meant being able to *hold the entire system in your head*. You read the diff because you wrote the surrounding code. You spotted the bug because you remembered why the old code worked. Your intuition was a compressed memory of past battles.

When the AI writes 800 lines you've never seen, in patterns you didn't choose, touching libraries you haven't used, that intuition fails you. It fails *quietly*. The code looks fine. The tests pass. The PR description sounds confident. Nothing pings your gut, because your gut was trained on a different game.

The skill you need now is the opposite of intuition. It's a *checklist*. It's a *protocol*. It's the discipline of asking, every single time, three brutal questions:

1. What is this code claiming to do, in one sentence?
2. What is the cheapest experiment that would prove it false?
3. If I'm wrong about question 1, who pays the price, when, and how much?

These questions are not impressive. They are not clever. They will not make you sound smart in an interview. They are the engineering equivalent of a surgeon counting sponges before closing — the boring discipline that separates people who ship working systems from people who ship confidently-broken ones.

## The Fabian strategy, applied to your pull request

There is an ancient Roman general named Fabius Maximus who is almost forgotten today, because his greatest achievement was *not fighting battles*. In 217 BC, facing Hannibal — who was destroying every Roman army that took the field against him — Fabius did the unthinkable. He refused to engage. He shadowed Hannibal's army, harassed his supply lines, took small victories, and waited.

The Roman Senate hated him for it. They called him *Cunctator* — "the Delayer." It was an insult. They wanted glory; he gave them patience. Years later, when Hannibal's army had bled out from a thousand small wounds, the same Senate realized that Fabius had won the war by refusing to lose it.

This is the strategy I am asking you to apply to your engineering practice this year. The AI tools will keep getting faster. Your competitors will keep shipping more, faster, louder. Some of them will get rich on the velocity. Most of them will ship the 21st-century equivalent of Therac-25 and won't know it until somebody gets hurt.

The Fabian play is this: slow down where it matters. Write the spec first. Decompose the change into pieces a human can hold in working memory. Run three reviewers across the diff. Keep the test suite ruthless. Don't ship until you can explain, in a single sentence, what could go wrong and how you'd notice.

This will feel like losing. It will feel like the people around you are pulling ahead. They are not. They are sprinting on the unplugged treadmill.

## What this means for what you practice tomorrow

If I had to give one piece of concrete advice — to a junior engineer asking me what to learn, or to my future self looking back at this moment — it would be this:

**Stop practicing how to write code faster. Start practicing how to review code you didn't write.**

Specifically:

- Each day, take one AI-generated diff and find one real flaw in it. Not a style issue. A real flaw. Write down what tipped you off.
- Each week, set up one new automated check that catches a bug class you've personally been burned by. Build the pipeline brick by brick. Make the pipeline your moat.
- Each month, review a piece of code in a domain you don't know well, and force yourself to articulate what you *can't* judge. The edges of your judgment are where the real risk lives.

The Japanese designer Manabu Mizuno wrote that taste is "the ability to make things look beautiful, accumulated through the patient collection of knowledge." His students trained by cataloging three good designs and three bad designs every day. After six months, they could judge the quality of a layout in half a second.

The same protocol works for code review. You're not training to be smarter than the AI. You're training to be the human whose half-second judgment is worth more than the AI's twenty-second generation.

## The line that won't let me go

The reason I keep coming back to that sentence from my Thursday morning notes is that it's an answer to a question I've been carrying around for two years: *what is the work that's still mine?*

The honest answer used to scare me. If the AI can write the code, what's left? If the AI can outline the doc, what's left? If the AI can scaffold the product, what's left?

Here's what's left. Judgment. Restraint. The patience to slow down when everyone around you is speeding up. The willingness to say "I don't trust this output yet" when the output looks beautiful. The discipline to build a pipeline that catches your own blind spots before they catch you.

The 10x engineer of 2020 was the person who could produce ten times more code than their peers. The 10x engineer of 2026 is the person whose review pipeline catches ten times more failure modes before they ship.

That role is wide open right now. Most engineers haven't realized the game changed. The treadmill is unplugged but the LED is still blinking, so people are still running.

You can stop running. You can walk over to where the new game is being played. The court is mostly empty. The ones already there will tell you it feels strange at first — slower, less glamorous, harder to brag about at parties.

And then, six months in, you'll catch a Therac-25-grade bug in a Friday afternoon diff, and you'll understand exactly why you're worth what you're worth.

That's the work that's still ours.

That's the work I'm betting my next decade on.

---

*Tony Sheng · 2026-05-28*
