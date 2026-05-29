from enum import Enum


class ComplaintCategory(str, Enum):

    INVOICE = "INVOICE"

    HR_RECRUITMENT = "HR_RECRUITMENT"

    GOOGLE_REVIEW = "GOOGLE_REVIEW"


class ComplaintStatus(str, Enum):

    OPEN = "OPEN"

    IN_PROGRESS = "IN_PROGRESS"

    RESOLVED = "RESOLVED"

    CLOSED = "CLOSED"