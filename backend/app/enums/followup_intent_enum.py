from enum import Enum


class FollowupIntent(str, Enum):

    STATUS_CHECK = "STATUS_CHECK"

    CLOSE_TICKET = "CLOSE_TICKET"

    REOPEN_TICKET = "REOPEN_TICKET"

    NONE = "NONE"