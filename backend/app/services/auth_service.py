from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository

from app.core.security import (
    hash_password,
    verify_password
)

from app.core.jwt import create_access_token


class AuthService:

    @staticmethod
    def register(
            db: Session,
            name: str,
            email: str,
            password: str
    ):

        existing_user = (
            UserRepository.get_by_email(
                db,
                email
            )
        )

        if existing_user:

            raise Exception(
                "Email already registered"
            )

        hashed_password = (
            hash_password(password)
        )

        return (
            UserRepository.create_user(
                db,
                name,
                email,
                hashed_password
            )
        )

    @staticmethod
    def login(
            db: Session,
            email: str,
            password: str
    ):

        user = (
            UserRepository.get_by_email(
                db,
                email
            )
        )

        if not user:

            raise Exception(
                "Invalid credentials"
            )

        if not verify_password(
                password,
                user.password
        ):

            raise Exception(
                "Invalid credentials"
            )

        return create_access_token(
            {
                "sub": str(user.id),
                "email": user.email
            }
        )