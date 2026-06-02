from app.agents.support_agent import (
    SupportAgent
)


class SupportOrchestrator:

    @staticmethod
    def process(
            message: str
    ):

        return (
            SupportAgent.process_message(
                message
            )
        )