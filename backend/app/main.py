from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth, claims, analytics, reports

app = FastAPI(
    title="ClaimWise AI API",
    version="1.0.0",
    description="Insurance claim processing copilot backend",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(claims.router, prefix="/api/claims", tags=["Claims"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics"])
app.include_router(reports.router, prefix="/api/reports", tags=["Reports"])


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "claimwise-ai-api",
        "version": "1.0.0",
    }
