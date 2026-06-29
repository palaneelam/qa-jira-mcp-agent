import os
import json
import re
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def clean_json_response(text):
    text = text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()
    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    match = re.search(r"\{.*\}", text, re.DOTALL)

    if match:
        return match.group(0)

    return text


def get_openai_client():
    github_token = os.getenv("GITHUB_TOKEN")

    if not github_token:
        raise ValueError("GITHUB_TOKEN is missing in .env file")

    return OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=github_token
    )


def call_github_models_json(prompt):
    client = get_openai_client()

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        response_format={
            "type": "json_object"
        }
    )

    raw_text = response.choices[0].message.content
    cleaned_text = clean_json_response(raw_text)

    try:
        return json.loads(cleaned_text)
    except Exception as e:
        return {
            "error": str(e),
            "raw_response": raw_text
        }