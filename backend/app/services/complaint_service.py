from sqlalchemy.orm import Session

from app.repositories.complaint_repository import (
    ComplaintRepository
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


class ComplaintService:

    @staticmethod
    def create_or_process_complaint(
            db: Session,
            user_id: int,
            complaint_text: str,
            category
    ):

        existing_complaint = (
            ComplaintRepository.find_existing_active_complaint(
                db=db,
                user_id=user_id,
                category=category
            )
        )

        # Complaint Already Exists

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
                        f"Complaint escalated."
                        f" Ticket {updated_ticket.id}"
                    )
                )

            return {
                "is_duplicate": True,
                "complaint": {
                    "id": existing_complaint.id,
                    "user_id": existing_complaint.user_id,
                    "complaint": existing_complaint.complaint,
                    "category": existing_complaint.category.value,
                    "status": existing_complaint.status.value
                }
            }

        # Create Complaint

        complaint = ComplaintRepository.create(
            db=db,
            user_id=user_id,
            complaint=complaint_text,
            category=category
        )

        # Create Ticket

        TicketService.create_ticket(
            db=db,
            complaint_id=complaint.id,
            priority=TicketPriority.MEDIUM
        )

        return {
            "is_duplicate": False,
            "complaint": complaint
        }
    
    @staticmethod
    def get_user_complaints(
            db: Session,
            user_id: int
    ):

        return ComplaintRepository.get_by_user(
            db,
            user_id
        )