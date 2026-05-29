from sqlalchemy.orm import Session

from app.repositories.escalation_email_repository import (
    EscalationEmailRepository
)


class EscalationEmailService:

    @staticmethod
    def create_escalation_email(
            db: Session,
            ticket_id: int,
            email_content: str
    ):

        return (
            EscalationEmailRepository.create(
                db=db,
                ticket_id=ticket_id,
                email_content=email_content
            )
        )