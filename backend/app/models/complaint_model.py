from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Enum as SqlEnum
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from datetime import datetime

from app.core.database import Base

from app.enums.complaint_enum import (
    ComplaintCategory,
    ComplaintStatus
)


class Complaint(Base):

    __tablename__ = "complaints"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    complaint = Column(
        Text,
        nullable=False
    )

    category = Column(
        SqlEnum(ComplaintCategory),
        nullable=False
    )

    status = Column(
        SqlEnum(ComplaintStatus),
        default=ComplaintStatus.OPEN,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="complaints"
    )

    ticket = relationship(
        "Ticket",
        back_populates="complaint",
        uselist=False
    )