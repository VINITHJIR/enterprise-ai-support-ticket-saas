from app.models.conversation_memory_model import (
    ConversationMemory
)


class MemoryService:

    @staticmethod
    def save_message(
        db,
        user_id,
        role,
        content
    ):
        memory = ConversationMemory(
            user_id=user_id,
            role=role,
            content=content
        )

        db.add(memory)
        db.commit()

        return memory

    @staticmethod
    def save(
        db,
        user_id,
        role,
        content
    ):
        return MemoryService.save_message(
            db,
            user_id,
            role,
            content
        )

    @staticmethod
    def get_history(
        db,
        user_id
    ):
        return (
            db.query(
                ConversationMemory
            )
            .filter(
                ConversationMemory.user_id
                == user_id
            )
            .order_by(
                ConversationMemory.id.asc()
            )
            .all()
        )