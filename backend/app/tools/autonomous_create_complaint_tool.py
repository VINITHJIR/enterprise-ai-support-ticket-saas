from langchain.tools import tool

from app.runtime.agent_context import (
    AgentContext
)

from app.services.complaint_service import (
    ComplaintService
)


@tool
def autonomous_create_complaint_tool():

    """
    Create complaint.
    """

    state = (
        AgentContext.get_state()
    )

    complaint = (
        ComplaintService.create_complaint(
            db=state["db"],
            user_id=state["user_id"],
            complaint_text=state["message"],
            category=state["category"]
        )
    )

    return {
        "complaint_id": complaint.id
    }