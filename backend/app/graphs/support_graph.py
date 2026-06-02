from langgraph.graph import (
    StateGraph,
    START,
    END
)

from app.states.support_state import (
    SupportState
)

from app.nodes.analyze_node import (
    analyze_node
)

from app.nodes.check_existing_node import (
    check_existing_node
)

from app.nodes.create_complaint_node import (
    create_complaint_node
)

from app.nodes.create_ticket_node import (
    create_ticket_node
)

from app.nodes.increase_priority_node import (
    increase_priority_node
)

from app.nodes.escalation_node import (
    escalation_node
)

from app.nodes.response_node import (
    response_node
)


# ----------------------------------
# ROUTERS
# ----------------------------------

def complaint_router(state):

    if state["is_complaint"]:
        return "check_existing"

    return "response"


def existing_router(state):

    if state["complaint_exists"]:
        return "increase_priority"

    return "create_complaint"

def category_router(state):

    category = state["category"]

    if category == "INVOICE":
        return "invoice_agent"

    if category == "HR_RECRUITMENT":
        return "hr_agent"

    if category == "GOOGLE_REVIEW":
        return "review_agent"

    return "response"

# ----------------------------------
# GRAPH BUILDER
# ----------------------------------

builder = StateGraph(
    SupportState
)

# ----------------------------------
# NODES
# ----------------------------------

builder.add_node(
    "analyze",
    analyze_node
)

builder.add_node(
    "check_existing",
    check_existing_node
)

builder.add_node(
    "create_complaint",
    create_complaint_node
)

builder.add_node(
    "create_ticket",
    create_ticket_node
)

builder.add_node(
    "increase_priority",
    increase_priority_node
)

builder.add_node(
    "escalation",
    escalation_node
)

builder.add_node(
    "response",
    response_node
)

# ----------------------------------
# START
# ----------------------------------

builder.add_edge(
    START,
    "analyze"
)

# ----------------------------------
# ANALYZE ROUTING
# ----------------------------------

builder.add_conditional_edges(
    "analyze",
    complaint_router,
    {
        "check_existing": "check_existing",
        "response": "response"
    }
)

# ----------------------------------
# EXISTING COMPLAINT ROUTING
# ----------------------------------

builder.add_conditional_edges(
    "check_existing",
    existing_router,
    {
        "increase_priority": "increase_priority",
        "create_complaint": "create_complaint"
    }
)

# ----------------------------------
# DUPLICATE FLOW
# ----------------------------------

builder.add_edge(
    "increase_priority",
    "escalation"
)

builder.add_edge(
    "escalation",
    "response"
)

# ----------------------------------
# NEW COMPLAINT FLOW
# ----------------------------------

builder.add_edge(
    "create_complaint",
    "create_ticket"
)

builder.add_edge(
    "create_ticket",
    "response"
)

# ----------------------------------
# END
# ----------------------------------

builder.add_edge(
    "response",
    END
)

support_graph = builder.compile()