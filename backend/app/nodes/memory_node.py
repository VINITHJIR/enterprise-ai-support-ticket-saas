from app.services.memory_context_service import (
    MemoryContextService
)


def memory_node(state):

    context = (
        MemoryContextService
        .build_context(
            user_id=state["user_id"],
            query=state["message"]
        )
    )

    state["memory_context"] = context

    print(
        "\n========== MEMORY CONTEXT =========="
    )

    print(context)

    print(
        "====================================\n"
    )

    return state