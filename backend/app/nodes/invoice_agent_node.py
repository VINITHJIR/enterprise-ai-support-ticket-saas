from app.agents.tool_calling_invoice_agent import (
    ToolCallingInvoiceAgent
)


def invoice_agent_node(state):

    print(
        "TOOL CALLING INVOICE AGENT EXECUTED"
    )

    result = (
        ToolCallingInvoiceAgent.process(
            state
        )
    )

    state.update(
        result
    )

    return state