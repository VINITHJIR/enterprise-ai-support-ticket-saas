from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base
class EscalationEmail(Base):

    __tablename__ = "escalation_emails"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    ticket_id = Column(
        Integer,
        ForeignKey("tickets.id"),
        nullable=False
    )

    email_content = Column(
        Text,
        nullable=False
    )

    sent_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    ticket = relationship(
        "Ticket",
        back_populates="escalation_emails"
    )