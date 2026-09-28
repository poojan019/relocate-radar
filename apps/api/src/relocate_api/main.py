"""FastAPI application entrypoint."""

from fastapi import FastAPI

app = FastAPI(title="RelocateRadar API", version="0.0.1")


@app.get("/health")
def health() -> dict[str, str]:
    """Liveness probe."""
    return {"status": "ok"}
