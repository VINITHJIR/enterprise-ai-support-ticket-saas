from langchain.agents import (
    create_tool_calling_agent,
    AgentExecutor
)

from langchain_core.prompts import (
    ChatPromptTemplate
)

from app.ai.openai_client import (
    llm
)

from app.langchain_tools.ticket_tools import (
    ticket_status_tool,
    close_ticket_agent_tool,
    reopen_ticket_agent_tool
)


tools = [

    ticket_status_tool,

    close_ticket_agent_tool,

    reopen_ticket_agent_tool

]


prompt = (
    ChatPromptTemplate
    .from_messages(
        [
            (
                "system",
                """
You are a support follow-up agent.

Use available tools whenever needed.

Never guess ticket status.

Always use tools.
"""
            ),
            (
                "human",
                "{input}"
            ),
            (
                "placeholder",
                "{agent_scratchpad}"
            )
        ]
    )
)


agent = (
    create_tool_calling_agent(
        llm,
        tools,
        prompt
    )
)


executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)