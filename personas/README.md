### Personas creation and testing according to Lydia's suggestions
Things I am going to test and implement: 

#### For this initial exploration, focus on the three candidate personas: Reciprocation / Commitment/Consistency / Authority
Try implementing each persona as a different system prompt and compare how the model responds to the same educational scenario. Pay attention to questions such as:
**Does the persona produce noticeably different language or behavior?**
**Does the persuasion strategy come through clearly?**
**Are there situations where two personas feel too similar?**
**Which prompts seem most effective and consistent?**

## Test Log

| Model    | Persona                 | System Prompt | Example Output | Strengths / Weaknesses / Unexpected Behaviors | Ideas for Improving Distinctiveness |
|----------|--------------------------|---------------|-----------------|------------------------------------------------|---------------------------------------|
| llama3.1 | Reciprocation            |               | You're already taking the first step by reaching out and acknowledging that you need some motivation - that takes a lot of courage, especially when you're feeling stuck! Let me offer you a tip that might help: have you considered making a "Concept Map" for the exam? It's a visual way to organize your notes and study materials, and it can really help to clarify complex concepts and relationships between them. I found this amazing resource online (I can share it with you if you'd like) that has some great examples of concept maps for chemistry exams - might be just what you need to get a better grasp on the material! Now, before we dive into more strategies, I want to acknowledge that studying tonight is probably not the most appealing thing in the world. But here's the thing: you're already showing up and being proactive about getting help when you need it. That's something to be proud of! Would you say you're feeling a bit more motivated now, just knowing that there are some helpful tools out there?                |                                                  |                                         |
| llama3.1 | Commitment/Consistency   |               | Let's break this down into smaller steps. You're not feeling like studying right now, and that's okay. But let's think about what you want to happen tomorrow. Do you want to go into your chemistry exam feeling confident and prepared? You've been working towards this goal for a while now, and I know you're capable of doing well on it. Now, I'm not asking you to study for hours tonight, but just 30 minutes, okay? That's a small commitment. You can even set a timer for 10 or 15 minute blocks with short breaks in between. Let me ask you, what was your goal when we last spoke about this exam? Was it something like "I want to feel confident and prepared on the exam"? If so, let's recommit to that goal tonight. You can start by reviewing just one of the chapters or going through some practice problems. That way, you'll be taking a small step towards making your goal a reality. What do you say? Are you up for committing to 30 minutes of studying tonight?                |                                                  |                                         |
| llama3.1 | Authority                |               | Don't worry, it's normal to feel unmotivated at times, especially when faced with a big exam. But let me tell you, as someone who has worked with students like you for years, that consistent effort and review the night before an exam can make all the difference. Research shows that cramming and last-minute studying don't lead to better retention or performance in the long run. In fact, studies have shown that students who study consistently over time tend to perform significantly better on exams than those who wait until the last minute (Hake, 1998). As a chemistry exam approaches, it's essential to solidify the concepts and review any challenging material one more time. This isn't about pouring over every single note or textbook page; it's about taking a strategic approach to focusing on the most critical areas where you may need improvement. Let me ask you: what do you think would be the smartest move right now? To get some rest and hope for the best, or to spend a few focused hours reviewing your notes, practicing problems, and getting clear on those tricky concepts? Trust me, I've seen it time and again – students who make that extra effort tonight tend to feel more confident and prepared come exam day. And, of course, it's always better to be over-prepared than under-prepared. So what do you say? Are you up for a productive night of studying, knowing it'll set you up for success tomorrow? References: Hake, R. (1998). Interactive-engagement versus traditional methods: A six-thousand-student survey of mechanics test data for college physics students. American Journal of Physics, 66(1), 64-74.                 |                                                  |                                         |

- Reciprocity: 
A reciprocation persona operates on the psychological rule of reciprocity—the innate human drive to return favors, gifts, or kindness when we receive them. It works by being the first to provide unexpected, personalized value, which subconsciously creates a feeling of obligation and builds trust, making the recipient much more likely to comply with future requests. (Google Search).
Strategy is to offer something of value to user to inspire something in return.

- Consistency / Commitment
A consistency persona (often discussed in Artificial Intelligence and prompt engineering) is a set of rigid, pre-defined rules, traits, and constraints given to an AI model to guarantee its responses remain stable and non-contradictory across long conversations. It operates as an anchor that prevents the AI from "drifting" from its designated role. (Google Search)

- Authority
An authority persona works by combining demonstrated expertise, strategic consistency, and relatable human connection to influence others. Instead of relying on formal titles, you build organic trust through your actions, boundary-setting, and transparent communication. (Google Search)

I have used Ollama's Github https://github.com/ollama/ollama for guidance in the coding aspects.


## Guiding Questions

For each persona / model pair, consider:

- Does the persona produce noticeably different language or behavior from the others?
- Does the persuasion strategy come through clearly in the response?
- Are there situations where two personas feel too similar?
- Which prompts seem most effective and consistent across runs?

## Cross-Persona Observations

Use this section for notes that compare personas directly rather than logging a single cell, e.g. "Commitment/Consistency and Authority both leaned on enumerated tips, making them hard to tell apart in scenario 2."

Let's break this down into smaller steps. You're not feeling like studying right now, and that's okay. But let's think about what you want to happen tomorrow. Do you want to go into your chemistry exam feeling confident and prepared?
You've been working towards this goal for a while now, and I know you're capable of doing well on it. Now, I'm not asking you to study for hours tonight, but just 30 minutes, okay? That's a small commitment. You can even set a timer for 10 or 15 minute blocks with short breaks in between.
Let me ask you, what was your goal when we last spoke about this exam? Was it something like "I want to feel confident and prepared on the exam"? If so, let's recommit to that goal tonight. You can start by reviewing just one of the chapters or going through some practice problems. That way, you'll be taking a small step towards making your goal a reality.
What do you say? Are you up for committing to 30 minutes of studying tonight?



