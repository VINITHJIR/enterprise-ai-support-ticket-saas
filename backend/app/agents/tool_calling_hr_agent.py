from app.ai.openai_client import (
    llm
)

from app.tools.hr_complaint_tool import (
    hr_complaint_tool
)

from app.runtime.tool_executor import (
    ToolExecutor
)


tools = [
    hr_complaint_tool
]

tool_map = {
    "hr_complaint_tool":
    hr_complaint_tool
}

llm_with_tools = (
    llm.bind_tools(
        tools
    )
)


class ToolCallingHRAgent:

    @staticmethod
    def process(
        state
    ):

        prompt = f"""
You are an HR Support Agent.

If the user reports an HR issue,
call hr_complaint_tool.

Message:

{state["message"]}
"""

        response = (
            llm_with_tools.invoke(
                prompt
            )
        )

        if response.tool_calls:

            tool_call = (
                response.tool_calls[0]
            )

            tool_name = (
                tool_call["name"]
            )

            tool_args = (
                tool_call["args"]
            )

            tool_result = (
                tool_map[
                    tool_name
                ].invoke(
                    tool_args
                )
            )

            return (
                ToolExecutor.execute(
                    tool_result,
                    state
                )
            )

        return {
            "response":
            response.content
        }