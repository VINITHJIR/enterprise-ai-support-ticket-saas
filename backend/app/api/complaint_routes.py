from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.dependencies.auth_dependency import (
    get_current_user
)

from app.models.user_model import User

from app.schemas.complaint_schema import (
    CreateComplaintRequest , ComplaintProcessResponse
)

from app.services.complaint_service import (
    ComplaintService
)

router = APIRouter(
    prefix="/api/complaints",
    tags=["Complaints"]
)


@router.post("/" , response_model=ComplaintProcessResponse)
def create_complaint(
        request: CreateComplaintRequest,
        db: Session = Depends(get_db),
        current_user: User = Depends(
            get_current_user
        )
):

    return (
        ComplaintService.create_or_process_complaint(
            db=db,
            user_id=current_user.id,
            complaint_text=request.complaint,
            category=request.category
        )
    )


@router.get("/")
def get_complaints(
        db: Session = Depends(get_db),
        current_user: User = Depends(
            get_current_user
        )
):

    return (
        ComplaintService.get_user_complaints(
            db,
            current_user.id
        )
    )