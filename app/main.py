from fastapi import FastAPI
from app.api.em_router import router as em_router
from app.settings import Settings
from app.utils.logging import configure_logging
from fastapi.middleware.cors import CORSMiddleware

settings = Settings()
configure_logging()

app = FastAPI(title="EM Reports API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(em_router, prefix="/reports/em-envelope", tags=["EM Envelope"])
