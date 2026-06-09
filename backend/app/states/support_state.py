from typing import TypedDict
from typing import Optional


class SupportState(TypedDict):

    message: str

    user_id: int

    db: object

    is_complaint: bool

    category: Optional[str]

    priority: Optional[str]

    complaint_exists: bool

    complaint_id: Optional[int]

    ticket_id: Optional[int]

    response: Optional[str]

    selected_agent: Optional[str]

    followup_handled: bool

    followup_response: Optional[str]

    memory_context: str