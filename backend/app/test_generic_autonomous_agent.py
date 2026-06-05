# app/test_generic_autonomous_agent.py

import app.models

from app.core.database import (
    SessionLocal
)

from app.agents.generic_autonomous_agent import (
    GenericAutonomousAgent
)

db = SessionLocal()

state = {

    "message":
    "Invoice not generated for last 10 days",

    "user_id":
    1,

    "category":
    "INVOICE",

    "priority":
    "HIGH",

    "db":
    db
}

result = (
    GenericAutonomousAgent.process(
        state,
        "INVOICE"
    )
)

print(result)