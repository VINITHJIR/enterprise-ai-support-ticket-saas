from app.services.complaint_service import (
    ComplaintService
)

from app.services.ticket_service import (
    TicketService
)

from app.services.escalation_email_service import (
    EscalationEmailService
)

from app.enums.ticket_enum import (
    TicketPriority
)


def execute_complaint_workflow(
    state,
    tool_result
):

    # -------------------------
    # CHECK EXISTING COMPLAINT
    # -------------------------

    existing_complaint = (
        ComplaintService.check_existing_complaint(
            db=state["db"],
            user_id=state["user_id"],
            category=state["category"]
        )
    )

    # -------------------------
    # DUPLICATE COMPLAINT
    # -------------------------

    if existing_complaint:

        ticket = (
            TicketService.get_ticket_by_complaint(
                state["db"],
                existing_complaint.id
            )
        )

        if ticket:

            updated_ticket = (
                TicketService.increase_priority(
                    db=state["db"],
                    ticket=ticket,
                    target_priority=state["priority"]
                )
            )

            EscalationEmailService.create_escalation_email(
                db=state["db"],
                ticket_id=updated_ticket.id,
                email_content=(
                    f"{state['category']} complaint escalated"
                )
            )

            return {
                "is_duplicate": True,
                "complaint_id":
                existing_complaint.id,

                "ticket_id":
                updated_ticket.id
            }

    # -------------------------
    # CREATE COMPLAINT
    # -------------------------

    complaint = (
        ComplaintService.create_complaint(
            db=state["db"],
            user_id=state["user_id"],
            complaint_text=tool_result[
                "complaint_text"
            ],
            category=state["category"]
        )
    )

    priority_mapping = {
        "LOW": TicketPriority.LOW,
        "MEDIUM": TicketPriority.MEDIUM,
        "HIGH": TicketPriority.HIGH
    }

    ticket = (
        TicketService.create_ticket(
            db=state["db"],
            complaint_id=complaint.id,
            priority=priority_mapping[
                state["priority"]
            ]
        )
    )

    return {
        "is_duplicate": False,
        "complaint_id": complaint.id,
        "ticket_id": ticket.id
    }