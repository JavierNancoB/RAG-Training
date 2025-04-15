'''
from openai import OpenAI

client = OpenAI(api_key="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",
base_url="https://openrouter.ai/api/v1")

chat = client.chat.completions.create(
    model="deepseek/deepseek-r1:free",
    messages=[
        {
        "role": "user",
        "content": "Hola, ¿cómo estás?"
        },
    ]
)

print(chat)
'''
from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

chat = client.chat.completions.create(
    model="deepseek/deepseek-r1:free",
    messages=[
        {
            "role": "user",
            "content": "Hola, ¿cómo estás?"
        },
    ]
)

# Mostrar solo la respuesta del modelo
print(chat.choices[0].message.content)
