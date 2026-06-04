from app.ai.openai_client import (
    llm
)

from app.tools.analytics_tool import (
    analytics_tool
)

from app.runtime.tool_executor import (
    ToolExecutor
)


tools = [
    analytics_tool
]

tool_map = {
    "analytics_tool":
    analytics_tool
}

llm_with_tools = (
    llm.bind_tools(
        tools
    )
)


class ToolCallingAnalyticsAgent:

    @staticmethod
    def process(
        state
    ):

        prompt = f"""
You are an Analytics Agent.

You MUST call analytics_tool whenever the user asks:

- How many complaints
- How many tickets
- Statistics
- Analytics
- Reports
- Dashboard metrics

Never answer from your own knowledge.

Always call analytics_tool first.

User message:

{state["message"]}
"""

        response = (
            llm_with_tools.invoke(
                prompt
            )
        )
        print("LLM RESPONSE =", response)
        print("TOOL CALLS =", response.tool_calls)
        if response.tool_calls:

            tool_call = response.tool_calls[0]

            tool_name = tool_call["name"]

            tool_result = (
                tool_map[
                    tool_name
                ].invoke({})
            )

            analytics_result = (
                ToolExecutor.execute(
                    tool_result,
                    state
                )
            )

            state["response"] = analytics_result

            return state