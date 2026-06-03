import app.models

from app.graphs.support_graph import (
    support_graph
)

from app.core.database import (
    SessionLocal
)

db = SessionLocal()

result = support_graph.invoke(
    {
        "message":
        "Invoice not generated for last 10 days",

        "user_id":
        1,

        "db":
        db
    }
)

print(result)