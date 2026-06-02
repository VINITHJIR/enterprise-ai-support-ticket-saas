from app.services.complaint_service import (
    ComplaintService
)


def check_existing_node(state):

    complaint = (
        ComplaintService.check_existing_complaint(
            db=state["db"],
            user_id=state["user_id"],
            category=state["category"]
        )
    )

    if complaint:

        state["complaint_exists"] = True
        state["complaint_id"] = complaint.id

    else:

        state["complaint_exists"] = False

    return state