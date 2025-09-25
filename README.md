# Career Conversation Agent


**Career Conversation Agent** is an AI-powered assistant that helps you explore career paths, engage in meaningful conversations, and provides real-time notifications via Pushover. It’s designed to demonstrate **agentic AI workflows**, integrating domain expertise with real-world interactions.

---

## 🚀 Features

- **AI-Powered Career Conversations**: Ask questions and receive insightful, context-aware answers.  
- **Push Notifications**: Get notifications directly to your phone via [Pushover](https://pushover.net).  
- **Agentic Workflows**: Demonstrates how AI can interact with real-world services and orchestrate tasks.  
- **Deployment Ready**: Easily deployable on Hugging Face Spaces using Gradio.

---

## 📲 Pushover Setup

1. Sign up at [pushover.net](https://pushover.net).  
2. Create an **Application/API Token** (name it e.g., *Agents*).  
3. Add the following to your `.env` file:


## 🚀 Deployment on Hugging Face Spaces

1. **Create a Hugging Face account**  
   Visit [huggingface.co](https://huggingface.co) and sign up.

2. **Generate an Access Token**  
   Make sure it has **WRITE permissions**.

3. **Install the Hugging Face CLI tool**  
   In your terminal, run:

   ```bash
   uv tool install "huggingface_hub[cli]"
   hf auth login
   hf auth whoami
### Add your token to `.env`

Deploy your app
From the 1_foundations folder, run:

bash
Copy code
uv run gradio deploy
Follow the prompts:

Space name: career_conversation

Entry point: app.py

Hardware: cpu-basic

Secrets: Yes → add OPENAI_API_KEY, PUSHOVER_USER, PUSHOVER_TOKEN

GitHub Actions: No

🔑 Secrets Management
Enter secrets as key-value pairs during deployment:

makefile
Copy code
OPENAI_API_KEY: sk-...
PUSHOVER_USER: u-...
PUSHOVER_TOKEN: a-...
Or manage them later on Hugging Face:

Avatar → Profile → Select Space → ⚙ Settings → Variables & Secrets

✅ Example Space
See a deployed example: Career Conversation Space

🔄 Redeploy / Reset
Delete the auto-generated README.md in the career_conversation folder before redeploying.

To delete the Space:

Hugging Face → Profile → Space → ⚙ Settings → Delete
