# You'll Build Things You Can't Understand

> 发布日期:2026-06-05 · [中文](../zh/2026-06-05-你迟早会造出自己看不懂的东西.md) | [English](../en/2026-06-05-build-things-you-cant-understand.md)

---

A developer I know shipped a program of about 260,000 lines. He maintains it, fixes every known bug, and adds every new feature people ask for. And he told me, plainly, that he has not directly edited the code since the very first version. The complexity, he said, is already past what one person can hold in his head.

Read that again. He can no longer read his own program. And it keeps getting better.

Your first reaction is probably the one I had: *that's terrifying.* You've lost control. Your skills are rotting. You've become a guy who points at a black box and hopes. This is exactly the future everyone warns about — the one where humans forget how to do the thing, and the machine quietly takes the wheel.

I want to argue the opposite. Not because the fear is wrong, but because it's aimed at the wrong target.

## Control didn't vanish. It moved.

Here's the detail that changed my mind. This developer didn't stop working when he stopped typing code. He started writing documentation — the rules, constraints, and specifications that tell the AI what it may and may not do. That documentation is now around 56,000 lines: roughly 21% the size of the codebase, and the ratio keeps climbing.

Think about what that number means. He didn't pocket the time he saved and walk away. He spent *more* attention than before — just at a higher altitude. He stopped controlling the program by reading each line and started controlling it by designing the constraints every line has to obey. He even abandoned the AI's old "plan mode" because the plans were throwaway hallucinations nobody could review, and replaced them with durable documents that other people — and other AIs — could actually inspect.

That's not a man losing his grip. That's a man moving his grip to a better handle.

And if this sounds like some strange new 2026 predicament, it isn't. It's the oldest move in computing. In 1972, Dennis Ritchie wrote a C compiler — in C. A tool mature enough to build the better version of itself. Today the Rust compiler is written in Rust, the Go compiler in Go. We even have a name for the milestone: self-hosting. When a compiler can compile its own source code, that act isn't a loss of control — it's the proof of correctness. The system that can reproduce itself is the one you can finally trust. We've been building tools we can't fully trace for fifty years. We just called it progress.

## So when *is* it decay?

The honest worry — the one worth keeping — is skill decay. Use a tool long enough and you forget how to do the thing yourself. That's real. But the science is more precise than the slogan, and the precision is everything.

In 2020, two researchers at McGill, Louisa Dahmani and Véronique Bohbot, published a study with a blunt title: habitual GPS use negatively impacts spatial memory. They tracked 50 drivers, then re-tested 13 of them three years later. The finding: the more you lean on GPS, the steeper your decline in the kind of spatial memory that lives in the hippocampus. And they checked the arrow of causation — it wasn't that bad navigators reached for GPS. The GPS came first; the decline followed.

But look at *why*. When you drive on autopilot, a region called the caudate nucleus suppresses the hippocampus. You stop encoding landmarks. You stop building the map in your head. The brain shrinks the muscle you stopped using.

Here's the part the scary headline skips: the damage doesn't come from the tool. It comes from dropping your attention. The driver who still notices "the destination is southeast of that ridge" keeps the hippocampus. The driver who goes blank and just obeys the voice loses it. Same GPS. Opposite brains. The tool never decided — *where the attention went* decided.

That is the whole question, transplanted from your hippocampus to your career. When the machine takes over the typing, the bug-fixing, the routine — where does your attention go? Into the void, or up a level?

## The centaurs already ran this experiment

In 1998, a year after a computer beat him, Garry Kasparov invented "Advanced Chess": a human and a machine playing as one team. People assumed the strongest combination would be the best grandmaster bolted to the best engine. It wasn't.

Reflecting later, Kasparov described what actually won. A *weak* human player, with a *machine*, running a *better process*, beat a strong computer alone — and beat a strong human running a worse process. The deciding variable wasn't the human's raw chess strength or the engine's horsepower. It was the quality of the collaboration. The skill that mattered had migrated: from "find the brilliant move" to "run the human-machine team well."

That is precisely the migration the 260k-line developer made. His value is no longer in writing the loop. It's in designing the constraints the loop has to satisfy — in running the team. The chess players found that out in 1998. The rest of us are finding it out now.

## The frontier admits the same thing

On June 4, 2026 — yesterday, as I write this — Anthropic published a report called *When AI Builds Itself.* The headline number is staggering: as of May 2026, more than 80% of the code merged into their own codebase was written by Claude, their AI. Sixteen months earlier it was a low single-digit percentage. They report engineers merging roughly eight times more code per day than in 2024.

I'll be honest where they were honest: Anthropic itself warns that lines-of-code is a junk metric, and that the 8× number "almost certainly inflates" the real gain. Keep your skepticism. But the direction is not in doubt — AI now writes most of the code that builds the next AI. Tools building their successors, the C compiler trick, at civilizational scale.

And yet. Buried in the same report is the admission that matters most. They cannot yet say their AI has *research judgment* — the ability to choose the right problem to work on in the first place. The machine recovered 97% of a hard research gap in 800 hours of compute, where humans got 23% in a week. It is staggeringly good at solving the problem in front of it. It still can't reliably decide *which* problem is worth solving.

That gap — deciding what's worth doing — is the handle you move your grip to. It's the documentation, the constraint, the direction, the taste. It is the last thing to be automated, and the first thing you should be pouring your freed-up attention into.

## You will build things you can't understand

So here is where I've landed.

You *will* build things you can't fully understand. Not as a failure. As the direction of travel. The systems are getting bigger than any single head, and pretending otherwise just means someone else builds them and you don't. That part isn't up for debate.

What *is* up for debate — the only thing that is — is what you do with the attention the machine hands back to you.

Decay is not "you stopped doing it by hand." Decay is pocketing the saved hours and buying nothing with them. It's letting the caudate nucleus switch off the hippocampus. It's playing the strong-human-bad-process game and losing to a kid with a laptop and a better method.

The opposite of decay isn't refusing the tool. It's reinvesting upward. Take the time the machine gives you and spend it on the things it still can't do: choosing the right problem, designing the constraints, holding the direction, building the system that improves itself. Your carbon hours are capped at twenty-four a day. The machine's hours aren't. The entire game — the *whole* game — is what you point your scarce attention at once the machine has freed it.

Build the thing you can't read line by line. Just make sure you can still say, better than the machine ever could, why it's worth building at all.

---

## Sources

- Anthropic Institute, *When AI Builds Itself* (June 4, 2026) — anthropic.com/institute/recursive-self-improvement. >80% of merged code authored by Claude as of May 2026; Anthropic's own caveat that lines-of-code inflates productivity gains; task-horizon doubling ~every 4 months; the open question of AI "research judgment."
- L. Dahmani & V. D. Bohbot, "Habitual use of GPS negatively impacts spatial memory during self-guided navigation," *Scientific Reports* (2020). 50 drivers; 3-year follow-up; hippocampus-dependent spatial-memory decline; caudate-nucleus inhibition mechanism.
- G. Kasparov, "The Chess Master and the Computer," *The New York Review of Books* (2010); Advanced Chess launched 1998; freestyle "centaur" tournaments 2005–2008.
- "Bootstrapping (compilers)," Wikipedia; Dennis Ritchie's first C compiler (~1972, Bell Labs); self-hosting as a validation milestone.
- Anchor case (260k-line "CodePilot" project, ~21% documentation ratio): from the author's own development notes, recounted with permission of the idea, not the identity.
