import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_name: str = "ClaimWise AI"
    api_prefix: str = "/api"
    secret_key: str = os.getenv("JWT_SECRET_KEY", "claimwise-secret-key")
    algorithm: str = os.getenv("JWT_ALGORITHM", "HS256")


settings = Settings()
