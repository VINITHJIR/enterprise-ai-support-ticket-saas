from app.services.embedding_service import (
    EmbeddingService
)

from app.services.qdrant_service import (
    QdrantService
)

from qdrant_client.models import (
    Filter,
    FieldCondition,
    MatchValue
)


class SemanticMemoryService:

    @staticmethod
    def search_memories(
        user_id,
        query,
        limit=5
    ):

        vector = (
            EmbeddingService
            .generate_embedding(
                query
            )
        )

        results = (
            QdrantService.client.query_points(

                collection_name=
                QdrantService.COLLECTION_NAME,

                query=
                vector,

                limit=limit,

                query_filter=
                Filter(
                    must=[
                        FieldCondition(
                            key="user_id",
                            match=
                            MatchValue(
                                value=user_id
                            )
                        )
                    ]
                )
            )
        )

        return [

            point.payload

            for point in results.points

        ]