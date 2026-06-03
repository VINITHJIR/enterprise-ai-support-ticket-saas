from app.workflows.invoice_workflow import (
    execute_invoice_workflow
)


ACTION_MAP = {

    "CREATE_INVOICE_COMPLAINT":
    execute_invoice_workflow

}


class ToolExecutor:

    @staticmethod
    def execute(
        tool_result,
        state
    ):

        action = (
            tool_result["action"]
        )

        workflow = (
            ACTION_MAP[action]
        )

        return workflow(
            state,
            tool_result
        )