from langchain.tools import tool

from app.ai.complaint_analyzer import (
    analyze_message
)


@tool
def complaint_analysis_tool(
        message: str
):

    """
    Analyze customer message.
    Detect complaint category and priority.
    """

    return analyze_message(
        message
    )