from app.ai.openai_client import (
    llm
)
from app.runtime.agent_context import (
    AgentContext
)
from app.tools.analytics_tool import (
    analytics_tool
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
        AgentContext.set_state(
    state
)

        prompt = f"""
        You are an Analytics Agent.

        Always use analytics_tool.

        Questions may include:

        - How many complaints?
        - How many tickets?
        - How many escalations?
        - How many invoice complaints?
        - How many HR complaints?
        - How many review complaints?

        Never answer from memory.

        Always call analytics_tool first.

        User:

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

        analytics_result = tool_result

        print(
            "ANALYTICS RESULT =",
            analytics_result
        )

        state["response"] = analytics_result

        return state