from app.ai.response_generator import (
    generate_response
)


def response_node(state):

    state["response"] = generate_response(
        state["message"]
    )

    return state