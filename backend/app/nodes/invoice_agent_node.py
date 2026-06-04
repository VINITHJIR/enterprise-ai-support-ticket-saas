from app.agents.autonomous_invoice_agent import (
    AutonomousInvoiceAgent
)

def invoice_agent_node(state):

    state["response"] = (
        AutonomousInvoiceAgent.process(
            state
        )
    )

    return state