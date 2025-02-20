import xml.etree.ElementTree as ET
import bs4 as soup
import requests
import yaml
import pandas as pd
import csv
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
from lxml import etree

# from categorizer import categorizer

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
        sysPrompt = prompts[lang]['system_prompts']['translator_prompt_1']
        userPrompt = prompts[lang]['user_prompts']['translator_prompt_1']
        # response_format = prompts[lang]['response_format']['format']['json']
        # response_format_prompt = prompts[lang]['response_format']['prompt']['json']

        # url = "https://v2.snsfeeder.app/ig/rss/7f074de9da34599777724d8d78550fe666977eecc4a92e02c897aa63ca840934"

        # url_link = requests.get(url)
        # file = soup.BeautifulSoup(url_link.text, features="xml")

        # content = file('title')[-1]
        # content = "./input_data/test.txt"
        with open("./input_data/cl_news.csv", 'r', encoding='utf-8') as csv_file:
            content = pd.read_csv(csv_file, usecols=['cl_id', 'cate_id', 'rss_id', 'title', 'body'])
            print(content)

            ai_message = {}

            if model == "chatGPT4":
                output = openAI.chat.completions.create(
                    model = chatGPT4,
                    # response_format = response_format,
                    messages = [
                        {
                            "role": "system",
                            "content": f'{sysPrompt}'
                        },
                        {
                            "role": "user",
                            "content": f'{userPrompt}{content}'
                        }
                    ],
                )
                ai_message = output.choices[0].message.content

            elif model == "axios" or model == "veritas":
                messages = [
                    SystemMessage(
                        content=f'{sysPrompt}'
                    ),
                    HumanMessage(
                        content=f'{userPrompt}{content}'
                    )
                ]

                ai_message = agent.invoke(messages)

            print(ai_message)

ai_analyzer('en', 'chatGPT4')
# # ai_analyzer('en', 'veritas')