from langchain.tools import tool

from app.enums.ticket_enum import (
    TicketPriority
)


@tool
def create_ticket_tool(
        complaint_id: int,
        priority: str,
        db
):

    """
    Create support ticket.
    """

    from app.services.ticket_service import (
        TicketService
    )

    priority_mapping = {
        "LOW": TicketPriority.LOW,
        "MEDIUM": TicketPriority.MEDIUM,
        "HIGH": TicketPriority.HIGH
    }

    ticket = (
        TicketService.create_ticket(
            db=db,
            complaint_id=complaint_id,
            priority=priority_mapping[
                priority
            ]
        )
    )

    return {
        "ticket_id": ticket.id
    }