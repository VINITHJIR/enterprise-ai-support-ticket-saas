from langchain.tools import tool

from app.core.database import (
    SessionLocal
)

from app.tools.get_ticket_status_tool import (
    get_ticket_status_tool
)

from app.tools.close_ticket_tool import (
    close_ticket_tool
)

from app.tools.reopen_ticket_tool import (
    reopen_ticket_tool
)


@tool
def ticket_status_tool(
    ticket_id: int
):
    """
    Get ticket status.
    """

    db = SessionLocal()

    return (
        get_ticket_status_tool(
            db,
            ticket_id
        )
    )


@tool
def close_ticket_agent_tool(
    ticket_id: int
):
    """
    Close ticket and complaint.
    """

    db = SessionLocal()

    return (
        close_ticket_tool(
            db,
            ticket_id
        )
    )


@tool
def reopen_ticket_agent_tool(
    ticket_id: int
):
    """
    Reopen ticket and complaint.
    """

    db = SessionLocal()

    return (
        reopen_ticket_tool(
            db,
            ticket_id
        )
    )