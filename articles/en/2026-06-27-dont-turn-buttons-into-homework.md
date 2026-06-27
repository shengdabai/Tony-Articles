# Don't Turn Buttons Into Homework

> 发布日期:2026-06-27 · [中文](../zh/2026-06-27-别把按钮变成作业.md) | [English](../en/2026-06-27-dont-turn-buttons-into-homework.md)

---

The most suspicious phrase in AI product design right now may be "just say what you want."

It sounds generous. No menus. No settings. No digging through pages. No need to learn the interface. You speak, the machine understands, and the service happens.

Sometimes that is a real improvement.

But sometimes it is just a button wearing a costume.

The old product asked you to tap "book a ride." The new product asks you to type, "Please book me a ride that is fast and cheap." The old product asked you to choose a service from a list. The new product asks you to describe the same service in a blank box, then wait for the system to guess the route back to a familiar screen.

That is not always progress.

Sometimes AI does not remove work from the user. It moves product work onto the user and calls it natural language.

## The difference between desire and description

Didi's AI ride assistant is a useful public example because the idea itself is not silly. Ride-hailing does contain many fuzzy, personal needs. A passenger may want a smoother driver because they are carsick, a larger trunk because they have luggage, or a route that works better for an elderly family member. These are hard to compress into a few fixed buttons.

According to a March 2026 Xinhua report, Didi said its AI assistant "Xiao Di" supports more than 90 service labels, turning fuzzy needs such as air quality or driving smoothness into dispatch conditions.[^1] That is the kind of place where natural language can help: the user has a real situation, and the product has too many possible combinations to expose cleanly.

But the same report also said the top personalized demand was "fast and cheap," at 57%, followed by "fresh air" at 12.5% and "nearest car" at 9.9%.[^1]

That number is interesting because "fast and cheap" is not a niche preference. It is close to the default reason people open a ride-hailing app.

If saying "fast and cheap" changes the result dramatically, the old default was probably not aligned with the most common user goal.

If saying it does not change the result much, the user has simply been asked to recite the obvious.

This is the first test for AI interaction:

Is the user expressing a real preference the system could not reasonably infer, or are they doing homework the product should have done already?

## A blank box can become a new command line

People often describe chat interfaces as the opposite of command lines. I am not so sure.

A command line forces the user to know what the system can do, remember the right command, and express the request in a format the machine accepts. A blank AI box can quietly recreate the same burden in softer language.

Instead of:

```text
taxi --cheap --fast
```

the user writes:

```text
Help me get a fast and cheap ride.
```

The sentence is friendlier, but the mental work is similar. The user still has to know that the system supports this kind of request. They still have to imagine the right words. They still have to check whether the result matches what they meant.

This is why the old UX principle of "recognition rather than recall" still matters. Nielsen Norman Group explains that recognition is easier because the interface provides cues; open-ended recall asks people to retrieve the answer from memory.[^2] Menus, cards, filters, and buttons are not automatically primitive. Often they are cognitive scaffolding. They show what is possible.

The tragedy of some AI products is that they remove the scaffolding too early.

They think the future is an empty box.

But an empty box is not freedom when the user does not know what to ask.

## Money needs a surface

Alipay's AI version, "Abao," shows the other side of the problem.

In June 2026, Alipay opened invitation testing for an AI version that lets users swipe right into a conversational interface. Public reports described examples such as asking to check a housing provident fund account, with Abao matching the relevant mini program and service entry.[^3]

That can be useful. A large super-app is full of hidden doors. If AI helps users find the right door faster, it is not a gimmick.

But Alipay also drew a clear boundary: anything involving payment or money movement must still be confirmed by the user.[^3] That boundary is not a weakness. It is the product admitting reality.

Money is not a good place for magical ambiguity.

When the task is low risk, a conversational shortcut can be forgiving. If the assistant recommends the wrong coffee shop, the cost is small. If it misunderstands a transfer, repayment, or investment instruction, the cost is not small. At that point the interface has to become inspectable again. Amount, recipient, account, fee, risk, and authorization need a visible surface.

That is what many AI-native narratives miss.

The final confirmation screen is not a leftover from the old world.

It is where responsibility becomes visible.

A button can be a promise: this is the action, this is the consequence, and this is the moment you choose.

Replacing that with a smooth sentence may feel advanced, but the user still needs a place to verify reality.

## The product value test

Yu Jun's product value formula is still a useful knife here:

```text
User value = new experience - old experience - switching cost
```

Different versions of the formula translate the last term as migration cost, replacement cost, or switching cost.[^4] The wording is less important than the subtraction.

AI teams are very good at praising the new experience. They show the demo: the user says one sentence, the system responds, and the screen moves by itself. It looks alive.

But the old experience also matters. If the old path took one tap, the new path has to beat one tap. If the old path showed all options clearly, the new path has to beat clarity. If the old path made responsibility obvious, the new path has to beat obviousness.

Then comes switching cost.

Does the user need to learn what the assistant can do?

Do they need to phrase requests carefully?

Do they need to inspect every result because the model may be wrong?

Do they need to wait through a conversation that could have been a button?

Do they need to recover when the assistant chooses the wrong path?

These costs are easy to hide in a launch video and painful in daily use.

The question is not "Can AI do this?"

The question is: "After all checking, correcting, waiting, and learning costs are counted, is the user's life actually easier?"

## Good AI often has less AI flavor

I do not think this means conversational interfaces are bad. The opposite is true. Natural language is one of the most important interfaces we have ever had.

But its value is situational.

Natural language is powerful when the user's goal is fuzzy, the conditions are many, the path is hidden, and the cost of being slightly wrong is low.

It is weaker when the goal is already clear, the old path is mature, the task takes one or two steps, and the user mainly needs speed.

It must be constrained when the goal is clear but the risk is high, especially around money, health, legal commitments, identity, or irreversible actions.

In those cases, AI should not replace the interface. It should prepare the interface.

It can fill the form, but the user should see the form.

It can find the service, but the user should see the service.

It can summarize the options, but the user should see the tradeoffs.

It can detect the likely mistake, but the user should see the warning.

The best AI product may not look like a chatbot at all. It may look like a default that got smarter, a form that filled itself, a button that appeared at the right time, a warning that caught an error before it became expensive, or a workflow that quietly skipped five useless steps.

That kind of AI has less AI flavor, but more user value.

## The real work is behind the screen

There is an organizational reason chatboxes spread so fast: they are easy to show.

A chatbox is a visible symbol. It tells the boss, the press, investors, and users: look, we have AI now.

But the work that truly improves experience is often ugly and invisible: better defaults, cleaner data, stronger state checks, safer permissions, more reliable routing, better exception handling, sharper evaluation, clearer fallback paths.

That work does not make a dramatic screenshot.

It just makes the user suffer less.

This is why AI product design needs more humility than hype. The model may be new, but the user is still human. Humans still prefer cues to memory. Humans still dislike unnecessary effort. Humans still need responsibility to be visible. Humans still trust systems through repeated small successes, not through slogans.

The goal of AI is not to make every product talk.

The goal is to make the product understand enough that the user does not have to perform understanding for it.

## Do not make the user prove the AI exists

Here is the simplest rule I want to keep:

Do not make the user prove the AI exists.

If a product is intelligent, the user should feel less burden, not more ceremony.

They should not have to describe the obvious.

They should not have to guess the system's abilities.

They should not have to inspect a vague action that should have been concrete.

They should not have to turn a clear button into a paragraph of instruction.

Use conversation when conversation absorbs ambiguity.

Use buttons when buttons reduce memory.

Use forms when forms make responsibility visible.

Use automation when automation removes dead work.

Use confirmation when confirmation protects the user.

AI should not be a new layer of homework placed between people and things they already know how to do.

The real upgrade is quieter.

It is not "say one more sentence."

It is "think one less unnecessary thought."

Do not replace a good button with a bad conversation.

Do not confuse a demo with relief.

And please, do not turn buttons into homework.

## References

[^1]: Xinhua, "滴滴公布 AI 打车数据，网约车进入个性化需求新阶段," 2026-03-23. https://www.news.cn/tech/20260323/7b1970fbe2484359bd595254b110be9a/c.html
[^2]: Nielsen Norman Group, "Memory Recognition and Recall in User Interfaces." https://www.nngroup.com/articles/recognition-and-recall/
[^3]: IT之家, "AI 版支付宝官宣开启邀测：右滑打开'阿宝'，官方放出 100 个邀请码," 2026-06-16. https://www.ithome.com/0/964/691.htm
[^4]: 人人都是产品经理, "破除误解，重读俞军的产品价值公式," 2019-11-06. https://www.woshipm.com/pd/3055985.html
