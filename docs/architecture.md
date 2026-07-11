# ClaimWise AI Architecture

## High-Level Design

- Frontend: Angular 20 dashboard for authentication, claim intake, AI results, and review workflow
- Backend: FastAPI REST API with JWT security, claim orchestration, and report endpoints
- AI Engine: CNN-style damage assessment pipeline with explainability hooks and severity scoring
- Database: PostgreSQL schema for users, claims, and decision logs
- Explainability Layer: confidence score, feature importance, and Grad-CAM-style heatmap rationale

## Runtime Flow

1. Claims officer uploads vehicle image and supporting claim documents.
2. Backend stores claim metadata and invokes AI assessment service.
3. AI engine returns classification, severity, confidence, fraud risk, and explanation.
4. Reviewer approves, rejects, or modifies the recommendation.
5. Final decision and notes are persisted and used for PDF generation.
