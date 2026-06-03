from sqlalchemy.orm import Session

from app.repositories.ticket_repository import (
    TicketRepository
)

from app.enums.ticket_enum import (
    TicketPriority
)


class TicketService:

    @staticmethod
    def create_ticket(
            db: Session,
            complaint_id: int,
            priority
    ):

        return TicketRepository.create(
            db=db,
            complaint_id=complaint_id,
            priority=priority
        )

    @staticmethod
    def get_ticket_by_complaint(
            db: Session,
            complaint_id: int
    ):

        return (
            TicketRepository.get_by_complaint_id(
                db,
                complaint_id
            )
        )

    @staticmethod
    def increase_priority(
            db: Session,
            ticket,
            target_priority: str
    ):

        priority_mapping = {
            "LOW": TicketPriority.LOW,
            "MEDIUM": TicketPriority.MEDIUM,
            "HIGH": TicketPriority.HIGH
        }

        return TicketRepository.update_priority(
            db,
            ticket,
            priority_mapping[target_priority]
        )

    @staticmethod
    def get_user_tickets(
            db: Session,
            user_id: int
    ):

        return TicketRepository.get_all_by_user(
            db,
            user_id
        )