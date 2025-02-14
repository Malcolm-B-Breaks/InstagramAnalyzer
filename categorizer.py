import json
import yaml
import regex as re
from jsonschema import validate
from schemas.categorizer_schema import categorizer_schema

def categorizer(data, lang):
    # output_data = json.load(data)
    # re.sub(r'\"', '"', data)
    # re.match(r'^\s*"([^"]*)"\s*$', data)
    print(type(data))
    validate(instance=data, schema=categorizer_schema)
    # try:
    #     print(data)
    #     validate(instance=data, schema=categorizer_schema)
    #     print('Validation checks out!')
    # except:
    #     print("Validation failed.")