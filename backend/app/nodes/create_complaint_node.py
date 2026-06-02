from app.services.complaint_service import (
    ComplaintService
)


def create_complaint_node(state):

    complaint = (
        ComplaintService.create_complaint(
            db=state["db"],
            user_id=state["user_id"],
            complaint_text=state["message"],
            category=state["category"]
        )
    )

    state["complaint_id"] = complaint.id

    return state