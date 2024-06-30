from graph import app


def generate_corrective_rag_response(question):
    """
    Generate a detailed explanation of Corrective RAG using the provided question.

    Parameters:
    question (str): The question to be answered.

    Returns:
    str: The final generated answer.
    """
    inputs = {"keys": {"question": question}}

    final_generation = ""

    for output in app.stream(inputs):
        for _, value in output.items():
            if "keys" in value and "generation" in value["keys"]:
                final_generation = value["keys"]["generation"]

    return final_generation
