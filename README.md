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

1. Create a Python virtual environment and install backend dependencies:
   `python -m venv .venv`
   `pip install -r backend/requirements.txt`
2. Install frontend dependencies inside `frontend/`:
   `npm install`
3. Start the API from the backend folder:
   `cd backend && uvicorn app.main:app --reload --host 127.0.0.1 --port 8000`
4. Start the Angular dashboard:
   `npm start --prefix frontend`

## Hackathon Demo Notes

- The API now boots with stable package versions and a consistent import layout.
- The frontend dev server is configured for a predictable local URL.
- AI recommendation logic is exposed through a deterministic demo engine so the demo remains runnable without model artifacts.

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
