.PHONY: setup backend frontend test docker-up docker-down

setup:
	python -m venv .venv && . .venv/bin/activate && pip install -r backend/requirements.txt

backend:
	uvicorn backend.app:app --reload --port 8000

frontend:
	cd frontend && npm ci && npm run dev

test:
	pytest -q backend/tests

docker-up:
	docker compose up -d db

docker-down:
	docker compose down -v
