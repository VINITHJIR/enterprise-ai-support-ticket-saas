from app.agents.generic_autonomous_agent import (
    GenericAutonomousAgent
)


class AutonomousReviewAgent:

    @staticmethod
    def process(
        state
    ):

        return (
            GenericAutonomousAgent.process(
                state,
                "GOOGLE_REVIEW"
            )
        )