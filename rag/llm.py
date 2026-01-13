from langchain_openai import OpenAI

def load_llm():
    return OpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo-instruct"
    )
