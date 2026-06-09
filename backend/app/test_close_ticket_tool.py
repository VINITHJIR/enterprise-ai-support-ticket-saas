from app.core.database import (
    SessionLocal
)

from app.tools.close_ticket_tool import (
    close_ticket_tool
)

db = SessionLocal()

result = (
    close_ticket_tool(
        db=db,
        ticket_id=16
    )
)

print(result)