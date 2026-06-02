from langchain.tools import tool


@tool
def escalation_email_tool(
        ticket_id: int,
        db
):

    """
    Create escalation email.
    """

    from app.services.escalation_email_service import (
        EscalationEmailService
    )

    EscalationEmailService.create_escalation_email(
        db=db,
        ticket_id=ticket_id,
        email_content=(
            f"Ticket {ticket_id} escalated"
        )
    )

    return {
        "email_created": True
    }