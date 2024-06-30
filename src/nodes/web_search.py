from langchain.schema import Document
from langchain_community.tools import DuckDuckGoSearchRun


def web_search(state):
    """
    Web search based on the re-phrased question using Tavily API.

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Web results appended to documents.
    """

    print("---WEB SEARCH---")
    state_dict = state["keys"]
    question = state_dict["question"]
    documents = state_dict["documents"]

    duckduckgo_search = DuckDuckGoSearchRun()
    docs = duckduckgo_search.invoke({"query": question})
    web_results = Document(page_content=docs)
    documents.append(web_results)

    return {"keys": {"documents": documents, "question": question}}
