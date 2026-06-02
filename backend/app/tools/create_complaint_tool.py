from langchain.tools import tool


@tool
def create_complaint_tool(
        user_id: int,
        complaint_text: str,
        category: str,
        db
):

    """
    Create complaint.
    """

    from app.services.complaint_service import (
        ComplaintService
    )

    complaint = (
        ComplaintService.create_complaint(
            db=db,
            user_id=user_id,
            complaint_text=complaint_text,
            category=category
        )
    )

    return {
        "complaint_id": complaint.id
    }