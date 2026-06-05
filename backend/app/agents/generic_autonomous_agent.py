# app/agents/generic_autonomous_agent.py

from app.ai.openai_client import llm

from app.runtime.agent_context import (
    AgentContext
)

from app.tools.generic_complaint_check_tool import (
    generic_complaint_check_tool
)

from app.tools.generic_create_complaint_tool import (
    generic_create_complaint_tool
)

from app.tools.generic_create_ticket_tool import (
    generic_create_ticket_tool
)

from app.tools.generic_escalation_tool import (
    generic_escalation_tool
)

from app.tools.generic_response_tool import (
    generic_response_tool
)


class GenericAutonomousAgent:

    tools = [

        generic_complaint_check_tool,
        generic_create_complaint_tool,
        generic_create_ticket_tool,
        generic_escalation_tool,
        generic_response_tool
    ]

    tool_map = {

        "generic_complaint_check_tool":
        generic_complaint_check_tool,

        "generic_create_complaint_tool":
        generic_create_complaint_tool,

        "generic_create_ticket_tool":
        generic_create_ticket_tool,

        "generic_escalation_tool":
        generic_escalation_tool,

        "generic_response_tool":
        generic_response_tool
    }

    @classmethod
    def process(
        cls,
        state,
        agent_type
    ):

        AgentContext.set_state(
            state
        )

        llm_with_tools = (
            llm.bind_tools(
                cls.tools
            )
        )

        messages = [

            (
                "system",
                f"""
You are an autonomous {agent_type} Support Agent.

Available Tools:

1. generic_complaint_check_tool
2. generic_create_complaint_tool
3. generic_create_ticket_tool
4. generic_escalation_tool
5. generic_response_tool

Rules:

1. Always check complaint first.

2. If complaint exists:
   escalate it.

3. If complaint does not exist:
   create complaint
   create ticket

4. If priority is HIGH:
   escalate ticket.

5. Always generate response.

Never ask user what to do.

Complete the workflow yourself.
"""
            ),

            (
                "human",
                f"""
Message:
{state["message"]}

Category:
{state["category"]}

Priority:
{state["priority"]}
"""
            )
        ]

        while True:

            response = (
                llm_with_tools.invoke(
                    messages
                )
            )

            messages.append(
                response
            )

            if not response.tool_calls:

                return response.content

            for tool_call in response.tool_calls:

                tool_name = (
                    tool_call["name"]
                )

                tool_result = (
                    cls.tool_map[
                        tool_name
                    ].invoke(
                        tool_call["args"]
                    )
                )

                print(
                    f"TOOL EXECUTED => {tool_name}"
                )

                print(
                    f"RESULT => {tool_result}"
                )

                if "complaint_id" in tool_result:

                    state["complaint_id"] = (
                        tool_result[
                            "complaint_id"
                        ]
                    )

                if "ticket_id" in tool_result:

                    state["ticket_id"] = (
                        tool_result[
                            "ticket_id"
                        ]
                    )

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id":
                        tool_call["id"],
                        "content":
                        str(tool_result)
                    }
                )