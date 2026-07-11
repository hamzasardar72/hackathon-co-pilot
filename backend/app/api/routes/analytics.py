from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class AnalyticsResponse(BaseModel):
    total_claims: int
    pending_reviews: int
    approved_claims: int
    rejected_claims: int
    ai_accuracy: float
    claim_trends: list[dict]
    fraud_trends: list[dict]
    processing_time_metrics: list[dict]


@router.get("", response_model=AnalyticsResponse)
def get_analytics():
    return AnalyticsResponse(
        total_claims=1284,
        pending_reviews=186,
        approved_claims=842,
        rejected_claims=256,
        ai_accuracy=0.94,
        claim_trends=[{"month": "Jan", "claims": 120}, {"month": "Feb", "claims": 144}],
        fraud_trends=[{"month": "Jan", "risk": 0.08}, {"month": "Feb", "risk": 0.12}],
        processing_time_metrics=[{"step": "Intake", "hours": 1.6}, {"step": "Review", "hours": 2.8}],
    )
