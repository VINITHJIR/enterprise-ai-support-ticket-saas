from langchain.tools import tool


@tool
def review_complaint_tool(
    complaint_text: str
):
    """
    Handle review complaints.
    """

    return {
        "action": "CREATE_REVIEW_COMPLAINT",
        "complaint_text": complaint_text
    }