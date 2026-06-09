from app.services.semantic_memory_service import (
    SemanticMemoryService
)


class MemoryContextService:

    @staticmethod
    def build_context(
        user_id,
        query
    ):

        memories = (
            SemanticMemoryService
            .search_memories(
                user_id=user_id,
                query=query,
                limit=5
            )
        )

        if not memories:
            return ""

        context = []

        for memory in memories:

            content = (
                memory.get(
                    "content",
                    ""
                )
            )

            ticket_id = (
                memory.get(
                    "ticket_id"
                )
            )

            complaint_id = (
                memory.get(
                    "complaint_id"
                )
            )

            context.append(
                f"""
Memory:
Content: {content}
Ticket ID: {ticket_id}
Complaint ID: {complaint_id}
"""
            )

        return "\n".join(context)