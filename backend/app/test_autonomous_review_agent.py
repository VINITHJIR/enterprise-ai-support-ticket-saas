import app.models

from app.agents.autonomous_review_agent import (
    AutonomousReviewAgent
)

from app.core.database import (
    SessionLocal
)

db = SessionLocal()

state = {

    "message":
    "Google review removed unfairly",

    "user_id":
    1,

    "db":
    db,

    "category":
    "GOOGLE_REVIEW",

    "priority":
    "HIGH"
}

result = (
    AutonomousReviewAgent.process(
        state
    )
)

print(result)