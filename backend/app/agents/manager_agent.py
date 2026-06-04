class ManagerAgent:

    @staticmethod
    def route(
        category
    ):

        mapping = {

            "INVOICE":
            "invoice_agent",

            "HR_RECRUITMENT":
            "hr_agent",

            "GOOGLE_REVIEW":
            "review_agent",

            "ANALYTICS":
            "analytics_agent"
        }

        return mapping.get(
            category,
            "response"
        )