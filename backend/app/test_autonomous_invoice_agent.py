import app.models

from app.core.database import (
    SessionLocal
)

from app.agents.autonomous_invoice_agent import (
    AutonomousInvoiceAgent
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
    AutonomousInvoiceAgent.process(
        state
    )
)

print(result)