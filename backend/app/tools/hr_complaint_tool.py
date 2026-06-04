from langchain.tools import tool


@tool
def hr_complaint_tool(
    complaint_text: str
):
    """
    Create an HR complaint request.
    """

    return {
        "action":
        "CREATE_HR_COMPLAINT",

        "complaint_text":
        complaint_text
    }