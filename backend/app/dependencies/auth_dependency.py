from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.core.jwt import verify_token

from app.repositories.user_repository import UserRepository

security = HTTPBearer()

def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        db: Session = Depends(get_db)
):

    token = credentials.credentials

    payload = verify_token(token)

    if not payload:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user_id = payload.get("sub")

    if not user_id:

        raise HTTPException(
            status_code=401,
            detail="Invalid token payload"
        )

    user = UserRepository.get_by_id(
        db,
        int(user_id)
    )

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user