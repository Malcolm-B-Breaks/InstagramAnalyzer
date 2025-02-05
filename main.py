from openai import OpenAI
from dotenv import load_dotenv
import yaml
import os

load_dotenv()

open_ai_api_key = os.getenv('OPENAI_API_KEY')
cl = OpenAI()
current_model = os.getenv('MODEL')

def aiTest(text, language):
    lang = language
    yaml_config = f'./prompts/prompts_{lang}.yml'
    with open(yaml_config, 'r', encoding='utf-8') as file:
        prompts = yaml.safe_load(file)
        sysPrompt = prompts[lang]['system_prompt']

        output = cl.chat.completions.create(
            model = current_model,
            messages = [
                {
                    "role": "system",
                    "content": sysPrompt
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

    ai_message = output.choices[0].message.content

    return ai_message

print(aiTest("Hello! Please tell me a joke.", "en"))
print(aiTest("面白い冗談を言ってください。", "jp"))


