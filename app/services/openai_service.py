import os

USE_MOCK = True #Troque para False, para ativar

def generate_response(message: str) -> str:
    if USE_MOCK:
        # simulação
        if "hello" in message.lower():
            return "Hello. How can I assist you today?"

        if "price" in message.lower():
            return "Pricing depends on your requirements. Can you give more details?"

        return f"I understand your message: '{message}'. Processing request..."

    # Caso o usuário possua crédito, rodar isso
    from openai import OpenAI
    from app.core.config import settings

    client = OpenAI(api_key=settings.OPENAI_API_KEY)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": message}
        ]
    )

    return response.choices[0].message.content
