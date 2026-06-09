from app.agents.followup_tool_agent import (
    executor
)

result = (
    executor.invoke(
        {
            "input":
            """
Ticket ID = 16

What is the status?
"""
        }
    )
)

print(
    result["output"]
)