from sqlalchemy.orm import Session

from app.models.ticket_model import Ticket

from app.enums.ticket_enum import (
    TicketPriority
)
from app.models.complaint_model import Complaint

class TicketRepository:

    @staticmethod
    def create(
            db: Session,
            complaint_id: int,
            priority: TicketPriority
    ):

        ticket = Ticket(
            complaint_id=complaint_id,
            priority=priority
        )

        db.add(ticket)

        db.commit()

        db.refresh(ticket)

        return ticket

    @staticmethod
    def get_by_complaint_id(
            db: Session,
            complaint_id: int
    ):

        return (
            db.query(Ticket)
            .filter(
                Ticket.complaint_id == complaint_id
            )
            .first()
        )

    @staticmethod
    def update_priority(
            db: Session,
            ticket: Ticket,
            priority
    ):

        ticket.priority = priority

        db.commit()

        db.refresh(ticket)

        return ticket
    
    @staticmethod
    def get_all_by_user(
            db: Session,
            user_id: int
    ):

        return (
            db.query(Ticket)
            .join(Ticket.complaint)
            .filter(
                Complaint.user_id == user_id
            )
            .all()
        )