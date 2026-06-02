from app.agents.hr_agent import (
    HRAgent
)


def hr_agent_node(state):

    response = (
        HRAgent.handle(
            state["message"]
        )
    )

    state["response"] = response

    return state