from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.dependencies.auth_dependency import (
    get_current_user
)

from app.models.user_model import User

from app.services.ticket_service import (
    TicketService
)

router = APIRouter(
    prefix="/api/tickets",
    tags=["Tickets"]
)


@router.get("/")
def get_tickets(
        db: Session = Depends(get_db),
        current_user: User = Depends(
            get_current_user
        )
):

    return (
        TicketService.get_user_tickets(
            db,
            current_user.id
        )
    )


@router.get("/{complaint_id}")
def get_ticket(
        complaint_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(
            get_current_user
        )
):

    return (
        TicketService.get_ticket(
            db,
            complaint_id
        )
    )