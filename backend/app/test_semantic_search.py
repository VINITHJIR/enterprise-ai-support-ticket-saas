from app.services.semantic_memory_service import (
    SemanticMemoryService
)

results = (
    SemanticMemoryService
    .search_memories(
        user_id=1,
        query="billing issue"
    )
)

print(
    f"Found {len(results)} memories"
)

for item in results:

    print(
        item.get("content")
    )

    print(
        item.get("ticket_id")
    )

    print(
        "-------------"
    )