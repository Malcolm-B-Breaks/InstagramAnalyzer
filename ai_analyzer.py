from openai import OpenAI
from dotenv import load_dotenv
import yaml
import json
import os

load_dotenv()

open_ai_api_key = os.getenv('OPENAI_API_KEY')
cl = OpenAI()
current_model = os.getenv('MODEL')

def ai_analyzer(language):
    lang = language
    yaml_config = f'./resources/prompts/prompts_{lang}.yml'
    with open(yaml_config, 'r', encoding='utf-8') as file:
        prompts = yaml.safe_load(file)
        sysPrompt = prompts[lang]['system_prompt']
        userPrompt = prompts[lang]['user_prompt']
        category_keywords = prompts[lang]['keywords']['category_keywords']
        response_format = prompts[lang]['response_format']['format']['json']
        response_format_prompt = prompts[lang]['response_format']['prompt']['json']

        with open('./input_data/IGposts.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

            output = cl.chat.completions.create(
                model = current_model,
                response_format = response_format,
                messages = [
                    {
                        "role": "system",
                        "content": sysPrompt
                    },
                    {
                        "role": "user",
                        "content": f'{userPrompt}{category_keywords}{data}{response_format_prompt}'
                    }
                ],
            )

    ai_message = output.choices[0].message.content

    with open(f"./output_data/categorized_posts/data_{lang}.json", "w", encoding='utf-8') as file:
        json.dump(ai_message, file, ensure_ascii=False)

    return ai_message

print(ai_analyzer("en"))
# print(ai_analyzer("jp"))