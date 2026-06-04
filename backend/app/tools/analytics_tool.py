from langchain.tools import tool


@tool
def analytics_tool():

    """
    Get support analytics.
    """

    return {
        "action":
        "GET_ANALYTICS"
    }