from app.services.escalation_email_service import (
    EscalationEmailService
)


def escalation_node(state):

    EscalationEmailService.create_escalation_email(
        db=state["db"],
        ticket_id=state["ticket_id"],
        email_content=(
            f"Ticket {state['ticket_id']} escalated"
        )
    )

    return state