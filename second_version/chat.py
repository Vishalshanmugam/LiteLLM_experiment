import openai
import requests

# Define public names mapped to model details
MODEL_CONFIGS = {
    "OpenRouter LLaMA3": {
        "model": "meta-llama/llama-3-8b-instruct",
        "base_url": "https://openrouter.ai/api/v1",
        "requires_api_key": True
    },
    "Local Ollama LLaMA3": {
        "model": "ollama/llama3",
        "base_url": "http://localhost:8000/v1",
        "requires_api_key": False
    },
    "OpenRouter Mistral": {
        "model": "mistral/mistral-7b-instruct",
        "base_url": "https://openrouter.ai/api/v1",
        "requires_api_key": True
    }
}

# Display model options
print("Available Models:")
for idx, name in enumerate(MODEL_CONFIGS.keys(), start=1):
    print(f"{idx}. {name}")

# Ask user to select one
selected = int(input("Choose a model by number: ").strip())
selected_model_name = list(MODEL_CONFIGS.keys())[selected - 1]
selected_config = MODEL_CONFIGS[selected_model_name]

# Ask for API key if required
api_key = None
if selected_config["requires_api_key"]:
    api_key = input("Enter API key for selected model: ").strip()

# Initialize OpenAI client
client = openai.OpenAI(
    api_key=api_key,
    base_url=selected_config["base_url"]
)

# Helper to capture multi-line input
def get_complete_input():
    print("\nYou: (End your input with ';;' on a new line)")
    lines = []
    while True:
        line = input()
        if line.strip() == ";;":
            break
        lines.append(line)
    return "\n".join(lines)

# Start chat session
print(f"\nChatting with: {selected_model_name}")
print("Type 'quit' to exit\n-------------------------------------")

while True:
    user_input = get_complete_input()

    if user_input.lower().strip() in ['quit', 'exit', 'q']:
        print("Goodbye!")
        break

    if not user_input.strip():
        continue

    try:
        response = client.chat.completions.create(
            model=selected_config["model"],
            messages=[{"role": "user", "content": user_input}],
            temperature=0.7
        )
        print(f"\n{selected_model_name}:\n{response.choices[0].message.content}")
    except Exception as e:
        print(f"\nError: {str(e)}")
