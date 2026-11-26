from fastapi import FastAPI

app = FastAPI(
    title="Geospatial File Measurement API",
    description="Backend service for processing geospatial files and calculating measurements.",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return the application health status."""
    return {"status": "ok"}