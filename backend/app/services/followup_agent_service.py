from app.services.semantic_memory_service import (
    SemanticMemoryService
)

from app.tools.get_ticket_status_tool import (
    get_ticket_status_tool
)

from app.tools.close_ticket_tool import (
    close_ticket_tool
)

from app.tools.reopen_ticket_tool import (
    reopen_ticket_tool
)

from app.enums.followup_intent_enum import (
    FollowupIntent
)


class FollowupAgentService:

    @staticmethod
    def handle(
        db,
        user_id,
        intent,
        message
    ):

        memories = (
            SemanticMemoryService
            .search_memories(
                user_id=user_id,
                query=message,
                limit=5
            )
        )

        ticket_id = None

        for memory in memories:

            if memory.get("ticket_id"):

                ticket_id = (
                    memory.get(
                        "ticket_id"
                    )
                )

                break

        if not ticket_id:

            return {
                "handled": False
            }

        # STATUS

        if (
            intent ==
            FollowupIntent.STATUS_CHECK
        ):

            result = (
                get_ticket_status_tool(
                    db,
                    ticket_id
                )
            )

            return {
                "handled": True,
                "response":
                f"""
Ticket #{ticket_id}

Status:
{result['status']}

Priority:
{result['priority']}
"""
            }

        # CLOSE

        if (
            intent ==
            FollowupIntent.CLOSE_TICKET
        ):

            result = (
                close_ticket_tool(
                    db,
                    ticket_id
                )
            )

            return {
                "handled": True,
                "response":
                f"""
Ticket #{ticket_id}
closed successfully.

Complaint
#{result['complaint_id']}
also closed.
"""
            }

        # REOPEN

        if (
            intent ==
            FollowupIntent.REOPEN_TICKET
        ):

            result = (
                reopen_ticket_tool(
                    db,
                    ticket_id
                )
            )

            return {
                "handled": True,
                "response":
                f"""
Ticket #{ticket_id}
reopened successfully.

Complaint
#{result['complaint_id']}
also reopened.
"""
            }

        return {
            "handled": False
        }