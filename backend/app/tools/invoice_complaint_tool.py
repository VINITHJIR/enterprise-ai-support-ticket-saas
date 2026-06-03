from langchain.tools import tool


@tool
def invoice_complaint_tool(
    complaint_text: str
):
    """
    Handle invoice related complaints.
    """

    return {
        "action": "CREATE_INVOICE_COMPLAINT",
        "complaint_text": complaint_text
    }