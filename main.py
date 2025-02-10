from openai import OpenAI
from dotenv import load_dotenv
import yaml
import json
import os

from ai_analyzer import ai_analyzer

load_dotenv()

open_ai_api_key = os.getenv('OPENAI_API_KEY')
cl = OpenAI()
current_model = os.getenv('MODEL')

print(ai_analyzer())