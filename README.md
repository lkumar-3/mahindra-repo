# Full‑Stack Sample Repo (Python FastAPI + React + AWS + CI/CD)

This repo is to practice and demonstrate to all level skills across **Python backend**, **React frontend**, **AWS (ECS/Fargate + S3/CloudFront)**, **CI/CD**, **microservices patterns**, and **SQL (Postgres)**.

> Built for local development first. Then gradually containerize and deploy to AWS using the included workflows and Terraform skeleton.

---

## 🧱 Stack
- **Backend**: FastAPI, SQLAlchemy 2.0 async, JWT (python-jose), pytest
- **Frontend**: React 18 + TypeScript + React Query + Axios + Vite
- **DB**: PostgreSQL (docker-compose for local)
- **CI/CD**: GitHub Actions (lint/test/build/deploy), Docker, ECR, ECS Fargate
- **Infra (optional)**: Terraform skeleton for ECS task + logs

---

## 🚀 Quick Start (Local Dev)

### Prerequisites
- Python 3.11+
- Node.js 18/20+
- Docker + Docker Compose

### 1) Start Postgres (Docker)
```bash
docker compose up -d db
```
Database URL (default): `postgresql+asyncpg://postgres:postgres@localhost:5432/orders`

### 2) Backend
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r backend/requirements.txt
python backend/scripts/init_db.py
uvicorn backend.app:app --reload --port 8000
```

Generate a JWT for testing (default secret in `.env.example`):
```bash
python scripts/generate_jwt.py --sub user-1
```
Use it as `Authorization: Bearer <token>`.

### 3) Frontend
```bash
cd frontend
npm ci
npm run dev  # http://localhost:5173
```

Update API base URL in `frontend/src/api.ts` if needed (default `http://localhost:8000`).

### 4) Try it
- Open the frontend, create an order.
- Or call the API directly:
```bash
curl -H "Authorization: Bearer <token>" http://localhost:8000/orders
```

---

## 🧪 Tests
```bash
pytest -q backend/tests
```

---

## 🐳 Docker Compose (Backend + DB)
```bash
docker compose up --build backend db
```
Backend will run on `http://localhost:8080` in container mode; adjust frontend API base accordingly.

---

## ☁️ AWS Deployment Overview
- **Backend**: GitHub Actions builds a Docker image → pushes to **Amazon ECR** → triggers ECS **Fargate** service redeploy.
- **Frontend**: Build artifacts uploaded to **S3** and served via **CloudFront**. Invalidation step included in workflow.

> Configure secrets in GitHub: `AWS_ROLE_ARN`, `ECR_REPO`, `ECS_CLUSTER`, `ECS_SERVICE`, `CF_ID`.

---

## 📁 Repo Structure
```
fullstack-sample-repo/
├─ backend/
│  ├─ app.py
│  ├─ auth.py
│  ├─ models.py
│  ├─ requirements.txt
│  ├─ Dockerfile
│  ├─ scripts/
│  │  └─ init_db.py
│  └─ tests/
│     └─ test_orders.py
├─ frontend/
│  ├─ package.json
│  ├─ tsconfig.json
│  ├─ vite.config.ts
│  ├─ public/index.html
│  └─ src/
│     ├─ main.tsx
│     ├─ App.tsx
│     ├─ OrdersTable.tsx
│     └─ api.ts
├─ infra/
│  └─ terraform/
│     ├─ provider.tf
│     ├─ variables.tf
│     ├─ ecs-task.tf
│     └─ README.md
├─ .github/workflows/
│  ├─ ci.yml
│  ├─ deploy-backend.yml
│  └─ deploy-frontend.yml
├─ docker-compose.yml
├─ Makefile
└─ scripts/
   └─ generate_jwt.py
```

---

## 🔐 Environment Variables
- Backend: `DATABASE_URL`, `JWT_SECRET`, `JWT_ALGO` (defaults provided in code for local dev only)
- Frontend: uses browser `localStorage` for token; update `api.ts` if you change header scheme.

---

## ✅ Next Steps / Extensions
- Add Alembic migrations
- Add SQS event publisher/consumer (microservices demo)
- Add OpenAPI auth flow & token refresh
- Add CodeDeploy blue/green for ECS
- Add Storybook for UI components

---

## License
MIT (for learning/demo purposes)
