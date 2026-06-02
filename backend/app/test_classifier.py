from app.ai.complaint_analyzer import (
    analyze_message
)

result = analyze_message(
    """
  Recruiter is not responding after my interview
    """
)

print(result)