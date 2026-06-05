import app.models

from app.core.database import (
    SessionLocal
)

from app.runtime.agent_context import (
    AgentContext
)

from app.tools.generic_complaint_check_tool import (
    generic_complaint_check_tool
)

from app.tools.generic_create_complaint_tool import (
    generic_create_complaint_tool
)

from app.tools.generic_create_ticket_tool import (
    generic_create_ticket_tool
)

from app.tools.generic_escalation_tool import (
    generic_escalation_tool
)

from app.tools.generic_response_tool import (
    generic_response_tool
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

AgentContext.set_state(
    state
)

print(
    "\nCHECK TOOL\n"
)

result = (
    generic_complaint_check_tool.invoke(
        {}
    )
)

print(result)

print(
    "\nCREATE COMPLAINT TOOL\n"
)

result = (
    generic_create_complaint_tool.invoke(
        {}
    )
)

print(result)

if "complaint_id" in result:

    state["complaint_id"] = (
        result["complaint_id"]
    )

print(
    "\nCREATE TICKET TOOL\n"
)

result = (
    generic_create_ticket_tool.invoke(
        {}
    )
)

print(result)

if "ticket_id" in result:

    state["ticket_id"] = (
        result["ticket_id"]
    )

print(
    "\nESCALATION TOOL\n"
)

result = (
    generic_escalation_tool.invoke(
        {}
    )
)

print(result)

print(
    "\nRESPONSE TOOL\n"
)

result = (
    generic_response_tool.invoke(
        {}
    )
)

print(result)