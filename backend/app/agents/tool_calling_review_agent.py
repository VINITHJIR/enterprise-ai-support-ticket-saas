from app.ai.openai_client import (
    llm
)

from app.tools.review_complaint_tool import (
    review_complaint_tool
)

from app.runtime.tool_executor import (
    ToolExecutor
)


tools = [
    review_complaint_tool
]

tool_map = {
    "review_complaint_tool":
    review_complaint_tool
}

llm_with_tools = (
    llm.bind_tools(
        tools
    )
)


class ToolCallingReviewAgent:

    @staticmethod
    def process(
        state
    ):

        prompt = f"""
You are a Google Review Support Agent.

If the user reports
review issues,
review removal,
negative reviews,
or review complaints,

call review_complaint_tool.

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