from langgraph.graph import (
    StateGraph,
    START,
    END
)
from app.nodes.followup_agent_node import (
    followup_agent_node
)
from app.nodes.memory_node import (memory_node)
from app.states.support_state import (
    SupportState
)
from app.nodes.analytics_agent_node import (
    analytics_agent_node
)
from app.nodes.analyze_node import (
    analyze_node
)

from app.nodes.manager_node import (
    manager_node
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

    category = state["category"]

    if category == "ANALYTICS":
        return "manager"

    if state["is_complaint"]:
        return "manager"

    return "response"

def manager_router(state):

    return state["selected_agent"]

def followup_router(state):

    if state.get(
        "followup_handled"
    ):
        return "response"

    return "analyze"
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
    "followup_agent",
    followup_agent_node
)
builder.add_node(
    "manager",
    manager_node
)
builder.add_node(
    "analytics_agent",
    analytics_agent_node
)
builder.add_node(
    "invoice_agent",
    invoice_agent_node
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
    "response",
    response_node
)

builder.add_node(
    "memory",
    memory_node
)

# ----------------------------------
# START
# ----------------------------------

builder.add_edge(
    START,
    "memory"
)

builder.add_edge(
    "memory",
    "followup_agent"
)

# ----------------------------------
# ANALYZE ROUTING
# ----------------------------------
builder.add_conditional_edges(
    "followup_agent",
    followup_router,
    {
        "response": "response",
        "analyze": "analyze"
    }
)
builder.add_conditional_edges(
    "analyze",
    complaint_router,
    {
        "manager": "manager",
        "response": "response"
    }
)

# ----------------------------------
# MANAGER ROUTING
# ----------------------------------

builder.add_conditional_edges(
    "manager",
    manager_router,
    {
        "invoice_agent":
        "invoice_agent",

        "hr_agent":
        "hr_agent",

        "review_agent":
        "review_agent",

        "analytics_agent":
        "analytics_agent"
    }
)

# ----------------------------------
# AGENT -> RESPONSE
# ----------------------------------

builder.add_edge(
    "invoice_agent",
    "response"
)

builder.add_edge(
    "hr_agent",
    "response"
)

builder.add_edge(
    "review_agent",
    "response"
)
builder.add_edge(
    "analytics_agent",
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