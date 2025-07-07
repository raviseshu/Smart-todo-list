import openai
import os

openai.api_key = os.getenv("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")

def get_ai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4o", etc.
        messages=[{"role": "user", "content": prompt}],
        max_tokens=256,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content']
