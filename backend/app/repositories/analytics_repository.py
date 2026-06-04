from sqlalchemy.orm import Session

from app.models.complaint_model import Complaint
from app.models.ticket_model import Ticket
from app.models.escalation_email_model import (
    EscalationEmail
)

from app.enums.complaint_enum import (
    ComplaintCategory
)


class AnalyticsRepository:

    @staticmethod
    def total_complaints(
        db: Session
    ):

        return (
            db.query(Complaint)
            .count()
        )

    @staticmethod
    def total_tickets(
        db: Session
    ):

        return (
            db.query(Ticket)
            .count()
        )

    @staticmethod
    def total_escalations(
        db: Session
    ):

        return (
            db.query(
                EscalationEmail
            )
            .count()
        )

    @staticmethod
    def invoice_complaints(
        db: Session
    ):

        return (
            db.query(Complaint)
            .filter(
                Complaint.category ==
                ComplaintCategory.INVOICE
            )
            .count()
        )