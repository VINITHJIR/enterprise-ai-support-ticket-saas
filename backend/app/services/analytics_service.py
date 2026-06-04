from app.repositories.analytics_repository import (
    AnalyticsRepository
)


class AnalyticsService:

    @staticmethod
    def get_dashboard_metrics(db):

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
            AnalyticsRepository.complaints_by_category(
                db,
                "INVOICE"
            ),

            "hr_complaints":
            AnalyticsRepository.complaints_by_category(
                db,
                "HR_RECRUITMENT"
            ),

            "review_complaints":
            AnalyticsRepository.complaints_by_category(
                db,
                "GOOGLE_REVIEW"
            )
        }