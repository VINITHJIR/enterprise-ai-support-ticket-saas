from app.core.database import (
    SessionLocal
)

from app.tools.reopen_ticket_tool import (
    reopen_ticket_tool
)

db = SessionLocal()

result = (
    reopen_ticket_tool(
        db=db,
        ticket_id=16
    )
)

print(result)