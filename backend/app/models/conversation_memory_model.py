from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime

from datetime import datetime

from app.core.database import Base


class ConversationMemory(Base):

    __tablename__ = "conversation_memory"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    role = Column(
        Text
    )

    content = Column(
        Text
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )