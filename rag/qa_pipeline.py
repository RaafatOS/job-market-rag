from langchain_core.messages import HumanMessage, SystemMessage

from rag.prompt import SYSTEM_PROMPT


def answer_question(llm, retriever, question):
    docs = retriever.invoke(question)
    context = "\n\n".join(d.page_content for d in docs)

    response = llm.invoke(
        [
            SystemMessage(content=SYSTEM_PROMPT.strip()),
            HumanMessage(content=f"Context:\n{context}\n\nQuestion:\n{question}"),
        ]
    )
    return response.content
