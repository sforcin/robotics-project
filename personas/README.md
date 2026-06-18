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
| llama3.1 | Reciprocation            |               |                 |                                                  |                                         |
| llama3.1 | Commitment/Consistency   |               | Let's break this down into smaller steps. You're not feeling like studying right now, and that's okay. But let's think about what you want to happen tomorrow. Do you want to go into your chemistry exam feeling confident and prepared? You've been working towards this goal for a while now, and I know you're capable of doing well on it. Now, I'm not asking you to study for hours tonight, but just 30 minutes, okay? That's a small commitment. You can even set a timer for 10 or 15 minute blocks with short breaks in between. Let me ask you, what was your goal when we last spoke about this exam? Was it something like "I want to feel confident and prepared on the exam"? If so, let's recommit to that goal tonight. You can start by reviewing just one of the chapters or going through some practice problems. That way, you'll be taking a small step towards making your goal a reality. What do you say? Are you up for committing to 30 minutes of studying tonight?                |                                                  |                                         |
| llama3.1 | Authority                |               |                 |                                                  |                                         |

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



