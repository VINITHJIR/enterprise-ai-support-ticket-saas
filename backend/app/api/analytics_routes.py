from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.dependencies.auth_dependency import (
    get_current_user
)

from app.models.user_model import User

from app.tools.analytics_tool import (
    analytics_tool
)

router = APIRouter(
    prefix="/api/analytics",
    tags=["Analytics"]
)


@router.get("/")
def dashboard_metrics(
        db: Session = Depends(get_db),
        current_user: User = Depends(
            get_current_user
        )
):

    result = analytics_tool(
        db=db,
        user_id=current_user.id
    )

    return result