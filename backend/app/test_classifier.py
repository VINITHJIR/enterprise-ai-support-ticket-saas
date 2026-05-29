from app.ai.complaint_analyzer import (
    analyze_message
)

result = analyze_message(
    """
    I attended interview
    4 months ago and still
    no update received.
    """
)

print(result)