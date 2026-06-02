from langchain_core.prompts import ChatPromptTemplate


support_agent_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI Support Agent.

Rules:

1. First analyze the customer message.
2. Use complaint_analysis_tool.
3. If it is normal chat:
   use customer_response_tool.
4. If it is a complaint:
   return complaint details.

Always use available tools.
"""
        ),
        ("human", "{input}")
    ]
)