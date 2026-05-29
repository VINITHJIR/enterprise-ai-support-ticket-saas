from sqlalchemy.orm import Session

from app.models.escalation_email_model import (
    EscalationEmail
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