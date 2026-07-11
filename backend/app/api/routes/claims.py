from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from pydantic import BaseModel

router = APIRouter()


class ClaimItem(BaseModel):
    id: str
    claimant_name: str
    policy_number: str
    damage_type: str
    severity: str
    confidence: float
    estimated_cost_range: str
    fraud_risk_score: float
    status: str
    created_at: str


class RecommendationResponse(BaseModel):
    claim_id: str
    classification: str
    severity: str
    confidence_score: float
    estimated_cost_range: str
    fraud_risk_score: float
    explanation: str
    feature_importance: List[str]


CLAIMS: List[ClaimItem] = [
    ClaimItem(
        id="CLM-1001",
        claimant_name="Ava Thompson",
        policy_number="POL-2048",
        damage_type="Rear Bumper",
        severity="Moderate",
        confidence=0.93,
        estimated_cost_range="$1,800 - $3,200",
        fraud_risk_score=0.11,
        status="Pending Review",
        created_at=datetime.utcnow().isoformat(),
    )
]


@router.get("", response_model=List[ClaimItem])
def list_claims():
    return CLAIMS


@router.post("/submit")
def submit_claim(
    claimant_name: str = Form(...),
    policy_number: str = Form(...),
    damage_type: str = Form(...),
    image: Optional[UploadFile] = File(default=None),
    pdf_document: Optional[UploadFile] = File(default=None),
):
    claim = ClaimItem(
        id=f"CLM-{len(CLAIMS) + 1000}",
        claimant_name=claimant_name,
        policy_number=policy_number,
        damage_type=damage_type,
        severity="Moderate",
        confidence=0.92,
        estimated_cost_range="$1,500 - $2,900",
        fraud_risk_score=0.14,
        status="Pending Review",
        created_at=datetime.utcnow().isoformat(),
    )
    CLAIMS.insert(0, claim)
    return {"message": "Claim submitted successfully", "claim": claim.model_dump()}


@router.post("/analyze", response_model=RecommendationResponse)
def analyze_claim():
    return RecommendationResponse(
        claim_id="CLM-1001",
        classification="Vehicle Damage",
        severity="Moderate",
        confidence_score=0.93,
        estimated_cost_range="$1,800 - $3,200",
        fraud_risk_score=0.11,
        explanation="The model detected structural deformation and surface scratches concentrated around the rear passenger side, consistent with moderate collision damage.",
        feature_importance=["crack density", "panel contour shift", "image sharpness", "vehicle geometry alignment"],
    )


@router.patch("/{claim_id}/review")
def review_claim(claim_id: str, decision: str, reviewer_notes: str = ""):
    if not any(claim.id == claim_id for claim in CLAIMS):
        raise HTTPException(status_code=404, detail="Claim not found")

    for claim in CLAIMS:
        if claim.id == claim_id:
            claim.status = decision.title()
            break

    return {
        "message": "Decision stored successfully",
        "claim_id": claim_id,
        "decision": decision,
        "reviewer_notes": reviewer_notes,
    }
