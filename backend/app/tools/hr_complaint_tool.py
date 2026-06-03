from langchain.tools import tool


@tool
def hr_complaint_tool(
    complaint_text: str
):
    """
    Handle HR recruitment complaints.
    """

    return {
        "action": "CREATE_HR_COMPLAINT",
        "complaint_text": complaint_text
    }