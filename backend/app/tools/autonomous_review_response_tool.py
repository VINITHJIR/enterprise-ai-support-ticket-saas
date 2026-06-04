from langchain.tools import tool


@tool
def autonomous_review_response_tool():

    """
    Generate review response.
    """

    return {
        "response":
        "Google review complaint processed successfully."
    }