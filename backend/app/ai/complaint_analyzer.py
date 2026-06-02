import json

from langchain_core.messages import HumanMessage

from app.ai.openai_client import llm


def analyze_message(message: str):

    prompt = f"""
You are an enterprise support complaint classifier.

Categories:

1. INVOICE
   - invoice
   - billing
   - payment
   - refund

2. HR_RECRUITMENT
   - recruiter
   - interview
   - offer letter
   - recruitment
   - hiring

3. GOOGLE_REVIEW
   - google review
   - business review
   - rating

Return JSON only:

{{
    "is_complaint": true,
    "category": "HR_RECRUITMENT",
    "priority": "HIGH"
}}

User Message:

{message}
"""

    response = llm.invoke(
        [
            HumanMessage(content=prompt)
        ]
    )

    return json.loads(
        response.content
    )