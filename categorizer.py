from jsonschema import validate
from categorizer_schema import categorizer_schema


def categorizer():
    output = "Put AI Output here"
    validate(instance=output, schema=categorizer_schema)
    """
    First, use jsonschema to validate ChatGPT's output
    If it fails, then have the original ai_analyzer function rerun
    perhaps with an additional prompt letting it know that it failed
    to properly produce the desired schema, and to not be sorry,
    but be careful.
    """
    pass