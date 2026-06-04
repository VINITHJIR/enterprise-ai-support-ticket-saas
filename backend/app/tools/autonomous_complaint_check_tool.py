from langchain.tools import tool

from app.runtime.agent_context import (
    AgentContext
)

from app.services.complaint_service import (
    ComplaintService
)


@tool
def autonomous_complaint_check_tool():

    """
    Check whether complaint exists.
    """

    state = (
        AgentContext.get_state()
    )

    complaint = (
        ComplaintService.check_existing_complaint(
            db=state["db"],
            user_id=state["user_id"],
            category=state["category"]
        )
    )

    if complaint:

        return {
            "exists": True,
            "complaint_id": complaint.id
        }

    return {
        "exists": False
    }