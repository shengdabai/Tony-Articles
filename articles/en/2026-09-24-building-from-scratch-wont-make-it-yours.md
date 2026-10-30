# Building from Scratch Won't Make It Yours

> 发布日期:2026-09-24 · [中文](../zh/2026-09-24-从零做不会让产品更像你.md) | [English](../en/2026-09-24-building-from-scratch-wont-make-it-yours.md)

---

Suppose I wanted to build a small tool for organizing reading material today. I would start with a working template, then add the simplest way to enter an item and save it. Within hours, the page might already look like a product: a title, a button, and a tidy result. The tempting next move would be to add animations, recommendations, and a more polished interface.

I would rather pause at a less attractive question. Does anyone need this particular workflow? If so, where would they give up? Writing every line myself might feel satisfying, but my satisfaction would not finish the user's task. AI has made it easier to produce a convincing beginning. That makes it more important to decide where my attention should go next.

Here is my view: a product becomes distinct through the specific problem its maker keeps taking responsibility for, not through inventing every layer from scratch. We can borrow the common parts. We cannot borrow our understanding of the part that actually matters. That distinction determines whether AI helps me produce a good demonstration or a tool someone can return to.

## Why starting from scratch can send effort to the wrong place

A blank page is seductive because every choice appears to be yours. You design the layout, write the sign-in flow, store the data, and connect payments. Each completed component looks like progress. But a growing collection of components tells us only that the tool is becoming more complete. It does not tell us whether somebody can now finish the job that brought them to it.

AI can generate those components quickly, which is a real advantage for a person without a full development team. You describe an idea and soon have a sidebar, cards, and notification boxes. It can feel as if a few more features will make the product ready. Yet speed can conceal a question: am I removing friction from a user's work, or am I removing the discomfort of having to find out what a user actually needs?

Think of someone preparing to sell breakfast. They could learn to build an oven from raw metal, and that might be an excellent way to learn about mechanics and materials. But if customers need a breakfast that tastes right and is ready before work, a dependable oven leaves more time to work on the recipe, pickup, and service. The comparison is useful because a standard tool handles common problems while the maker faces the need that remains unsolved.

The comparison has a limit. A software template does not always reveal what is inside it as clearly as a kitchen appliance does. It might make data hard to export, fail a security requirement, or make later changes expensive. Starting with an existing tool therefore calls for checking who controls the data, whether it can be moved, and which parts of the workflow can be changed. Borrowing is a decision about boundaries, not a pledge of trust.

The part worth building ourselves often becomes visible only during use. A reading tool may already have adequate sign-in and layout, yet still fail to turn scattered excerpts into clues a reader can find later. In that case, the organizing and retrieval flow deserves our effort. If the only complaint is that the button lacks a distinctive shape, I would have a harder time calling a rebuild necessary.

Design and engineering still matter. People may leave a tool that is ugly, slow, or unreliable. A usable baseline gets the tool into the room; it does not tell me which detail is worth maintaining for years. Rebuilding every component I could buy, borrow, or reuse might consume the attention I need to discover that detail.

## Where users stop is where the product question begins

It is easy to treat a working feature as a full stop. I now see it as the start of a question: can someone use the tool to do their own work without my explanation? Where do they hesitate, go back, or return to their old method? Those actions can reveal a more useful next step than my description of what the product is supposed to be.

In [his 2013 essay for founders](https://paulgraham.com/ds.html), Paul Graham describes how the Viaweb team built online stores for merchants by hand in the early days. Midway through the work, they would discover a missing software feature, add it, and then continue helping the merchant. What interests me is the sequence: a real task got stuck before the feature entered the product. This is founder advice and a first-person account, not an experiment showing that the same approach will make every product succeed.

[GreenPal founder Bryan Clayton's account](https://buffer.com/resources/bootstrapping-growth/) offers another concrete detail. His team asked early customers how they normally found lawn care. Customers said they first asked family and friends; if that failed, they searched for nearby services. The company then worked on content for searches in smaller surrounding towns rather than relying on a broad market slogan. I can take this as the founder's account of a change in direction. One retrospective story cannot isolate which step caused growth.

Neither story is an instruction to copy a store-building service or a search strategy. They show a way of working: let a person carry their original task through the process, then decide what to build from the place where the task breaks. An early user cannot represent everyone, but their point of failure can expose the false smoothness of a flow that only its creator understands. Seeing different people stop in the same place would strengthen the judgment.

There is a harder possibility, too: the problem may not be inside the product. Perhaps this person does not have the need at all. Perhaps an existing tool is good enough, or the inconvenience is tolerable while changing habits is not. Adding features is an easy way to avoid these answers. I would rather accept them as evidence that I have not yet found the piece of work worth owning.

That is why I want to record praise for a beautiful page separately from evidence that someone completed a task. The praise is welcome; completing a task exposes the costs of time, steps, understanding, and trust. Even when someone goes back to their old method, learning why gets me closer to an answer than staring at a demo and guessing what people want.

## After borrowing the tools, where should learning happen?

The strongest objection to templates and AI is that touching less of the underlying system may leave us understanding less. There is reason to take that seriously. In [a 2026 randomized study by Anthropic](https://www.anthropic.com/research/AI-assistance-coding-skills), 52 mostly junior software engineers worked with a Python library they did not know, a ready-made set of programming tools. On a quiz immediately after the task, the AI-assisted group averaged 50% and the hand-coding group 67%. The AI group finished about two minutes sooner on average, but the sample did not provide enough evidence to conclude that AI actually made the task faster. The study did not establish what happens to long-term skill, or what would happen on every kind of development task.

I do not read that as a verdict against AI, and the researchers do not present it as one. Their observations distinguish how people used the assistant. Some delegated the code and skipped understanding it. Others asked follow-up questions, sought explanations, or worked through concepts before coding. Those latter patterns appeared alongside higher quiz scores, but that qualitative analysis cannot prove that a particular way of asking caused the scores. It does remind me that delivery speed and my ability to catch a future error belong in separate accounts.

Another study makes the alternative more concrete. [An exploratory trial reported in 2025 by the Google LearnLM team and Eedi](https://arxiv.org/abs/2512.23633) involved 165 students across five UK secondary schools. Expert tutors supervised every AI-drafted message in mathematics tutoring and could revise it before it reached a student. In the authors' abstract, the group supported by LearnLM solved subsequent novel problems at a rate of 66.2%, compared with 60.7% for students tutored by humans alone. I have checked the authors' abstract, not the paper's full methods. The supervised setup cannot tell us that an unsupervised tutor would perform the same way.

Taken together, these studies support a conditional judgment of my own: useful AI need not always carry us over the difficult part. It can help expose the difficulty so we can practice making a decision. While building a tool, I can ask why information is arranged a certain way inside the program, under which conditions two implementations might fail, and what I should expect before running either one. If I simply paste an answer until the page works, I may be skipping the understanding I will need when I have to maintain it.

Learning does not require reading every textbook from the first page. It can follow the gap that actual use reveals. If people cannot find what they saved, learn about retrieval and information organization. If exports repeatedly fail, understand the format and its limits. If a slow page prevents completion, measure the delay instead of guessing. Time saved by using existing tools should return to questions with consequences for the user's task.

[A 2016 learning experiment](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.01977/full) suggests a practical method. Students studied passages, tried to recall ideas without looking, received feedback, and later applied the ideas to questions in a different knowledge domain. In the second experiment, recall practice beat rereading, but its advantage became smaller when the rereading group also received focused exposure to the key information. Trying to remember and attending to the feedback both matter; this is no license to make struggle a virtue in itself. Applying these findings to product builders is my inference. The study did not test product development.

So I want to keep one simple habit. Whenever AI helps me through a real obstacle, I can close its answer and explain, in my own words, the problem, the change, and a new failure the change might create. Then I can try a related but different case. If I cannot explain it, I should keep investigating rather than treating a fluent explanation as a skill I possess. The point of spending that extra time is to be able to change and maintain the tool later. I will know whether it worked only when I can handle the next case more independently.

## Won't templates make every product look the same?

They can, and saying "just add personality" does not settle the issue. When everyone uses the same page structure and the same AI-generated patterns, products can converge in their first screen, wording, and interactions. More seriously, a template may determine where data lives, how permission works, and who can fix a failure. If those constraints block the user's essential task, borrowing the template is no longer a bargain.

Writing everything yourself does not automatically create a meaningful difference, either. A wholly custom form may still be an ordinary form. A tool built on existing software may earn repeat use because it makes one neglected step work. My comparison is this: what burden did this choice remove from the user, and what maintenance responsibility did it give me? The maker's effort is a cost, not proof of value.

When a tool handles highly sensitive data or faces strict industry requirements, its components need a higher standard of review. Owning the core implementation may be necessary if the dependency itself creates the problem. For a low-risk experiment whose data can easily be moved, borrowing a reliable foundation may make the need easier to see. Both decisions require evidence. Neither "custom is safer" nor "templates are faster" is enough on its own.

Someone might also argue that apparently unnecessary work from scratch can lead to unexpected discoveries. I agree. Exploring a technology or learning a craft can be the purpose of a project. In that case, judge it by what was learned, not by how many people use it. Trouble begins when a practice project is described as a product that already solves a real problem, or when users are asked to pay for the maker's learning with their own time.

Here is a standard I would use. If replacing the template would not clearly improve the user's essential action, wait before rewriting it. If it would, describe the improvement precisely and replace only enough to test it in real use. A rebuild then answers a constraint we have observed, instead of soothing our fear that the product looks too ordinary.

## Try it with one small project today

Choose a recurring nuisance in your own life that another person could also test independently. For instance, you might want to turn scattered public reading links into a list you can search later. Do not begin by planning a grand "knowledge operating system." Write down the starting point and finish line: the person has a few links and, after leaving the page, can find the one they need. This is a hypothetical exercise, not a product I claim to have validated.

Next, use a template or the plainest available tool to make a complete path. Record the boundaries of what you borrowed: Can the information be exported? Who can see it? What cannot be changed? Then ask someone willing to try it to use their own public material. Do not click the buttons for them or explain every pause. Record what they intended to do, what they actually did, and whether they needed to return to their old method.

After watching, make a prediction that could be wrong: perhaps they cannot find an item because saving it gave them no clue they will remember later. Change only that step. You might ask for a sentence describing the future question that would lead them back to the item. Leave the homepage, animation, and model alone. Let that person, or another user, try again and see whether the point of failure moves. If it does not, admit the prediction was wrong and go back to the observed action.

Use AI in two places along the way: to connect the standard parts, and to challenge technical choices you do not yet understand. Before delivering an important change, close the AI answer and explain what happens with empty, duplicate, or unexportable content. That is a small exercise in recalling what you learned and testing it in a nearby situation. It is not a security audit, and it cannot replace feedback from an actual user.

There is a tougher question for the reader, too. If you covered up the polish, the feature count, and the pride of saying "I wrote it all," why would this person come back? If the answer depends entirely on the demonstration, there may not yet be a task worth owning for the long term. If it points to a recurring action that current tools still handle badly, the project has a reason to continue, even if its first version borrows a great deal.

Back at the reading tool from the opening, I am willing to keep the ordinary page for now. The next step is to see whether a real user can save an item and find it later. If they cannot, I need to find out exactly where the trail disappeared. Once that problem is clear, the decision about what to borrow and what to build myself will be clearer than it was when I stared at the blank page.

## References

- Judy Hanwen Shen and Alex Tamkin / Anthropic, 2026, [How AI assistance impacts the formation of coding skills](https://www.anthropic.com/research/AI-assistance-coding-skills): immediate learning assessment and its limits.
- LearnLM Team Google and Eedi, 2025, [AI tutoring can safely and effectively support students: An exploratory RCT in UK classrooms](https://arxiv.org/abs/2512.23633): AI tutoring with expert review of each message; only the authors' abstract was checked here.
- Paul Graham, 2013, [Do Things that Don't Scale](https://paulgraham.com/ds.html): founder advice and examples of discovering product gaps by serving early users directly.
- Bryan Clayton, 2023, [Bootstrapping a $30 Million Dollar Company: The Strategies Behind Our Decade of Growth](https://buffer.com/resources/bootstrapping-growth/): the GreenPal founder's account of customer conversations and a change in acquisition strategy.
- Gerdien G. van Eersel et al., 2016, [The Testing Effect and Far Transfer: The Role of Exposure to Key Information](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.01977/full): retrieval practice, focused feedback, and limits on applying the experiment to a new context.
