from app.ai.response_generator import (
    generate_response
)


class HRAgent:

    @staticmethod
    def handle(
            message: str
    ):

        prompt = f"""
You are an HR Recruitment Support Specialist.

Help customer regarding:

- Recruitment process
- Interview status
- Offer letters
- HR communication

Customer Message:

{message}
"""

        return generate_response(
            prompt
        )