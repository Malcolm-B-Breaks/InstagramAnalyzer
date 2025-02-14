from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
import regex as re
import yaml
import json

from categorizer import categorizer

def ai_analyzer(language, model):
    if model == "axios":
        from ai_models.axios_init import axios as agent
    elif model == "veritas":
        from ai_models.veritas_init import veritas as agent
    elif model == "chatGPT4":
        from ai_models.chatgpt_init import openAI, chatGPT4

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
            ai_message = {}

            for post in data['data']:

                if model == "chatGPT4":
                    output = openAI.chat.completions.create(
                        model = chatGPT4,
                        response_format = response_format,
                        messages = [
                            {
                                "role": "system",
                                "content": sysPrompt
                            },
                            {
                                "role": "user",
                                "content": f'{userPrompt}{category_keywords}{post}{response_format_prompt}'
                            }
                        ],
                    )
                    # ai_message.append(output.choices[0].message.content)
                    ai_message = output.choices[0].message.content

                elif model == "axios" or model == "veritas":
                    messages = [
                        SystemMessage(
                            content=sysPrompt
                        ),
                        HumanMessage(
                            content=f'{userPrompt}{category_keywords}{post}{response_format_prompt}'
                        )
                    ]

                    ai_message = agent.invoke(messages)


                print(type(ai_message))
                print(ai_message)

                # re.match(r'^\s*"([^"]*)"\s*$', ai_message)
                # re.sub(r'\"', '"', ai_message)

                with open(f"./output_data/categorized_posts/data_{lang}.json", "a", encoding='utf-8') as file:
                    json.dump(ai_message, file, ensure_ascii=False)
                    # json.dump(ai_message, file)

                # categorizer(ai_message, lang)