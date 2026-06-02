from app.graphs.support_graph import (
    support_graph
)

result = support_graph.invoke(
    {
        "message":
            "Invoice payment not reflected",
        "user_id": 1
    }
)

print(result)