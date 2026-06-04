from app.ai.openai_client import llm

from app.runtime.agent_context import (
    AgentContext
)

from app.tools.autonomous_hr_check_tool import (
    autonomous_hr_check_tool
)

from app.tools.autonomous_hr_create_complaint_tool import (
    autonomous_hr_create_complaint_tool
)

from app.tools.autonomous_create_ticket_tool import (
    autonomous_create_ticket_tool
)

from app.tools.autonomous_escalation_tool import (
    autonomous_escalation_tool
)
from app.tools.autonomous_hr_response_tool import (
    autonomous_hr_response_tool
)

class AutonomousHRAgent:

    tools = [
    autonomous_hr_check_tool,
    autonomous_hr_create_complaint_tool,
    autonomous_create_ticket_tool,
    autonomous_escalation_tool,
    autonomous_hr_response_tool
]

    tool_map = {

        "autonomous_hr_check_tool":
        autonomous_hr_check_tool,

        "autonomous_hr_create_complaint_tool":
        autonomous_hr_create_complaint_tool,

        "autonomous_create_ticket_tool":
        autonomous_create_ticket_tool,

        "autonomous_escalation_tool":
        autonomous_escalation_tool,

        "autonomous_hr_response_tool":
        autonomous_hr_response_tool
    }

    @classmethod
    def process(
        cls,
        state
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
                """
You are an autonomous HR Support Agent.

Workflow:

1. Check HR complaint existence.

2. If complaint exists:
   call autonomous_escalation_tool

3. If complaint does not exist:
   call autonomous_hr_create_complaint_tool
   then autonomous_create_ticket_tool

4. Always call autonomous_hr_response_tool.

Never ask the user what to do.

Always complete the workflow yourself.
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

                # -------------------------
                # UPDATE STATE
                # -------------------------

                if "complaint_id" in tool_result:

                    state[
                        "complaint_id"
                    ] = (
                        tool_result[
                            "complaint_id"
                        ]
                    )

                if "ticket_id" in tool_result:

                    state[
                        "ticket_id"
                    ] = (
                        tool_result[
                            "ticket_id"
                        ]
                    )

                                # -------------------------
                # FORCE ESCALATION
                # -------------------------

                if (
                    tool_name ==
                    "autonomous_create_ticket_tool"
                    and
                    state["priority"] == "HIGH"
                ):

                    escalation_result = (
                        autonomous_escalation_tool.invoke(
                            {}
                        )
                    )

                    print(
                        "AUTO ESCALATION =>",
                        escalation_result
                    )

                # -------------------------
                # TOOL MESSAGE
                # -------------------------

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id":
                        tool_call["id"],
                        "content":
                        str(tool_result)
                    }
                )