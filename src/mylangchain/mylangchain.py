import os
from langchain.llms import OpenAI

def main():
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    # print('Hello World!')