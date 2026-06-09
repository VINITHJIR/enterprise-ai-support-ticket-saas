from app.ai.openai_client import (
    llm
)


class FollowupLLMService:

    @staticmethod
    def detect_action(
        message
    ):

        prompt = f"""
You are a support ticket follow-up classifier.

Possible actions:

STATUS_CHECK
CLOSE_TICKET
REOPEN_TICKET
NONE

Examples:

User:
What is the status of my issue?

Output:
STATUS_CHECK

User:
Can you give me an update?

Output:
STATUS_CHECK

User:
Everything is fixed now.

Output:
CLOSE_TICKET

User:
The problem is solved.

Output:
CLOSE_TICKET

User:
Still facing the issue.

Output:
REOPEN_TICKET

User:
Issue happened again.

Output:
REOPEN_TICKET

User:
Hello

Output:
NONE

Classify this message.

User:

{message}

Return ONLY one action.
"""

        response = (
            llm.invoke(
                prompt
            )
        )

        return (
            response.content
            .strip()
            .upper()
        )