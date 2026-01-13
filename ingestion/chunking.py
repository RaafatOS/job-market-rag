from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_text(text: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=80
    )
    return splitter.split_text(text)
