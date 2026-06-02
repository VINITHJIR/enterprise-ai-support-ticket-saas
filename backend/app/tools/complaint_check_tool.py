from langchain.tools import tool


@tool
def complaint_check_tool(
        user_id: int,
        category: str,
        db
):

    """
    Check whether active complaint exists.
    """

    from app.services.complaint_service import (
        ComplaintService
    )

    complaint = (
        ComplaintService.check_existing_complaint(
            db=db,
            user_id=user_id,
            category=category
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