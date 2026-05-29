from sqlalchemy.orm import Session

from app.models.complaint_model import Complaint
from app.enums.complaint_enum import ComplaintStatus

class ComplaintRepository:

    @staticmethod
    def create(
            db: Session,
            user_id: int,
            complaint: str,
            category
    ):

        complaint_obj = Complaint(
            user_id=user_id,
            complaint=complaint,
            category=category
        )

        db.add(complaint_obj)

        db.commit()

        db.refresh(complaint_obj)

        return complaint_obj

    @staticmethod
    def find_existing_active_complaint(
        db: Session,
        user_id: int,
        category
    ):

        return (
            db.query(Complaint)
            .filter(
                Complaint.user_id == user_id,
                Complaint.category == category,
                Complaint.status.in_([
                    ComplaintStatus.OPEN,
                    ComplaintStatus.IN_PROGRESS
                ])
            )
            .first()
        )

    @staticmethod
    def get_by_user(
            db: Session,
            user_id: int
    ):

        return (
            db.query(Complaint)
            .filter(
                Complaint.user_id == user_id
            )
            .all()
        )
    @staticmethod
    def get_by_id(
            db: Session,
            complaint_id: int
    ):

        return (
            db.query(Complaint)
            .filter(
                Complaint.id == complaint_id
            )
            .first()
        )