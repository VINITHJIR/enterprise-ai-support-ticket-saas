from app.core.database import (
    SessionLocal
)

from app.services.memory_service import (
    MemoryService
)

db = SessionLocal()

memories = (
    MemoryService.get_recent_memories(
        db,
        user_id=1
    )
)

for m in memories:

    print(m.message)

    print(m.response)

    print("------")