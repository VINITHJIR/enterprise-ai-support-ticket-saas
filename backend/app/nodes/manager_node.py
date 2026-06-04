from app.agents.manager_agent import (
    ManagerAgent
)


def manager_node(
    state
):

    state["selected_agent"] = (
        ManagerAgent.route(
            state["category"]
        )
    )

    return state