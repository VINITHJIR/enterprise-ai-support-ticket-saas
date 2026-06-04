from langchain.tools import tool


@tool
def autonomous_hr_response_tool():

    """
    Generate HR response.
    """

    return {
        "response":
        "HR complaint processed successfully."
    }