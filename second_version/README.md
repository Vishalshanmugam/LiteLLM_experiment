# Multi-Model AI Chat Interface (Python CLI)

This project is a **command-line chat interface** that allows users to interact with different AI models (such as LLaMA3, Mistral) hosted either **locally (e.g., Ollama)** or via **API services (e.g., OpenRouter)**.

Users can:
- Choose from predefined models with friendly public names.
- Provide API keys only when required.
- Chat with any model through a unified terminal interface.

---

## 🧠 Supported Models

| Public Name           | Model ID                      | Hosted At                  | Requires API Key |
|-----------------------|-------------------------------|----------------------------|------------------|
| OpenRouter LLaMA3     | `meta-llama/llama-3-8b-instruct` | `https://openrouter.ai`     | ✅               |
| Local Ollama LLaMA3   | `ollama/llama3`                | `http://localhost:8000`    | ❌               |
| OpenRouter Mistral    | `mistral/mistral-7b-instruct`  | `https://openrouter.ai`     | ✅               |

---

## 📦 Requirements

Python 3.7+

Install dependencies:

```bash
pip install openai requests
```

### 1. Start Ollama
```bash
ollama serve
ollama run llama3
```
### 2. Run the script:
```bash
python3 chat.py
```
### 3. Choose a model when prompted:
```bash
Available Models:
1. OpenRouter LLaMA3
2. Local Ollama LLaMA3
3. OpenRouter Mistral
Choose a model by number:
```
### 4. Enter API key
### 5. Interaction with the AI

## API Keys
OpenRouter: Get a free key from https://openrouter.ai
For local models (like Ollama), no key is needed.

## Future Features
Model fallback if one fails.

Web interface using Flask or JavaScript frontend.

Save chat history locally.

## Troubleshooting
401 Unauthorized: Your API key is missing or invalid.

404 Not Found: Model not loaded or incorrect base URL.

Connection refused: Ensure Ollama or your server is running.

## License
This project is licensed under the MIT License.

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

## Attribution
LiteLLM is developed and maintained by BerriAI

Models served via OpenRouter
