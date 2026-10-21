
from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(
    title="CloudOps Platform API",
    description="A cloud-ready API with operational health checks.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "service": "CloudOps Platform",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/ready")
def readiness():
    return {"status": "ready"}


@app.get("/info")
def info():
    return {
        "service": "CloudOps Platform API",
        "version": app.version,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
