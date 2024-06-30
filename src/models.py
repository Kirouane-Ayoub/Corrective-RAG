import settings
from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings
from langchain_community.llms import Cohere

load_dotenv()
llm = Cohere(model=settings.COHERE_LLM_MODEL, temperature=0.5)
embeddings = CohereEmbeddings(model=settings.COHERE_EMBEDDING_MODEL)
