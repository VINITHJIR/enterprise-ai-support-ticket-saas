from app.agents.generic_autonomous_agent import (
    GenericAutonomousAgent
)


class AutonomousInvoiceAgent:

    @staticmethod
    def process(
        state
    ):

        return (
            GenericAutonomousAgent.process(
                state,
                "INVOICE"
            )
        )