from langchain.tools import tool


@tool
def autonomous_response_tool():

    """
    Generate final customer response.
    """

    return {
        "response":
        "Complaint processed successfully."
    }