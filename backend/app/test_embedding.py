from app.services.embedding_service import (
    EmbeddingService
)

vector = (
    EmbeddingService
    .generate_embedding(
        "Invoice not generated"
    )
)

print(
    len(vector)
)

print(
    vector[:5]
)