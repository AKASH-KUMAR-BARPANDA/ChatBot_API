
from groq import Groq
client = Groq(
        api_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    )

def GROQ_Server_INJECTION(message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="openai/gpt-oss-20b",
        stream=False,
    )

    return chat_completion.choices[0].message.content
