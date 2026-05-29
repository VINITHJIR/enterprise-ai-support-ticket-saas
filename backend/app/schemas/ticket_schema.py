from pydantic import BaseModel

from app.enums.ticket_enum import (
    TicketPriority,
    TicketStatus
)


class TicketResponse(BaseModel):

    id: int

    priority: TicketPriority

    status: TicketStatus

    assigned_agent: str | None

    class Config:

        from_attributes = True