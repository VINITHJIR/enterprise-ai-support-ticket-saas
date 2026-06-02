from app.agents.support_agent import (
    SupportAgent
)


result = (
    SupportAgent.process_message(
        "Hello, how are you?"
    )
)

print(result)