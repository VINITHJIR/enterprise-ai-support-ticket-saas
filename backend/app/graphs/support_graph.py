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

    if state["is_complaint"]:
        return "manager"

    return "response"


def manager_router(state):

    return state["selected_agent"]


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
    "manager",
    manager_node
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
        "invoice_agent": "invoice_agent",
        "hr_agent": "hr_agent",
        "review_agent": "review_agent"
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

# ----------------------------------
# END
# ----------------------------------

builder.add_edge(
    "response",
    END
)

support_graph = builder.compile()