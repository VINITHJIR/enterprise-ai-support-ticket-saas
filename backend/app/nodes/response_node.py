from app.ai.response_generator import (
    generate_response
)


def response_node(state):

    # -------------------------
    # FOLLOW-UP RESPONSE
    # -------------------------

    if state.get(
        "followup_handled"
    ):

        state["response"] = (
            state.get(
                "followup_response",
                "Request processed."
            )
        )

        return state

    # -------------------------
    # MEMORY CONTEXT
    # -------------------------

    memory_context = (
        state.get(
            "memory_context",
            ""
        )
    )

    # Debug

    if memory_context:

        print(
            "\n========== MEMORY USED =========="
        )

        print(
            memory_context
        )

        print(
            "=================================\n"
        )

    # -------------------------
    # AGENT RESPONSE ALREADY EXISTS
    # -------------------------

    if state.get(
        "response"
    ):

        return state

    # -------------------------
    # FALLBACK RESPONSE
    # -------------------------

    prompt = f"""
Previous Related Memories:

{memory_context}

Current User Message:

{state["message"]}

Instructions:

- Use previous memories if relevant.
- Do not display raw memory data.
- Do not display internal ticket references unless useful.
- Give a natural customer-facing response.
"""

    state["response"] = (
        generate_response(
            prompt
        )
    )

    return state