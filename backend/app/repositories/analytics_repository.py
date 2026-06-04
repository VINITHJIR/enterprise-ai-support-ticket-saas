from app.models.complaint_model import Complaint
from app.models.ticket_model import Ticket
from app.models.escalation_email_model import EscalationEmail


class AnalyticsRepository:

    @staticmethod
    def total_complaints(db):

        return (
            db.query(Complaint)
            .count()
        )

    @staticmethod
    def total_tickets(db):

        return (
            db.query(Ticket)
            .count()
        )

    @staticmethod
    def total_escalations(db):

        return (
            db.query(EscalationEmail)
            .count()
        )

    @staticmethod
    def complaints_by_category(
        db,
        category
    ):

        return (
            db.query(Complaint)
            .filter(
                Complaint.category == category
            )
            .count()
        )