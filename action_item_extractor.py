import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

def extract_action_items(text):
    client = OpenAI(api_key=openai_api_key)

    prompt = (
        "Extract clear and actionable task items from the following meeting transcript.\n\n"
        "Return the list in bullet points format."
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()
