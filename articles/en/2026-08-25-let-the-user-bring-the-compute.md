# Let the User Bring the Compute

> 发布日期:2026-08-25 · [中文](../zh/2026-08-25-让用户把算力带来.md) | [English](../en/2026-08-25-let-the-user-bring-the-compute.md)

---

There is a quiet kind of leverage that does not look like leverage at first.

It does not announce itself as a bigger model, a larger team, a new funding round, or a heroic founder story. It looks more boring than that: a product opens in the browser, the user's own computer does most of the work, files stay on the user's device, and the server mostly ships static code.

That architecture sounds like an implementation detail. It is not.

In many software businesses, architecture is the business model before pricing becomes the business model. The place where computation happens decides who pays, who waits, who trusts, who scales, and who captures the upside when usage grows. If the work happens on your server, every new user brings new cost. If the work happens on the user's machine, every new user brings not only demand but also a little piece of supply.

This is why Photopea is more interesting than the usual "one-person startup" headline. The shallow version says: one person built a browser-based image editor, kept going for years, and turned it into a multi-million-dollar business. That is true enough, but it is not the deepest lesson. The deeper lesson is that the product was shaped around a cost curve most people forget to look at.

Photopea did not begin as a grand attempt to rebuild Photoshop in the cloud. Its public build story says that by the end of 2017 it had grown for more than four years, had been visited by more than 2.5 million people, and had accumulated about 120,000 hours of use. A later interview reported that in 2021 the site was being opened about 10 million times a month, with users spending about 1.5 million hours a month inside it, while hosting cost was described as roughly $50 a year because there was no server-side code. Later revenue estimates vary because the company is private, but the reported pattern is stable: most income came from ads, while the infrastructure bill stayed almost absurdly low for a product with that much usage.

The word that matters here is not "ads." Ads are not a universal lesson. The word is "where."

Where does the work happen?

When a user opens a large image file, applies a filter, moves layers around, and exports the result, that work could have been designed as a cloud service. The file could have been uploaded, processed, stored, synchronized, and downloaded. That would create a very familiar business: user growth would be tied to compute bills, storage bills, bandwidth bills, privacy risk, compliance complexity, and operational load.

Instead, Photopea's privacy policy states that opened files are processed on the user's device and do not leave it for editing. That one architectural choice changes the whole equation. The user's machine is not merely a client terminal. It is part of the production system.

Once you see this, the product stops looking like "free Photoshop in a browser." It starts looking like a small factory distributed across millions of already-owned machines.

This matters for anyone thinking about AI, learning, and personal leverage, because the AI era is tempting us toward the opposite instinct. We keep imagining intelligence as something centralized: a giant model in a giant data center, wrapped in a subscription, reached through a chat box. That picture is partly true. Frontier training and high-end inference do require massive capital, hardware, energy, and engineering discipline.

But if we stop there, we miss the part ordinary people can actually use.

The question for a creator, independent developer, teacher, consultant, or small team is not "How do I own the biggest model?" That is the wrong contest. The useful question is: "What can I move to the place where the cost is already paid?"

The user's device is already paid for. The user's context already exists. The user's files, notes, habits, preferences, and repeated work are already there. The user's judgment is already present, even if it is often underused. A strong AI workbench should not try to replace all of that with a remote oracle. It should connect to it, structure it, and let it compound.

This is a very different design philosophy from "AI does everything for you."

"AI does everything for you" sounds convenient, but it often makes the human weaker. The person stops forming predictions, stops making intermediate judgments, stops owning the process, and eventually cannot tell whether the output is good. The machine becomes faster, while the person becomes more dependent.

"AI helps you bring your own compute" is different. Here, compute is not only CPU and GPU. It is also accumulated context, taste, memory, examples, constraints, and standards. The machine can accelerate steps, but the user's own environment remains the workbench. The user does not vanish from the loop. The user becomes better equipped inside the loop.

That is the real bridge between products like Photopea and personal AI systems.

Photopea shows one version of the principle: put heavy interactive work in the browser, keep user files local, and make the web page both product and distribution surface. An AI workbench can apply a similar principle at the level of knowledge work: let notes stay portable, let instructions be files instead of trapped chat memories, let workflows be inspectable, let verification happen close to the work, and let the user's own context flow into the tools they choose.

This is not nostalgia for local software. It is a way of protecting agency.

The old desktop era gave users ownership but often lacked reach. The cloud era gave reach but often took ownership away. The interesting future is not a simple return to the desktop. It is a hybrid: cloud intelligence when needed, local and portable context by default, and architecture that treats the user as a participant rather than a source of raw material.

That shift has strategic consequences.

First, it changes cost. If every meaningful action requires your server to think, store, and transform, then scale punishes you. You need pricing, quotas, funding, and operational controls before usage can grow too far. If meaningful parts of the work happen on the user's side, scale can become less fragile. Not free, not magical, but less directly punished by success.

Second, it changes trust. People trust tools differently when their work does not have to leave their hands. This is especially important for creative files, private notes, business records, and learning traces. A product does not become trustworthy by declaring itself safe. It becomes more trustworthy when its architecture reduces the amount of trust required.

Third, it changes learning. A tool that keeps the user's working material close can become a practice environment. You do not learn only by receiving polished answers. You learn by manipulating the thing itself, seeing consequences, correcting mistakes, saving versions, and returning tomorrow with a little more context than yesterday. That is how skill compounds.

This is where many AI products still feel strangely backward. They can generate impressive artifacts, but they often do not help the user's system improve. The output appears, the conversation scrolls away, and tomorrow the person starts again from a vague memory. The visible speed is high; the accumulated ability is low.

If AI is going to make people stronger rather than lazier, the unit of progress cannot be one answer. It has to be the workbench.

A good workbench remembers without imprisoning. It makes the next attempt easier without hiding the standards. It lets the user take materials away. It exposes enough structure for inspection. It separates the model's suggestion from the user's decision. It makes verification cheaper. It turns one successful process into a reusable path.

This is why "bring your own compute" is bigger than a technical slogan. It is a way to ask whether a system gives power back to the user or quietly absorbs it.

Of course, the principle has limits.

Not every task belongs on the user's machine. Some workloads require shared databases, global coordination, specialized hardware, strict audit trails, or proprietary models that cannot run locally. Moving work to the client can create performance problems, battery costs, accessibility issues, browser compatibility bugs, and new security boundaries. A clumsy local-first design can simply move the burden from the company to the user and call it empowerment.

So the serious version of this idea is not "local good, cloud bad." The serious version is: put each part of the system where it creates the most total freedom after cost, trust, capability, and learning are all counted.

Sometimes that place is a data center. Sometimes it is a browser. Sometimes it is a plain text file. Sometimes it is a checklist. Sometimes it is the user's own repeated judgment, made visible enough for AI to help with but not replace.

The deeper question is not technical. It is moral in a practical sense: after the system becomes more capable, who becomes more capable with it?

If the answer is only "the platform," the user is being mined. If the answer is only "the model," the human is being trained into passivity. If the answer includes the user's files, habits, standards, context, and decision-making ability, then the system is doing something rarer. It is turning capability into strength.

That is the lesson I want to keep from Photopea.

Not that everyone should build a browser app. Not that ads are noble. Not that one person should spend fourteen years fighting alone. Those are surface details, and surface details are dangerous when copied blindly.

The lesson is simpler and harder: look for the hidden cost curve. Ask where the work actually happens. Ask whether growth adds weight or distributes it. Ask whether the user leaves stronger, with more of their own context and more of their own ability intact.

In the next decade, many people will compete to sell us intelligence. Some will sell speed. Some will sell convenience. Some will sell the fantasy that we no longer have to think.

I am more interested in tools that make thinking more productive.

The best tools do not merely perform for us. They let our own machines, our own context, and our own judgment enter the production line. They do not ask us to become idle spectators of artificial intelligence. They help us become better operators of our own lives.

That may be the most important kind of leverage now: not owning all the compute, but designing the loop so every user brings some of it, keeps some of it, and becomes stronger because of it.

Sources: [Photopea's 2017 build story](https://blog.photopea.com/creating-photopea.html), [Photopea privacy policy](https://cdn.photopea.com/privacy.html), [2021 founder interview on Failory](https://www.failory.com/interview/photopea), and [OperatorBook's revenue-source ledger](https://www.operatorbook.dev/stories/photopea-revenue).
