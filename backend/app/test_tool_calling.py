import app.models

from app.agents.tool_calling_invoice_agent import (
    ToolCallingInvoiceAgent
)

from app.core.database import (
    SessionLocal
)

db = SessionLocal()

state = {
    "message":
    "Invoice not generated for last 10 days",

    "user_id":
    1,

    "db":
    db,

    "category":
    "INVOICE",

    "priority":
    "HIGH"
}

result = (
    ToolCallingInvoiceAgent.process(
        state
    )
)

print(
    "\nFINAL RESULT =",
    result
)