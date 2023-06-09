import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def main():
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)

    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    chain.run("colorful socks")
