from app.agents.tool_calling_hr_agent import (
    ToolCallingHRAgent
)


def hr_agent_node(
    state
):

    return (
        ToolCallingHRAgent.process(
            state
        )
    )