class ManagerAgent:

    @staticmethod
    def route(category: str):

        if category == "INVOICE":
            return "invoice_agent"

        if category == "HR_RECRUITMENT":
            return "hr_agent"

        if category == "GOOGLE_REVIEW":
            return "review_agent"

        return "analytics_agent"