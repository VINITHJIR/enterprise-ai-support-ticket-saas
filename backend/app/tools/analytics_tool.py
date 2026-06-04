from langchain.tools import tool

from app.runtime.agent_context import (
    AgentContext
)

from app.services.analytics_service import (
    AnalyticsService
)


@tool
def analytics_tool():

    """
    Return support analytics.
    """

    state = AgentContext.get_state()

    return (
        AnalyticsService.get_dashboard_metrics(
            state["db"]
        )
    )