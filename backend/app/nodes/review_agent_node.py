from app.agents.review_agent import (
    ReviewAgent
)


def review_agent_node(state):

    response = (
        ReviewAgent.handle(
            state["message"]
        )
    )

    state["response"] = response
    print("Review Agent Executed")
    return state