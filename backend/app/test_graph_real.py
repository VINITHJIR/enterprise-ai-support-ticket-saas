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
    "Recruiter not responding",

    "user_id":
    1,

    "db":
    db
    }
)

print(result)

