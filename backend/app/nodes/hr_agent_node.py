from app.agents.autonomous_hr_agent import (
    AutonomousHRAgent
)

def hr_agent_node(state):

    state["response"] = (
        AutonomousHRAgent.process(
            state
        )
    )

    return state