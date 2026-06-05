from langchain.tools import tool


@tool
def generic_response_tool():

    """
    Generate final customer response.
    """

    return {
        "response":
        "Complaint processed successfully."
    }