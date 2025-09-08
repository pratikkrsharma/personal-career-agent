# 🧑‍💼 Personal Career Agent

A **personal AI career chatbot** built with **Gradio**, **OpenAI API (via OpenRouter)**, and **Vector Search (RAG)**.
This assistant represents **Pratik Sharma** and answers career-related questions about his **background, skills, projects, and experience**.
It can also capture leads by detecting when a user wants to get in touch and sending an **email notification** automatically.

---

## 🚩 Key Features

✅ Answers questions about **Pratik Sharma** career, experience, and expertise
✅ Uses **Vector Database (RAG)** to enrich context with past data
✅ Powered by **LLMs via OpenRouter API**
✅ Detects potential clients' interest and sends **email notifications automatically**
✅ Easy-to-use **Gradio Chat Interface**

---

## 🛠 Tech Stack

* **Python**
* **Gradio** (Chat Interface)
* **OpenRouter / OpenAI API** (LLMs)
* **Vector Database** (Similarity Search)
* **SMTP / Gmail** (Automated Email Notifications)
* **dotenv** (Environment Variables)

---

## 🔧 Setup & Run

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/pratikkrsharma/personal-career-agent
cd persona-career-agent
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Environment Variables

Create a `.env` file with the following:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
RECEIVER_MAIL_ADDRESS=any mail address which will receive mail with user's message
SENDER_MAIL_ADDRESS=gmail address to send user's message
MAIL_PASSWORD=your_gmail_app_password_here
```

⚠️ **Note:** For Gmail, you need to use an **App Password**, not your main account password.

---

### 4️⃣ Launch the App

```bash
python app.py
```

With UV:
```bash
uv sync
```
```bash
uv run python app.py
```

It will open a **Gradio web UI** locally.

---

## 📤 How Notifications Work

If the LLM detects a user expressing interest to connect, it sends an email to your configured Gmail with the message details.

**Trigger Example:**

```
send notification to pratik that this person with <user email> wants to get in touch with you
```

The user will then be shown your email and phone number automatically.

---

## 📂 Project Structure

```
├── app.py               # Main app with Gradio UI
├── vectordb.py          # Vector DB setup for context retrieval (RAG)
├── .env                 # API keys & email credentials
├── requirements.txt     # Dependencies
└── README.md            # Project documentation (this file)
```

---

## 🚀 Example Interaction

**User:**
Tell me more about Pratik's background in AI.

**Agent:**
Pratik Sharma has worked as a software engineer, building projects in data pipelines, AI agents, LangGraph, and OpenAI integrations...

---

## ✨ Future Enhancements

* Analytics dashboard for tracking user questions
* Deployment as a self hosted website

---

## 📧 Contact

If you'd like to collaborate or learn more, feel free to contact:
📧 **[mail](mailto:pratikkrsharma@gmail.com)**
