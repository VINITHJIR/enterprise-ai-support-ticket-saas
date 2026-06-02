from app.ai.response_generator import (
    generate_response
)


class InvoiceAgent:

    @staticmethod
    def handle(
            message: str
    ):

        prompt = f"""
You are a Billing and Invoice Support Specialist.

Help customer regarding:

- Invoice issues
- Payment issues
- Refund issues
- Subscription billing issues

Customer Message:

{message}
"""

        return generate_response(
            prompt
        )