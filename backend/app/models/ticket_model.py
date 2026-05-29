from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Enum as SqlEnum

from sqlalchemy.orm import relationship

from datetime import datetime

from app.core.database import Base

from app.enums.ticket_enum import (
    TicketPriority,
    TicketStatus
)


class Ticket(Base):

    __tablename__ = "tickets"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    complaint_id = Column(
        Integer,
        ForeignKey("complaints.id"),
        unique=True,
        nullable=False
    )

    priority = Column(
        SqlEnum(TicketPriority),
        default=TicketPriority.MEDIUM,
        nullable=False
    )

    status = Column(
        SqlEnum(TicketStatus),
        default=TicketStatus.OPEN,
        nullable=False
    )

    assigned_agent = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    complaint = relationship(
        "Complaint",
        back_populates="ticket"
    )

    escalation_emails = relationship(
        "EscalationEmail",
        back_populates="ticket"
    )