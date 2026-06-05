from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.dependencies.auth_dependency import (
    get_current_user
)

from app.models.user_model import User

from app.services.escalation_email_service import (
    EscalationEmailService
)

router = APIRouter(
    prefix="/api/emails",
    tags=["Escalation Emails"]
)


@router.get("/")
def get_emails(
        db: Session = Depends(get_db),
        current_user: User = Depends(
            get_current_user
        )
):

    return (
        EscalationEmailService
        .get_user_emails(
            db,
            current_user.id
        )
    )