from sqlalchemy.orm import Session

from app.repositories.complaint_repository import (
    ComplaintRepository
)


class ComplaintService:

    @staticmethod
    def check_existing_complaint(
            db: Session,
            user_id: int,
            category
    ):

        return (
            ComplaintRepository.find_existing_active_complaint(
                db=db,
                user_id=user_id,
                category=category
            )
        )

    @staticmethod
    def create_complaint(
            db: Session,
            user_id: int,
            complaint_text: str,
            category
    ):

        return ComplaintRepository.create(
            db=db,
            user_id=user_id,
            complaint=complaint_text,
            category=category
        )

    @staticmethod
    def get_user_complaints(
            db: Session,
            user_id: int
    ):

        return ComplaintRepository.get_by_user(
            db,
            user_id
        )