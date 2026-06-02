from app.ai.response_generator import (
    generate_response
)


class ReviewAgent:

    @staticmethod
    def handle(
            message: str
    ):

        prompt = f"""
You are a Google Review Support Specialist.

Help customer regarding:

- Google Reviews
- Review removal
- Review moderation
- Business profile reviews

Customer Message:

{message}
"""

        return generate_response(
            prompt
        )