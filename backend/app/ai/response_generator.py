from langchain_core.messages import HumanMessage

from app.ai.openai_client import llm


def generate_response(message: str):

    prompt = f"""
You are a helpful customer support assistant.

Reply professionally.

User Message:

{message}
"""

    response = llm.invoke(
        [
            HumanMessage(content=prompt)
        ]
    )

    return response.content