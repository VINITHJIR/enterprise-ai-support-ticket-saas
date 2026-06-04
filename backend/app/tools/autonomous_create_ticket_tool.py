from langchain.tools import tool

from app.runtime.agent_context import (
    AgentContext
)

from app.services.ticket_service import (
    TicketService
)

from app.enums.ticket_enum import (
    TicketPriority
)


@tool
def autonomous_create_ticket_tool():

    """
    Create ticket.
    """

    state = (
        AgentContext.get_state()
    )

    priority_mapping = {

        "LOW":
        TicketPriority.LOW,

        "MEDIUM":
        TicketPriority.MEDIUM,

        "HIGH":
        TicketPriority.HIGH
    }

    complaint_id = (
        state["complaint_id"]
    )

    ticket = (
        TicketService.create_ticket(
            db=state["db"],
            complaint_id=complaint_id,
            priority=priority_mapping[
                state["priority"]
            ]
        )
    )

    return {
        "ticket_id": ticket.id
    }