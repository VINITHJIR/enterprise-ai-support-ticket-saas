import app.models

from app.core.database import (
    SessionLocal
)

from app.agents.tool_calling_review_agent import (
    ToolCallingReviewAgent
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
    ToolCallingReviewAgent.process(
        state
    )
)

print(result)