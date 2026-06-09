from openai import OpenAI

from app.core.config import settings


class EmbeddingService:

    client = OpenAI(
        api_key=settings.OPENAI_API_KEY
    )

    @classmethod
    def generate_embedding(
        cls,
        text: str
    ):

        response = (
            cls.client.embeddings.create(
                model=
                "text-embedding-3-small",

                input=text
            )
        )

        return (
            response
            .data[0]
            .embedding
        )