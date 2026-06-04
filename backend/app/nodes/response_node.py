from app.ai.response_generator import (
    generate_response
)


def response_node(state):

    # Response already exists
    if state.get("response"):

        return state

    # Fallback response generation

    from app.ai.response_generator import (
        generate_response
    )

    state["response"] = (
        generate_response(
            state["message"]
        )
    )

    return state