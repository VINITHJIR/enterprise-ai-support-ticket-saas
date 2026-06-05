from sqlalchemy.orm import Session

from app.models.escalation_email_model import (
    EscalationEmail
)
from app.models.escalation_email_model import (
    EscalationEmail
)

from app.models.ticket_model import (
    Ticket
)

from app.models.complaint_model import (
    Complaint
)

class EscalationEmailRepository:

    @staticmethod
    def create(
            db: Session,
            ticket_id: int,
            email_content: str
    ):

        email = EscalationEmail(
            ticket_id=ticket_id,
            email_content=email_content
        )

        db.add(email)

        db.commit()

        db.refresh(email)

        return email
    
    @staticmethod
    def get_user_emails(
            db,
            user_id
    ):

        return (

            db.query(
                EscalationEmail
            )

            .join(
                Ticket,
                Ticket.id ==
                EscalationEmail.ticket_id
            )

            .join(
                Complaint,
                Complaint.id ==
                Ticket.complaint_id
            )

            .filter(
                Complaint.user_id ==
                user_id
            )

            .all()
        )