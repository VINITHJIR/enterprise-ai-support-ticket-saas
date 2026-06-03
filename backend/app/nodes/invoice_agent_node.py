from app.agents.invoice_agent import (
    InvoiceAgent
)


def invoice_agent_node(state):

    print(
        "Invoice Agent Executed"
    )

    return InvoiceAgent.process(
        state
    )