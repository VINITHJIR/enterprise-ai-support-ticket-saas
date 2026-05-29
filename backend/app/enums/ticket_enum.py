from enum import Enum


class TicketPriority(str, Enum):

    LOW = "LOW"

    MEDIUM = "MEDIUM"

    HIGH = "HIGH"


class TicketStatus(str, Enum):

    OPEN = "OPEN"

    IN_PROGRESS = "IN_PROGRESS"

    RESOLVED = "RESOLVED"

    CLOSED = "CLOSED"