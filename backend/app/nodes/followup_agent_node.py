from app.services.followup_llm_service import (
    FollowupLLMService
)

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


def followup_agent_node(state):

    action = (
        FollowupLLMService
        .detect_action(
            state["message"]
        )
    )

    if action == "NONE":

        state["followup_handled"] = False

        return state

    memories = (
        SemanticMemoryService
        .search_memories(
            user_id=state["user_id"],
            query=state["message"],
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

        state["followup_handled"] = False

        return state

    db = state["db"]

    # --------------------
    # STATUS
    # --------------------

    if action == "STATUS_CHECK":

        result = (
            get_ticket_status_tool(
                db,
                ticket_id
            )
        )

        state[
            "followup_response"
        ] = f"""
Ticket #{ticket_id}

Status:
{result['status']}

Priority:
{result['priority']}
"""

        state[
            "followup_handled"
        ] = True

        return state

    # --------------------
    # CLOSE
    # --------------------

    if action == "CLOSE_TICKET":

        result = (
            close_ticket_tool(
                db,
                ticket_id
            )
        )

        state[
            "followup_response"
        ] = f"""
Ticket #{ticket_id}
closed successfully.

Complaint
#{result['complaint_id']}
also closed.
"""

        state[
            "followup_handled"
        ] = True

        return state

    # --------------------
    # REOPEN
    # --------------------

    if action == "REOPEN_TICKET":

        result = (
            reopen_ticket_tool(
                db,
                ticket_id
            )
        )

        state[
            "followup_response"
        ] = f"""
Ticket #{ticket_id}
reopened successfully.

Complaint
#{result['complaint_id']}
also reopened.
"""

        state[
            "followup_handled"
        ] = True

        return state

    state["followup_handled"] = False

    return state