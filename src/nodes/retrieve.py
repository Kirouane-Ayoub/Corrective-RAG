import settings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFDirectoryLoader
from models import embeddings

print("Loading Data...")
loader = PyPDFDirectoryLoader("src/data_input")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=settings.CHUNK_SIZE, chunk_overlap=settings.CHUNK_OVERLAP
)
chunks = text_splitter.split_documents(documents)

print("create chroma database...")
db = Chroma.from_documents(chunks, embeddings)

print("create retriever...")
retriever = db.as_retriever(search_kwargs={"k": 8})


### Retriever ###
def retrieve(state):
    """
    Retrieve documents

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): New key added to state, documents, that contains retrieved documents
    """
    print("---RETRIEVE---")
    state_dict = state["keys"]
    question = state_dict["question"]
    documents = retriever.invoke(question)
    return {"keys": {"documents": documents, "question": question}}
