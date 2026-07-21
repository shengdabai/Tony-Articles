# Parallel Work Needs Separate Rooms

> 发布日期:2026-07-21 · [中文](../zh/2026-07-21-并行不是开更多窗口而是给任务分房间.md) | [English](../en/2026-07-21-parallel-work-needs-separate-rooms.md)

---

A lot of people are discovering a new kind of ambition.

Not "I want to finish this task faster."

That was the first layer of AI.

The new ambition is: "I want ten useful things moving at the same time."

One agent cleans up an old module. Another checks a failing test. Another rewrites a page. Another researches a small market. Another turns notes into a draft. Another builds the first version of a tool that may or may not survive the week.

At first glance, this looks like abundance. The old bottleneck was human hands. Now the hands are cheap. Start another session. Open another tab. Give the machine another job. Let silicon time run while carbon time sleeps.

But a strange thing happens as soon as parallelism becomes cheap.

The bottleneck moves from doing to containing.

Can the tasks stay separate? Can the system remember who is changing what? Can you tell which result is worth keeping? Can you stop one thread without poisoning another? Can you review the work without loading the whole mess back into your own head?

If the answer is no, you do not have parallel work.

You have parallel confusion.

This is why an old developer tool suddenly feels philosophical to me: Git worktree.

Git's own documentation describes worktree as a way to manage multiple working trees attached to the same repository. In plain language, the same codebase can have more than one working directory, so different branches or experiments can be checked out at the same time.[^1] GitHub's write-up of Git 2.5 in 2015 framed the new `git worktree` command as a way to create additional working trees connected to an existing repository, avoiding some of the overhead of maintaining separate clones.[^2]

That fact is technical.

The lesson is larger.

A branch is a route. A worktree is a room.

The branch says: this line of work is going in a particular direction.

The room says: this work has a physical place to happen.

Before AI, many people could survive with only routes. You worked on one thing, switched branches, changed context, came back, kept enough in your head, and paid the switching cost yourself. It was annoying, but the human pace limited the damage.

AI changes the damage profile.

If one person can launch five or twenty code tasks, the cost of not having separate rooms compounds quickly. A task that should have been isolated starts touching shared files. A quick fix changes the assumptions of a larger refactor. Two agents each make locally reasonable decisions that become globally incoherent. You return later and cannot tell which edits belong to which intention.

The problem is not that AI is bad at parallel work.

The problem is that humans often ask for parallel output before designing parallel space.

This happens outside programming too.

In writing, parallel space means separate drafts for separate theses, not one giant document full of half-born arguments. In learning, it means one notebook or project per line of inquiry, not a pile of highlights pretending to be thinking. In business, it means one experiment has its own audience, promise, price, and success criterion, not ten ideas competing inside one vague plan. In personal productivity, it means your calendar, task list, inbox, and notes are not all secretly the same dumping ground.

When rooms are missing, intelligence leaks.

You can have a strong model, a long context window, a beautiful prompt, and still get poor results because the work has no boundary.

That is the part many people do not want to hear. They want AI to rescue them from structure. In reality, AI rewards structure. It makes a structured person stronger and an unstructured person noisier.

This is also where "using AI to become lazy" and "using AI to become stronger" separate.

The lazy version says: I do not want to think through the task, so I will ask the model to handle everything.

The stronger version says: I will think harder about the shape of the task so the model can work in a smaller, cleaner, more reviewable room.

The first version produces motion. The second version produces leverage.

Leverage always needs a container.

Water turns a wheel only when there is a channel. Electricity becomes useful only when there is a circuit. A factory produces reliably only when materials, stations, quality checks, and exits are separated. Without containment, more energy often means more damage.

AI is energy.

Worktree is one small example of a container.

The deeper container has four parts.

First, a task needs a boundary.

What is this task allowed to touch? What is it explicitly not allowed to touch? If the task is "improve the product," the room is too large. If the task is "replace the empty state copy on one page and do not change layout," the room is small enough to inspect.

Second, a task needs a finish line.

Not a vibe. Not "make it better." A finish line. A test passes. A page renders. A draft reaches a specific shape. A report contains three sourced findings. A prototype can be opened by another person. Without a finish line, parallel work becomes infinite because no thread knows when to stop.

Third, a task needs a merge rule.

Parallelism is not the same as acceptance. An agent can finish work that should not be merged. A draft can be interesting and still not belong in today's article. A feature can work and still make the product worse. If every output is treated as progress, the system will fill with clutter.

Fourth, a task needs a recovery path.

What happens if this thread fails? Can we discard it cleanly? Can we compare it with another route? Can we keep the useful part and throw away the rest? A good room has a door. A bad room becomes a trap.

These four things sound ordinary because they are ordinary.

That is why they matter.

The AI age keeps pushing us toward spectacular words: agents, graphs, orchestration, autonomous teams, self-evolving systems. I like these words when they point to real mechanisms. But the mechanism often begins with something humble: give each piece of work a place, a boundary, a finish line, a merge rule, and a way to leave.

Only then does the exciting part become sane.

I think this is one reason the old distinction between "technical person" and "non-technical person" is becoming less useful.

In the past, if you did not write code, Git worktree sounded like someone else's concern. Today, the concept matters even if you never type the command. The question is no longer only "Can you program?" It is also "Can you arrange work so that intelligence can operate without destroying its own context?"

That is an engineering question, but not only for engineers.

A teacher designing student practice needs rooms. A creator testing three content directions needs rooms. A small business owner trying five offers needs rooms. A learner exploring AI tools needs rooms. A founder asking agents to build prototypes needs rooms.

The surface tools differ.

The discipline is the same.

Separate the work enough that feedback becomes readable.

This is the real meaning of parallelism. It is not opening more windows. It is making more clean feedback possible per unit of time.

If five agents work for five hours and you need ten hours to understand what happened, you did not gain much. If three small threads run independently and each returns a clear yes, no, or maybe, you have increased your learning rate. The goal is not maximum activity. The goal is maximum clean signal.

That last word matters: clean.

A messy signal is worse than no signal because it feels like evidence while hiding confusion. You cannot learn from an experiment if three other experiments changed the same condition. You cannot judge a refactor if an unrelated feature slipped in. You cannot evaluate a writing direction if it is mixed with a different argument. You cannot know whether AI helped if you never defined what help would look like.

So before asking AI to do more, ask a more boring question:

Where will this work live?

That question sounds too simple. It is not.

It forces you to name the task. It forces you to separate intention from mood. It forces you to decide what counts as completion. It forces you to protect the rest of the system. It forces you to think like someone responsible for more than one pair of hands.

This is why the "one-person team" idea is both real and dangerous.

It is real because AI gives one person access to many temporary workers. It is dangerous because many people hear "team" and imagine labor, but forget management. A team without roles, spaces, standards, and review is not a team. It is a crowd.

AI can give you a crowd very quickly.

You have to build the team.

And building the team begins before the first prompt.

It begins with the room.

For me, this connects back to a simple long-term belief: real growth is not just adding capability. It is learning how to hold more capability without being deformed by it.

More memory requires better retrieval. More tools require better permissions. More output requires better taste. More automation requires better recovery. More agents require better rooms.

Every increase in power asks for a matching increase in structure.

Ignore that, and AI becomes another way to manufacture overwhelm.

Respect it, and something different becomes possible. A person does not merely work faster. A person learns to run several clean learning loops at once. Not by pretending to be a machine, and not by surrendering judgment to the machine, but by designing the environment in which machine work can become human progress.

That is the part worth practicing.

Not "How many agents can I launch?"

But "How many independent lines of work can I keep understandable, reviewable, and reversible?"

That is a much better measure of strength.

Because the future will not reward the person who can create the most motion.

It will reward the person who can create the most clean motion, keep the signal, discard the noise, and return tomorrow with a system that is stronger than it was today.

Parallel work does not begin with more windows.

It begins with separate rooms.

[^1]: Git, "git-worktree Documentation." https://git-scm.com/docs/git-worktree
[^2]: GitHub Blog, "Git 2.5, including multiple worktrees and triangular workflows," 29 July 2015. https://github.blog/open-source/git/git-2-5-including-multiple-worktrees-and-triangular-workflows/
