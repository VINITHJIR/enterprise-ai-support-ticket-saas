from langchain.tools import tool


@tool
def review_complaint_tool(
    complaint_text: str
):
    """
    Create review complaint request.
    """

    return {
        "action":
        "CREATE_REVIEW_COMPLAINT",

        "complaint_text":
        complaint_text
    }