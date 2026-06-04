from app.workflows.base_complaint_workflow import (
    execute_complaint_workflow
)


def execute_hr_workflow(
    state,
    tool_result
):

    return execute_complaint_workflow(
        state,
        tool_result
    )