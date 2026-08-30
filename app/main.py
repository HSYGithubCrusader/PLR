from fastapi import FastAPI

app = FastAPI(
    title="Plumber Lead Recovery",
    version="0.1.0",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
