from app.models.ticket_model import (
    Ticket
)

from app.models.complaint_model import (
    Complaint
)

from app.enums.ticket_enum import (
    TicketStatus
)

from app.enums.complaint_enum import (
    ComplaintStatus
)


def reopen_ticket_tool(
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
            "success": False,
            "message":
            "Ticket not found"
        }

    complaint = (
        db.query(Complaint)
        .filter(
            Complaint.id ==
            ticket.complaint_id
        )
        .first()
    )

    ticket.status = (
        TicketStatus.OPEN
    )

    if complaint:

        complaint.status = (
            ComplaintStatus.OPEN
        )

    db.commit()

    return {

        "success": True,

        "ticket_id":
        ticket.id,

        "complaint_id":
        ticket.complaint_id,

        "ticket_status":
        ticket.status.value,

        "complaint_status":
        complaint.status.value
        if complaint else None
    }