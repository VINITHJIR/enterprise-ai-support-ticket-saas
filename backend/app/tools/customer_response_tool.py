from langchain.tools import tool

from app.ai.response_generator import (
    generate_response
)


@tool
def customer_response_tool(
        message: str
):

    """
    Generate customer response.
    """

    return generate_response(
        message
    )