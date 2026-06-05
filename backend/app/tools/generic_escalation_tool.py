from langchain.tools import tool

from app.runtime.agent_context import (
    AgentContext
)

from app.services.ticket_service import (
    TicketService
)

from app.services.escalation_email_service import (
    EscalationEmailService
)


@tool
def generic_escalation_tool():

    """
    Escalate existing complaint.
    """

    state = (
        AgentContext.get_state()
    )

    ticket = (
        TicketService.get_ticket_by_complaint(
            state["db"],
            state["complaint_id"]
        )
    )

    if not ticket:

        return {
            "escalated": False
        }

    updated_ticket = (
        TicketService.increase_priority(
            state["db"],
            ticket,
            "HIGH"
        )
    )

    EscalationEmailService.create_escalation_email(
        db=state["db"],
        ticket_id=updated_ticket.id,
        email_content=(
            f"Ticket {updated_ticket.id} escalated"
        )
    )

    return {
        "escalated": True,
        "ticket_id": updated_ticket.id
    }