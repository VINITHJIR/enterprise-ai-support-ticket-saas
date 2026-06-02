from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.chat_schema import (
    ChatRequest
)

from app.dependencies.auth_dependency import (
    get_current_user
)

from app.models.user_model import User

from app.orchestrators.support_orchestrator import (
    SupportOrchestrator
)

from app.ai.response_generator import (
    generate_response
)

from app.services.complaint_service import (
    ComplaintService
)

from app.services.ticket_service import (
    TicketService
)

from app.services.escalation_email_service import (
    EscalationEmailService
)

from app.enums.ticket_enum import (
    TicketPriority
)

router = APIRouter(
    prefix="/api/chat",
    tags=["AI Chat"]
)


@router.post("/")
def chat(
        request: ChatRequest,
        db: Session = Depends(get_db),
        current_user: User = Depends(
            get_current_user
        )
):

    result = (
        SupportOrchestrator.process(
            request.message
        )
    )

    analysis = result["analysis"]

    # NORMAL CHAT

    if not analysis["is_complaint"]:

        response = generate_response(
            request.message
        )

        return {
            "type": "CHAT",
            "response": response
        }

    # COMPLAINT FLOW

    existing_complaint = (
        ComplaintService.check_existing_complaint(
            db=db,
            user_id=current_user.id,
            category=analysis["category"]
        )
    )

    # DUPLICATE COMPLAINT

    if existing_complaint:

        ticket = (
            TicketService.get_ticket_by_complaint(
                db,
                existing_complaint.id
            )
        )

        if ticket:

            updated_ticket = (
                TicketService.increase_priority(
                    db,
                    ticket
                )
            )

            EscalationEmailService.create_escalation_email(
                db=db,
                ticket_id=updated_ticket.id,
                email_content=(
                    f"Complaint escalated. "
                    f"Ticket ID {updated_ticket.id}"
                )
            )

            return {
                "type": "COMPLAINT",
                "is_duplicate": True,
                "complaint_id": existing_complaint.id,
                "ticket_id": updated_ticket.id,
                "category": analysis["category"],
                "priority": updated_ticket.priority.value
            }

    # NEW COMPLAINT

    complaint = (
        ComplaintService.create_complaint(
            db=db,
            user_id=current_user.id,
            complaint_text=request.message,
            category=analysis["category"]
        )
    )

    priority_mapping = {
        "LOW": TicketPriority.LOW,
        "MEDIUM": TicketPriority.MEDIUM,
        "HIGH": TicketPriority.HIGH
    }

    ticket = (
        TicketService.create_ticket(
            db=db,
            complaint_id=complaint.id,
            priority=priority_mapping[
                analysis["priority"]
            ]
        )
    )

    return {
        "type": "COMPLAINT",
        "is_duplicate": False,
        "complaint_id": complaint.id,
        "ticket_id": ticket.id,
        "category": analysis["category"],
        "priority": analysis["priority"]
    }