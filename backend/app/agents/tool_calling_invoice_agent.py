from app.ai.openai_client import llm

from app.tools.invoice_complaint_tool import (
    invoice_complaint_tool
)

from app.runtime.tool_executor import (
    ToolExecutor
)

tools = [
    invoice_complaint_tool
]

tool_map = {
    "invoice_complaint_tool":
    invoice_complaint_tool
}

llm_with_tools = (
    llm.bind_tools(
        tools
    )
)


class ToolCallingInvoiceAgent:

    @staticmethod
    def process(
        state
    ):

        prompt = f"""
You are an Invoice Support Agent.

If the user reports an invoice issue,
call invoice_complaint_tool.

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

            execution_result = (
                ToolExecutor.execute(
                    tool_result,
                    state
                )
            )


            return execution_result

        return {
            "message":
            response.content
        }