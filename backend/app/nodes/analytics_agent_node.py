from app.agents.tool_calling_analytics_agent import (
    ToolCallingAnalyticsAgent
)


def analytics_agent_node(
    state
):

   result = ToolCallingAnalyticsAgent.process(state)

   print("ANALYTICS NODE RESULT =", result)

   return result