from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.routes import analytics, auth, claims, reports

app = FastAPI(
    title="ClaimWise AI API",
    version="1.0.0",
    description="Insurance claim processing copilot backend",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "http://localhost:4201",
        "https://frontend-dun-delta-72.vercel.app",
        "https://hackathon-co-pilot-no6mcaahm-hamza72.vercel.app",
        "https://hackathon-co-pilot.vercel.app",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(claims.router, prefix="/api/claims", tags=["Claims"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics"])
app.include_router(reports.router, prefix="/api/reports", tags=["Reports"])


@app.get("/")
def root_status():
    return {
        "message": "ClaimWise AI API is running",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "claimwise-ai-api",
        "version": "1.0.0",
    }
