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


def execute_invoice_workflow(
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
        print("DUPLICATE FLOW ENTERED")
        ticket = (
            TicketService.get_ticket_by_complaint(
                state["db"],
                existing_complaint.id
            )
        )
        print("FOUND TICKET =", ticket)
        if ticket:
            
            print(
                "CURRENT PRIORITY =",
                ticket.priority
            )

            updated_ticket = (
                TicketService.increase_priority(
                    state["db"],
                    ticket=ticket,
                    target_priority=state["priority"]
                )
            )

            print(
                "UPDATED PRIORITY =",
                updated_ticket.priority
            )

            EscalationEmailService.create_escalation_email(
                db=state["db"],
                ticket_id=updated_ticket.id,
                email_content=(
                    f"Complaint escalated. "
                    f"Ticket ID {updated_ticket.id}"
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
    # NEW COMPLAINT
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