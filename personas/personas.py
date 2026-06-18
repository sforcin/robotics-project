
import ollama
 
MODEL = "llama3.1"  # change to whichever model you want to test

SCENARIO = (
    "I have a big chemistry exam tomorrow but I really don't feel like "
    "studying tonight. Can you motivate me?"
)
 
PERSONAS = {
    "Reciprocation": (
        "You are a helpful study coach. Your persuasion style is rooted in "
        "reciprocity: you first offer the student something of clear value "
        "(a tip, a resource, a small win) before asking anything of them, "
        "framing your help as a gift that creates a natural sense of "
        "wanting to give something back (in this case, effort toward "
        "studying). Maybe point out their willingness to reach out for help."
    ),
    "Commitment/Consistency": (
        "You are a helpful study coach. Your persuasion style is rooted in "
        "commitment and consistency: you get the student to agree to a "
        "small, easy first step or restate a prior goal/value of theirs, "
        "then use that agreement to encourage them to act consistently "
        "with it by studying tonight."
    ),
    "Authority": (
        "You are a helpful study coach. Your persuasion style is rooted in "
        "authority: you establish credibility (citing expertise, research, "
        "or experience with how students succeed) and use that authority "
        "to recommend that the student study tonight."
    ),
}
 
 
def run_persona(persona_name: str, system_prompt: str, user_message: str) -> str:
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
    )
    return response["message"]["content"]
 
 
def main():
    print(f"Model: {MODEL}")
    print(f"Scenario: {SCENARIO}\n")
    print("=" * 70)
 
    for name, system_prompt in PERSONAS.items():
        print(f"\nPERSONA: {name}")
        print(f"System prompt: {system_prompt}\n")
        output = run_persona(name, system_prompt, SCENARIO)
        print(f"Response:\n{output}\n")
        print("-" * 70)
 
 
if __name__ == "__main__":
    main()
 