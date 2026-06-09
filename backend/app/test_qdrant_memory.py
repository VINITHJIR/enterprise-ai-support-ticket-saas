from app.services.qdrant_memory_service import (
    QdrantMemoryService
)

QdrantMemoryService.save_memory(

    user_id=1,

    role="user",

    content=
    "Invoice not generated"
)

print(
    "Memory Stored"
)