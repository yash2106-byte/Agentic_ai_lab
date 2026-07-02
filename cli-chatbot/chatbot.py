from dotenv import load_dotenv
import os
from groq import Groq
import sys

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
ch = input("You want to chat?")
while ch != "no":
    system_prompt = input("Enter system prompt (leave blank for none): ")
    user_prompt = input("Enter your prompt: ")

    messages = []

    if system_prompt:
        messages.append({
            "role": "system",
            "content": system_prompt+"make sure to answer it in 5 lines"
        })

    messages.append({
        "role": "user",
        "content": user_prompt
    })
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile"
    )
    sys.stdout.reconfigure(encoding="utf-8")
    # Print the completion returned by the LLM.
    print(chat_completion.choices[0].message.content)
    ch = input("You want to chat?")
