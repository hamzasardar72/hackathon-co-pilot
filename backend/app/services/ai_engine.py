from dataclasses import dataclass
from typing import Any


@dataclass
class DamageAssessment:
    classification: str
    severity: str
    confidence_score: float
    estimated_cost_range: str
    fraud_risk_score: float
    explanation: str
    feature_importance: list[str]


def run_cnn_damage_assessment(image_bytes: bytes | None = None, claim_metadata: dict[str, Any] | None = None) -> DamageAssessment:
    """Reference AI assessment pipeline for demo purposes.

    The implementation intentionally uses a deterministic heuristic placeholder to keep the
    hackathon demo runnable without a trained model artifact in the repository.
    """
    metadata = claim_metadata or {}
    damage_type = metadata.get("damage_type", "Rear bumper")
    severity = "Moderate"
    confidence = 0.93
    fraud_risk = 0.11
    explanation = (
        f"The model detected concentrated impact patterns around the {damage_type.lower()} region, "
        "with an elevated structural distortion score and moderate panel surface damage."
    )

    return DamageAssessment(
        classification="Vehicle Damage",
        severity=severity,
        confidence_score=confidence,
        estimated_cost_range="$1,800 - $3,200",
        fraud_risk_score=fraud_risk,
        explanation=explanation,
        feature_importance=[
            "panel contour distortion",
            "edge crack density",
            "surface texture variance",
            "vehicle geometry alignment",
        ],
    )
