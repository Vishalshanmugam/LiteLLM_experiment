# 🧠 Chatting using LiteLLM 

A lightweight command-line chatbot that uses only AI models via [OpenRouter](https://openrouter.ai), optionally through a local proxy using [LiteLLM](https://github.com/BerriAI/litellm).

---

## ✨ Features

- Chat with OpenRouter-hosted models like - free usage of API key:
  - `meta-llama/llama-3-8b-instruct` ✅
  - `mistralai/mistral-7b-instruct` ✅
  - `deepseek-ai/deepseek-llm` ✅
- Multi-line chat input (`;;` to submit)
- Uses official `openai` Python SDK
- Optional local inference using LiteLLM

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/llama3-openrouter-chat.git
cd llama3-openrouter-chat
```
### 2. Create the virtual environment

```bash
python -m venv <any name>  # Create the venv first if needed copied in a file of different name
python -m pip install --upgrade pip  # Optional: upgrade pip
```
```bash
source venv/bin/activate # in case of linux/mac os
.\venv\Scripts\Activate.ps1 # in case of Powershell
venv\Scripts\activate # in case of CMD
```

### 3. Install Python Dependencies

``` bash

pip install openai

```

### 4. Set Your OpenRouter API Key

Get a free API key at https://openrouter.ai.

Set the API key as an environment variable in your terminal:

``` bash
export OPENROUTER_API_KEY=your_openrouter_api_key_here        # macOS/Linux
set OPENROUTER_API_KEY=your_openrouter_api_key_here           # Windows CMD
$env:OPENROUTER_API_KEY="your_openrouter_api_key_here"        # PowerShell
```

### Optional

Run LiteLLM Locally

Install LiteLLM:
```bash
pip install litellm
```
### 5. Run the server
Run with a local model (e.g., via Ollama + LLaMA 3):
```bash
litellm --model ollama/llama3 --host localhost --port 8000
```

### 6. Running the Chat Interface

Run the Python script:
```bash
python chat_with_llama3.py
```
Sample interaction:
```bash
Chat with OpenRouter Model - Type 'quit' to exit
-------------------------------------
You: (End your input with ';;' on a new line)
Type your message, then enter ;; on a new line to send.
```

### License

MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights 
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
copies of the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in 
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE.

### Attribution

LiteLLM is developed and maintained by BerriAI

