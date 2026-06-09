from uuid import uuid4

from qdrant_client.models import (
    PointStruct
)

from app.services.qdrant_service import (
    QdrantService
)

from app.services.embedding_service import (
    EmbeddingService
)


class QdrantMemoryService:

    @staticmethod
    def save_memory(
        user_id,
        role,
        content,
        ticket_id=None,
        complaint_id=None
    ):

        vector = (
            EmbeddingService
            .generate_embedding(
                content
            )
        )

        point = PointStruct(

            id=str(
                uuid4()
            ),

            vector=vector,

            payload={

                "user_id":
                user_id,

                "role":
                role,

                "content":
                content,

                "ticket_id":
                ticket_id,

                "complaint_id":
                complaint_id
            }
        )

        (
            QdrantService.client
            .upsert(
                collection_name=
                QdrantService.COLLECTION_NAME,

                points=[
                    point
                ]
            )
        )

        return True