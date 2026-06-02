from app.services.ticket_service import (
    TicketService
)


def increase_priority_node(state):

    ticket = (
        TicketService.get_ticket_by_complaint(
            state["db"],
            state["complaint_id"]
        )
    )

    updated_ticket = (
        TicketService.increase_priority(
            state["db"],
            ticket
        )
    )

    state["ticket_id"] = updated_ticket.id

    return state