from qdrant_client import (
    QdrantClient
)

from qdrant_client.models import (
    Distance,
    VectorParams
)


class QdrantService:

    COLLECTION_NAME = (
        "support_memory"
    )

    client = QdrantClient(
        host="localhost",
        port=6333
    )

    @classmethod
    def create_collection(cls):

        collections = (
            cls.client
            .get_collections()
        )

        collection_names = [

            c.name

            for c in
            collections.collections
        ]

        if (
            cls.COLLECTION_NAME
            not in collection_names
        ):

            cls.client.create_collection(

                collection_name=
                cls.COLLECTION_NAME,

                vectors_config=
                VectorParams(
                    size=1536,
                    distance=
                    Distance.COSINE
                )
            )

            print(
                f"{cls.COLLECTION_NAME}"
                " created"
            )

        else:

            print(
                f"{cls.COLLECTION_NAME}"
                " already exists"
            )