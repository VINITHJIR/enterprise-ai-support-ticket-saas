import app.models

from app.core.database import (
    SessionLocal
)

from app.agents.tool_calling_analytics_agent import (
    ToolCallingAnalyticsAgent
)

db = SessionLocal()

state = {

    "message":
    "How many complaints are there?",

    "db":
    db
}

result = (
    ToolCallingAnalyticsAgent.process(
        state
    )
)

print(result)