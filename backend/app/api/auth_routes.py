from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.auth_schema import (RegisterRequest,LoginRequest)
from app.services.auth_service import (AuthService)
from app.dependencies.auth_dependency import (get_current_user)
from app.models.user_model import User
router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
        request: RegisterRequest,
        db: Session = Depends(get_db)
):

    try:

        user = AuthService.register(
            db,
            request.name,
            request.email,
            request.password
        )

        return {
            "message": "User registered",
            "user_id": user.id
        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    
@router.post("/login")
def login(
        request: LoginRequest,
        db: Session = Depends(get_db)
):

    try:

        token = AuthService.login(
            db,
            request.email,
            request.password
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    except Exception as e:

        raise HTTPException(
            status_code=401,
            detail=str(e)
        )
    
@router.get("/me")
def get_me(
        current_user: User = Depends(
            get_current_user
        )
):

    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email
    }