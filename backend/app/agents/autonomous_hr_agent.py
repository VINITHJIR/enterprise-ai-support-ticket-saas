from app.agents.generic_autonomous_agent import (
    GenericAutonomousAgent
)


class AutonomousHRAgent:

    @staticmethod
    def process(
        state
    ):

        return (
            GenericAutonomousAgent.process(
                state,
                "HR"
            )
        )