from app.graphs.support_graph import (
    support_graph
)


class LangGraphOrchestrator:

    @staticmethod
    def process(
            message: str,
            user_id: int,
            db
    ):

        return support_graph.invoke(
            {
                "message": message,
                "user_id": user_id,
                "db": db
            }
        )