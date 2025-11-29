"""
Health Check Endpoints

API endpoints for health status monitoring.
"""

from fastapi import APIRouter, Depends

from app.api.dependencies import get_model
from app.config import get_settings
from app.logger import get_logger
from app.models.schemas import HealthResponse
from app.services.model_service import ModelService

logger = get_logger(__name__)
settings = get_settings()

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=HealthResponse)
async def health_check(
    model_service: ModelService = Depends(get_model),
) -> HealthResponse:
    """
    Check API health status.

    Returns:
        Health status including model loading state
    """
    logger.info("Health check requested")

    response = HealthResponse(
        status="healthy",
        model_loaded=model_service.is_loaded,
        version=settings.VERSION,
    )

    logger.info(f"Health check response: status={response.status}, model_loaded={response.model_loaded}")

    return response


@router.get("/")
async def root() -> dict:
    """
    Root endpoint.

    Returns:
        Welcome message
    """
    return {
        "message": "Welcome to the Urdu Character Recognition API",
        "version": settings.VERSION,
        "docs": "/docs",
    }
