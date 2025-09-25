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

```bash
PUSHOVER_USER=<your user key>
PUSHOVER_TOKEN=<your app token>
