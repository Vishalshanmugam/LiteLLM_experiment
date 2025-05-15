import openai
import os

# Explicit client instantiation
client = openai.OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def get_complete_input():
    print("\nYou: (End your input with ';;' on a new line)")
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == ";;":
                break
            lines.append(line)
        except EOFError:
            break
    return "\n".join(lines)

print("Chat with OpenRouter Model - Type 'quit' to exit")
print("-------------------------------------")

while True:
    user_input = get_complete_input()

    if user_input.lower().strip() in ['quit', 'exit', 'q']:
        print("Goodbye!")
        break

    if not user_input.strip():
        continue

    # Use the instantiated client
    response = client.chat.completions.create(
        model="meta-llama/llama-3-8b-instruct",
        messages=[{"role": "user", "content": user_input}],
        temperature=0.7
    )

    print("\nAI:", response.choices[0].message.content)
