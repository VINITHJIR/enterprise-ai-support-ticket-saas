from app.services.followup_llm_service import (
    FollowupLLMService
)

print(
    FollowupLLMService.detect_action(
        "Everything is fixed now"
    )
)

print(
    FollowupLLMService.detect_action(
        "Still facing the issue"
    )
)

print(
    FollowupLLMService.detect_action(
        "What is the latest update?"
    )
)

print(
    FollowupLLMService.detect_action(
        "Hello"
    )
)