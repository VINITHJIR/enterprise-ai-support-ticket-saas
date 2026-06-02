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

from app.nodes.complaint_check_node import (
    complaint_check_node
)

from app.nodes.create_complaint_node import (
    create_complaint_node
)

from app.nodes.create_ticket_node import (
    create_ticket_node
)

from app.nodes.escalation_node import (
    escalation_node
)

from app.nodes.response_node import (
    response_node
)

builder = StateGraph(
    SupportState
)

builder.add_node(
    "analyze",
    analyze_node
)

builder.add_node(
    "check_complaint",
    complaint_check_node
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
    "escalation",
    escalation_node
)

builder.add_node(
    "response",
    response_node
)

builder.add_edge(
    START,
    "analyze"
)

builder.add_edge(
    "analyze",
    "check_complaint"
)

builder.add_edge(
    "check_complaint",
    "create_complaint"
)

builder.add_edge(
    "create_complaint",
    "create_ticket"
)

builder.add_edge(
    "create_ticket",
    "escalation"
)

builder.add_edge(
    "escalation",
    "response"
)

builder.add_edge(
    "response",
    END
)

support_graph = builder.compile()