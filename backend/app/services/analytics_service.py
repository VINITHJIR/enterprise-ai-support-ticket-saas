from sqlalchemy.orm import Session

from app.repositories.analytics_repository import (
    AnalyticsRepository
)


class AnalyticsService:

    @staticmethod
    def get_summary(
        db: Session
    ):

        return {

            "total_complaints":
            AnalyticsRepository.total_complaints(
                db
            ),

            "total_tickets":
            AnalyticsRepository.total_tickets(
                db
            ),

            "total_escalations":
            AnalyticsRepository.total_escalations(
                db
            ),

            "invoice_complaints":
            AnalyticsRepository.invoice_complaints(
                db
            )
        }