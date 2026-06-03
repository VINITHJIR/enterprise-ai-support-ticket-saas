from app.agents.manager_agent import (
    ManagerAgent
)


def manager_node(state):

    selected_agent = (
        ManagerAgent.route(
            state["category"]
        )
    )

    state["selected_agent"] = (
        selected_agent
    )

    return state