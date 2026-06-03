from app.tools.complaint_check_tool import (
    complaint_check_tool
)

from app.tools.create_complaint_tool import (
    create_complaint_tool
)

from app.tools.create_ticket_tool import (
    create_ticket_tool
)

from app.tools.escalation_email_tool import (
    escalation_email_tool
)

from app.tools.customer_response_tool import (
    customer_response_tool
)


class InvoiceAgent:

    @staticmethod
    def process(state):

        existing = (
            complaint_check_tool.invoke(
                {
                    "user_id": state["user_id"],
                    "category": state["category"],
                    "db": state["db"]
                }
            )
        )

        # Duplicate Complaint

        if existing["exists"]:

            escalation_email_tool.invoke(
                {
                    "ticket_id": state["ticket_id"],
                    "db": state["db"]
                }
            )

            state["response"] = (
                customer_response_tool.invoke(
                    {
                        "message":
                        "Complaint already exists and has been escalated."
                    }
                )
            )

            return state

        # Create Complaint

        complaint = (
            create_complaint_tool.invoke(
                {
                    "user_id": state["user_id"],
                    "complaint_text": state["message"],
                    "category": state["category"],
                    "db": state["db"]
                }
            )
        )

        state["complaint_id"] = (
            complaint["complaint_id"]
        )

        # Create Ticket

        ticket = (
            create_ticket_tool.invoke(
                {
                    "complaint_id":
                    complaint["complaint_id"],

                    "priority":
                    state["priority"],

                    "db":
                    state["db"]
                }
            )
        )

        state["ticket_id"] = (
            ticket["ticket_id"]
        )

        # Escalation

        if state["priority"] == "HIGH":

            escalation_email_tool.invoke(
                {
                    "ticket_id":
                    ticket["ticket_id"],

                    "db":
                    state["db"]
                }
            )

        state["response"] = (
            customer_response_tool.invoke(
                {
                    "message":
                    state["message"]
                }
            )
        )

        return state