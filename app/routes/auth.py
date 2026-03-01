from fastapi import (
    APIRouter,
    Depends,
    Response,
    Request
)
from sqlalchemy.orm import Session
from app.schemas.auth import (
    RegisterRequest,
    LoginRequest,
    TokenResponse
)
from app.core.database import get_db
from app.services.auth_service import (
    register_user,
    authenticate_user
)
from app.core.security import (
    create_access_token
)
from jose import jwt
from app.core.config import (
    SECRET_KEY,
    ALGORITHM
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register")
def register(
    data: RegisterRequest,
    db: Session = Depends(get_db)
):

    register_user(
        db,
        data.email,
        data.password
    )

    return {"message": "User created"}

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    data: LoginRequest,
    response: Response,
    db: Session = Depends(get_db)
):

    access_token, refresh_token = \
        authenticate_user(
            db,
            data.email,
            data.password
        )

    # HTTP ONLY COOKIE
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=False,  # True in production HTTPS
        samesite="lax"
    )

    return {
        "access_token": access_token
    }

@router.post("/refresh")
def refresh_token(
    request: Request
):

    token = request.cookies.get(
        "refresh_token"
    )

    if not token:
        raise Exception("No refresh token")

    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    user_id = payload.get("sub")

    new_access_token = create_access_token(
        {"sub": user_id}
    )

    return {
        "access_token": new_access_token
    }