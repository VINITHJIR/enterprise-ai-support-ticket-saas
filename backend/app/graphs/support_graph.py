from langgraph.graph import (
    StateGraph,
    START,
    END
)

from app.states.support_state import (
    SupportState
)
from app.nodes.category_router_node import (
    category_router_node
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

from app.nodes.invoice_agent_node import (
    invoice_agent_node
)

from app.nodes.hr_agent_node import (
    hr_agent_node
)

from app.nodes.review_agent_node import (
    review_agent_node
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

    return "category_router"


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
# GRAPH
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
    "invoice_agent",
    invoice_agent_node
)
builder.add_node(
    "category_router",
    category_router_node
)
builder.add_node(
    "hr_agent",
    hr_agent_node
)

builder.add_node(
    "review_agent",
    review_agent_node
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
        "category_router": "category_router"
    }
)

# ----------------------------------
# CATEGORY ROUTING
# ----------------------------------

builder.add_conditional_edges(
    "category_router",
    category_router,
    {
        "invoice_agent": "invoice_agent",
        "hr_agent": "hr_agent",
        "review_agent": "review_agent",
        "response": "response"
    }
)

# ----------------------------------
# AGENT FLOWS
# ----------------------------------

builder.add_edge(
    "invoice_agent",
    "create_complaint"
)

builder.add_edge(
    "hr_agent",
    "create_complaint"
)

builder.add_edge(
    "review_agent",
    "create_complaint"
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
# END
# ----------------------------------

builder.add_edge(
    "response",
    END
)

support_graph = builder.compile()