import json

from langchain_core.messages import HumanMessage

from app.ai.openai_client import llm


def analyze_message(message: str):

    prompt = f"""
You are an Enterprise Support Ticket AI.

Analyze the user message.

Categories:
- INVOICE
- HR_RECRUITMENT
- GOOGLE_REVIEW

Priority:
- LOW
- MEDIUM
- HIGH

Rules:

If message is normal conversation:

Return:

{{
    "is_complaint": false,
    "category": null,
    "priority": null
}}

If complaint:

Return:

{{
    "is_complaint": true,
    "category": "INVOICE",
    "priority": "HIGH"
}}

Return JSON only.

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