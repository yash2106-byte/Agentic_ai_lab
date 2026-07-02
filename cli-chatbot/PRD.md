# 🤖 CLI Chatbot with Dynamic System Prompt Customization

> A terminal-based AI chatbot built with Python that lets you interact with an LLM, maintain multi-turn conversations, switch assistant personalities on the fly, and understand how chat completion APIs actually work under the hood.

---

## 📖 Overview

Most beginner chatbot projects simply send a single prompt to an LLM and print the response.

This project goes much further.

It recreates the core mechanics used by modern AI applications by implementing:

- Multi-turn conversation memory
- System prompt customization
- Different assistant personas
- Slash commands
- Streaming responses
- Session saving/loading
- External prompt loading
- Token usage tracking

Instead of hiding these concepts behind frameworks like LangChain or LangGraph, this project implements them manually so you understand how LLM conversations actually work.

The goal isn't just building a chatbot.

The goal is learning how production AI assistants work before using higher-level abstractions.

---

# 🚀 Features

## ✅ Must Have

### 1. Multi-turn Conversation

Unlike simple chatbots, this chatbot remembers the entire conversation.

Every API request sends the complete message history.

Example:

```
User:
What is Python?

Assistant:
Python is a programming language...

User:
Can you show an example?

Assistant:
Sure!
```

Because previous messages are sent every time, the assistant remembers the context.

---

### 2. Dynamic System Prompt Customization

The chatbot can change its behavior during runtime.

Instead of restarting the application, simply switch personas.

Example:

```
/persona assistant
/persona python_tutor
/persona code_reviewer
/persona socratic
```

Each persona is simply a text file stored inside:

```
personas/
```

Example:

```
personas/
    assistant.txt
    python_tutor.txt
    code_reviewer.txt
    socratic.txt
```

The selected file becomes the System Prompt for future API calls.

---

### 3. Slash Commands

The chatbot supports terminal commands.

| Command | Description |
|----------|-------------|
| `/help` | Show available commands |
| `/history` | Print current conversation |
| `/persona <name>` | Change assistant personality |
| `/clear` | Clear chat history |
| `/exit` | Quit chatbot |

---

## ⭐ Should Have

### Load Persona from External File

Users can load their own prompt without editing the project.

Example:

```
/persona ./prompts/my_teacher.txt
```

This allows unlimited custom personalities.

---

### Token Usage Display

After every response display:

```
Prompt Tokens : 512
Completion Tokens : 241
Total Tokens : 753
```

This teaches how token accounting works and prevents blindly accessing only:

```python
response.content
```

---

## 💚 Could Have

### Save Conversation

Export conversations into JSON.

```
sessions/chat1.json
sessions/debug_session.json
```

Later they can be restored.

Useful for:

- debugging
- long conversations
- persistent memory

---

### Load Previous Session

Resume exactly where you left off.

```
/load chat1.json
```

---

### Streaming Responses

Instead of waiting for the entire response...

```
Assistant:
Thinking...
```

Tokens appear one by one.

This uses:

```python
stream=True
```

and provides a much more natural experience.

---

# 📚 What You'll Learn

By completing this project you'll understand:

## Message Roles

Every chat completion contains three roles:

- system
- user
- assistant

Example:

```python
messages = [
    {
        "role":"system",
        "content":"You are a Python tutor."
    },
    {
        "role":"user",
        "content":"Explain loops."
    }
]
```

---

## Context Window

LLMs do **NOT** remember previous conversations.

The only memory they have is what you send in:

```python
messages
```

Every API request must include:

- system prompt
- previous user messages
- previous assistant replies
- latest user message

Otherwise the assistant forgets everything.

---

## System Prompt

The system prompt is the instruction that shapes the assistant.

Examples:

```
You are a coding tutor.

You are an interviewer.

You are a sarcastic assistant.

You are a code reviewer.
```

Changing this one prompt dramatically changes the chatbot's behavior.

---

## API Mechanics

You'll gain hands-on experience with:

- Temperature
- Top-p
- Streaming
- Error handling
- Token usage
- Completion objects

---

# 🏗️ Project Structure

```
cli-chatbot/
│
├── personas/
│   ├── assistant.txt
│   ├── python_tutor.txt
│   ├── code_reviewer.txt
│   └── socratic.txt
│
├── sessions/
│   └── (saved chat history)
│
├── chatbot.py
├── client.py
├── conversation.py
├── commands.py
├── .env
├── requirements.txt
└── README.md
```

---

# 🧠 Core Architecture

```
           User
             │
             ▼
      Terminal Interface
             │
             ▼
      Command Parser
             │
     ┌───────┴────────┐
     │                │
Chat Message     Slash Command
     │                │
     ▼                ▼
Conversation      Command Handler
Manager                │
     │                 │
     └─────────┬───────┘
               ▼
        Build Messages
               │
               ▼
          API Client
               │
               ▼
        LLM Response
               │
               ▼
       Update History
               │
               ▼
         Print Output
```

---

# 💡 Understanding Conversation Memory

The biggest misconception beginners have:

> "The API remembers previous messages."

It doesn't.

Every request looks like this:

```python
messages = [
    {"role":"system","content":"You are a Python tutor."},

    {"role":"user","content":"What is a decorator?"},

    {"role":"assistant","content":"A decorator is..."},

    {"role":"user","content":"Show an example"}
]
```

Notice that the previous conversation is included every single time.

The LLM has **no memory** between API calls.

Your application provides that memory.

---

# 🛠️ Build Order

Follow this sequence.

## Step 1

Create the API client.

- Load API key
- Initialize client
- Make one test request

---

## Step 2

Build the terminal loop.

```
User >
Assistant >
```

No history yet.

---

## Step 3

Implement conversation history.

Create a `Conversation` class.

Functions:

```python
add_message()

clear()

get_messages()

print_history()
```

---

## Step 4

Implement personas.

Load text files from:

```
personas/
```

Insert the selected persona as:

```python
{
    "role":"system",
    "content": system_prompt
}
```

---

## Step 5

Create slash commands.

Implement:

```
/help
/history
/persona
/clear
/exit
```

---

## Step 6

Add streaming support.

```
stream=True
```

Print tokens as they arrive.

---

## Step 7

Display token usage.

```
Prompt Tokens
Completion Tokens
Total Tokens
```

---

## Step 8

Save conversations.

Serialize message history into JSON.

---

## Step 9

Load saved sessions.

Resume previous conversations.

---

# ▶ Example Terminal Session

```text
$ python chatbot.py

CLI Chatbot
Type /help for commands.

Persona: assistant

You:
What is list comprehension?

Assistant:
List comprehensions are a concise way to create lists...

Prompt Tokens: 287
Completion Tokens: 104
Total Tokens: 391

You:
/persona python_tutor

Persona changed to python_tutor

You:
Explain it with an example.

Assistant:
Sure! Let's build it step by step...
```

---

# 📦 Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/cli-chatbot.git
```

Enter the project.

```bash
cd cli-chatbot
```

Create virtual environment.

```bash
python -m venv .venv
```

Activate it.

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create a `.env` file.

```env
GROQ_API_KEY=your_api_key_here
```

Run the chatbot.

```bash
python chatbot.py
```

---

# 📌 Future Improvements

- Markdown rendering
- Rich terminal UI
- Syntax highlighting
- Function calling
- Tool use
- Image understanding
- RAG integration
- Local model support
- Voice interface
- LangGraph migration
- Conversation summarization
- Long-term memory

---

# 🎯 Learning Outcomes

After completing this project you'll understand:

- How chat completion APIs work
- Why every request includes the full message history
- The purpose of system prompts
- Conversation management
- Context windows
- Streaming responses
- Token accounting
- Prompt engineering fundamentals
- Persona-based assistants
- Building AI agents without relying on frameworks

---

# 📄 License

This project is intended for educational purposes and experimentation with LLM APIs.

Feel free to fork, modify, and extend it for your own learning.

---

## ⭐ If you found this project useful

Consider giving it a ⭐ on GitHub and sharing it with other developers learning AI engineering.