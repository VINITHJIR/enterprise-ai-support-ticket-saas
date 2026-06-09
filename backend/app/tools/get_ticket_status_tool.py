from app.models.ticket_model import (
    Ticket
)


def get_ticket_status_tool(
    db,
    ticket_id
):

    ticket = (
        db.query(Ticket)
        .filter(
            Ticket.id == ticket_id
        )
        .first()
    )

    if not ticket:

        return {
            "found": False,
            "message":
            "Ticket not found"
        }

    return {
        "found": True,
        "ticket_id":
        ticket.id,

        "status":
        ticket.status.value,

        "priority":
        ticket.priority.value,

        "assigned_agent":
        ticket.assigned_agent
    }