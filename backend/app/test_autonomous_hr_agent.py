import app.models

from app.agents.autonomous_hr_agent import (
    AutonomousHRAgent
)

from app.core.database import (
    SessionLocal
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
    AutonomousHRAgent.process(
        state
    )
)

print(result)