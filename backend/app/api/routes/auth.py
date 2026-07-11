from datetime import datetime, timedelta
from typing import Optional

import jwt
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter()
SECRET_KEY = "claimwise-secret-key"
ALGORITHM = "HS256"


class LoginRequest(BaseModel):
    email: str
    password: str


class RegisterRequest(BaseModel):
    full_name: str
    email: str
    password: str
    role: str = "claims_officer"


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest):
    if payload.email and payload.password:
        token = jwt.encode(
            {
                "sub": payload.email,
                "role": "claims_officer",
                "exp": datetime.utcnow() + timedelta(hours=8),
            },
            SECRET_KEY,
            algorithm=ALGORITHM,
        )
        return {"access_token": token}

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")


@router.post("/register", response_model=TokenResponse)
def register(payload: RegisterRequest):
    token = jwt.encode(
        {
            "sub": payload.email,
            "role": payload.role,
            "exp": datetime.utcnow() + timedelta(hours=8),
        },
        SECRET_KEY,
        algorithm=ALGORITHM,
    )
    return {"access_token": token}
