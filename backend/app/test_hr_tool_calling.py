import app.models

from app.core.database import (
    SessionLocal
)

from app.agents.tool_calling_hr_agent import (
    ToolCallingHRAgent
)

db = SessionLocal()

state = {

    "message":
    "Recruiter not responding after interview",

    "user_id":
    1,

    "db":
    db,

    "category":
    "HR_RECRUITMENT",

    "priority":
    "HIGH"
}

result = (
    ToolCallingHRAgent.process(
        state
    )
)

print(result)