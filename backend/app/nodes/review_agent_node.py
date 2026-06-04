from app.agents.autonomous_review_agent import (
    AutonomousReviewAgent
)

def review_agent_node(state):

    state["response"] = (
        AutonomousReviewAgent.process(
            state
        )
    )

    return state