
# CloudOps Platform

A cloud-ready REST API demonstrating containerization, automated testing,
and continuous integration practices.

## Project Overview

CloudOps Platform is a Python FastAPI service packaged with Docker and
validated through automated tests. GitHub Actions runs the test suite
when code is pushed to the `main` branch or a pull request targets it.

## Architecture

```text
Developer
   |
   v
Git + GitHub Repository
   |
   v
GitHub Actions CI
   |
   +--> Install Python dependencies
   |
   +--> Run pytest suite
   |
   v
Validated application code

Local deployment:
Docker Image --> Docker Container --> FastAPI endpoints
```

## Technology Stack

- Python 3.13
- FastAPI
- Uvicorn
- Pytest
- HTTPX
- Docker
- Git and GitHub
- GitHub Actions

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Service status |
| GET | `/health` | Health check |
| GET | `/ready` | Readiness endpoint |
| GET | `/info` | Service metadata |
| GET | `/docs` | Interactive API documentation |

## Run Locally

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

Start the API:

```bash
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` to explore the API.

## Run Tests

```bash
python -m pytest -v
```

## Run with Docker

Build the image:

```bash
docker build -t cloudops-platform:1.0 .
```

Run the container:

```bash
docker run --rm --name cloudops-api -p 8000:8000 cloudops-platform:1.0
```

In another terminal, check its health:

```bash
curl http://localhost:8000/health
```

Stop a foreground container with `Ctrl+C`.

## Continuous Integration

The GitHub Actions workflow is defined in
`.github/workflows/ci.yml`.

It installs the development dependencies and runs the automated tests
on pushes to `main` and pull requests targeting `main`.

## Repository Structure

```text
cloudops-platform/
├── app/
│   └── main.py
├── tests/
│   └── test_main.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## Current Scope and Future Improvements

This is a production-style learning project, not yet a production deployment.

Planned improvements include:
- Structured application logging
- Stronger readiness checks and configuration management
- Container security and dependency scanning
- Terraform infrastructure validation
- Cloud deployment design with cost controls
- Monitoring and operational documentation

## Cost and Security

The application and Docker container currently run locally. GitHub Actions
runs automated tests; no AWS infrastructure is required for these steps.

Do not commit passwords, access keys, tokens, or `.env` files.
