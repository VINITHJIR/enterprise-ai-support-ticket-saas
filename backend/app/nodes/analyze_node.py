from app.ai.complaint_analyzer import (
    analyze_message
)


def analyze_node(state):

    result = analyze_message(
        state["message"]
    )
    print("ANALYSIS =", result)
    state["is_complaint"] = result["is_complaint"]
    state["category"] = result["category"]
    state["priority"] = result["priority"]
    print("STATE CATEGORY =", state["category"])
    return state