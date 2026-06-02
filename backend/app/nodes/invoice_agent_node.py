from app.agents.invoice_agent import (
    InvoiceAgent
)


def invoice_agent_node(state):
    
    response = (
        InvoiceAgent.handle(
            state["message"]
        )
    )

    state["response"] = response
    print("Invoice Agent Executed")
    return state