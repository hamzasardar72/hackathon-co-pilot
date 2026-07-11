# ClaimWise AI – Insurance Claim Processing Co-Pilot

ClaimWise AI is a production-style hackathon demo for multimodal insurance claim intake and AI-assisted damage triage.

## Stack

- Frontend: Angular 20 + Bootstrap 5 + TypeScript
- Backend: FastAPI + Python + JWT + REST
- AI: TensorFlow/Keras-style CNN mock pipeline with OpenCV + Grad-CAM-inspired explanation layer
- Database: PostgreSQL schema and SQL seed data

## Folder Structure

- `frontend/` – Angular 20 dashboard client
- `backend/` – FastAPI API and model orchestration
- `database/` – PostgreSQL DDL
- `docs/` – deployment, architecture, presentation, and API docs
- `ai/` – AI model artifacts and training notes

## Quick Start

1. Create Python virtual environment and install backend dependencies.
2. Install frontend dependencies with `npm install` inside `frontend/`.
3. Run `uvicorn backend.app.main:app --reload`.
4. Run `npm start` inside `frontend/`.

## Demo Capabilities

- Claim intake with image and PDF upload references
- AI classification, severity, fraud risk, and cost estimate output
- Human review with approve/reject/modify flow
- PDF report generation structure
- Explainability panel with confidence and feature insights

## Business Model Snapshot

- SaaS subscription
- Enterprise licensing
- Per-claim processing fees
- ROI calculator panel in the dashboard
