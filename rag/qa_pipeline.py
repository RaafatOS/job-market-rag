def answer_question(llm, retriever, question):
    docs = retriever.get_relevant_documents(question)
    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
    You are an AI assistant specialized in job market analysis.
    Answer ONLY using the provided context.
    If the answer is not in the context, say you don't know.

    Context:
    {context}

    Question:
    {question}
    """

    return llm(prompt)
