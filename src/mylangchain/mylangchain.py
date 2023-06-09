import os
from langchain.llms import OpenAI


def main():
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    # print('Hello World!')

    text = "What would be a good company name for a company that makes colorful socks?"
    print(llm(text))
