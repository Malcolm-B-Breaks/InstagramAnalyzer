from ai_analyzer import ai_analyzer
from categorizer import categorizer

lang = 'en'
# lang = 'jp'
model = "axios"
# model = "veritas"
# model = "chatGPT4"

def main():
    ai_analyzer(lang, model)

if __name__ == '__main__':
    main()