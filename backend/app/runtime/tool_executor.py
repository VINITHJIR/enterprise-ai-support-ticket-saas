from app.workflows.invoice_workflow import (
    execute_invoice_workflow
)

from app.workflows.hr_workflow import (
    execute_hr_workflow
)

from app.workflows.review_workflow import (
    execute_review_workflow
)
ACTION_MAP = {

    "CREATE_INVOICE_COMPLAINT":
    execute_invoice_workflow,

    "CREATE_HR_COMPLAINT":
    execute_hr_workflow,

    "CREATE_REVIEW_COMPLAINT":
    execute_review_workflow
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