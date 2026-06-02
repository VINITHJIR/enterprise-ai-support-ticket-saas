from app.tools.complaint_analysis_tool import (
    complaint_analysis_tool
)


class SupportAgent:

    @staticmethod
    def process_message(
            message: str
    ):

        analysis = complaint_analysis_tool.invoke(
            {
                "message": message
            }
        )

        return {
            "analysis": analysis
        }