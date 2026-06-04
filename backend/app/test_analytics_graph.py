import app.models

from app.graphs.support_graph import (
    support_graph
)

from app.core.database import (
    SessionLocal
)

db = SessionLocal()

result = (
    support_graph.invoke(
        {
            "message":
            "How many complaints are there?",

            "user_id":
            2,

            "db":
            db
        }
    )
)

print(result)