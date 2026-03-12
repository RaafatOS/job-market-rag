from langchain_openai import ChatOpenAI


def load_llm():
    return ChatOpenAI(
        temperature=0,
        model="gpt-4o-mini",
    )
