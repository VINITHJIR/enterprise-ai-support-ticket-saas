from langchain_core.tools import tool

from app.runtime.agent_context import (
    AgentContext
)

from app.services.ticket_service import (
    TicketService
)


@tool
def generic_create_ticket_tool():
    """
    Create support ticket.
    """

    state = AgentContext.get_state()

    ticket = (
        TicketService.create_ticket(
            db=state["db"],
            complaint_id=state["complaint_id"],
            priority=state["priority"]
        )
    )

    return {
        "ticket_id": ticket.id
    }