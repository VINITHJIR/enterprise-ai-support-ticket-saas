from app.core.database import (
    SessionLocal
)

from app.tools.get_ticket_status_tool import (
    get_ticket_status_tool
)

db = SessionLocal()

result = (
    get_ticket_status_tool(
        db=db,
        ticket_id=16
    )
)

print(result)