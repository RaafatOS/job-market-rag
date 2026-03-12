from dotenv import load_dotenv

from rag.llm import load_llm
from rag.qa_pipeline import answer_question
from rag.retriever import load_retriever


def main():
    load_dotenv()
    llm = load_llm()
    retriever = load_retriever()

    print("Job Market RAG - ask a question (type 'exit' to quit)")

    while True:
        question = input("> ")
        if question.lower() == "exit":
            break

        answer = answer_question(llm, retriever, question)
        print("\nAnswer:\n", answer, "\n")


if __name__ == "__main__":
    main()
