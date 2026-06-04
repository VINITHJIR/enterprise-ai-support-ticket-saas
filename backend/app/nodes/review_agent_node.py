from app.agents.tool_calling_review_agent import (
    ToolCallingReviewAgent
)


def review_agent_node(
    state
):

    return (
        ToolCallingReviewAgent.process(
            state
        )
    )