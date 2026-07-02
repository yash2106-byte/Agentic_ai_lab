from dotenv import load_dotenv
import os
import sys # LLM models tend to return Unicode character which cannot be procesd hence we need to use utf-8
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
prompt = "tell me something about numbers"
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": prompt
        }
    ],

    model="llama-3.3-70b-versatile"
)
sys.stdout.reconfigure(encoding="utf-8")
# Print the completion returned by the LLM.
print(chat_completion.choices[0].message.content)