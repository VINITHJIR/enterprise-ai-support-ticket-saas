from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.dependencies.auth_dependency import (
    get_current_user
)   

from app.models.user_model import User

from app.services.memory_service import (
    MemoryService
)

router = APIRouter(
    prefix="/api/memory",
    tags=["Memory"]
)


@router.get("/")
def get_memory(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    history = (
        MemoryService.get_history(
            db,
            current_user.id
        )
    )

    return [
        {
            "role": item.role,
            "content": item.content
        }
        for item in history
    ]