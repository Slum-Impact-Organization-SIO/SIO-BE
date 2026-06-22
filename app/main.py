from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="SIO-BE API",
    description="Backend API for SIO Services",
    version="0.1.0",
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "Welcome to SIO-BE API",
        "status": "online",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}
