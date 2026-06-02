from app.services.ticket_service import (
    TicketService
)

from app.enums.ticket_enum import (
    TicketPriority
)


def create_ticket_node(state):

    priority_map = {
        "LOW": TicketPriority.LOW,
        "MEDIUM": TicketPriority.MEDIUM,
        "HIGH": TicketPriority.HIGH
    }

    ticket = (
        TicketService.create_ticket(
            db=state["db"],
            complaint_id=state["complaint_id"],
            priority=priority_map[
                state["priority"]
            ]
        )
    )

    state["ticket_id"] = ticket.id

    return state