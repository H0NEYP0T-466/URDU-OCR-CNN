"""
API Dependencies

Shared dependencies for API routes.
"""

from app.services.image_service import ImageService, get_image_service
from app.services.model_service import ModelService, get_model_service
from app.services.digit_model_service import DigitModelService, get_digit_model_service


def get_model() -> ModelService:
    """
    Dependency to get model service.

    Returns:
        ModelService instance
    """
    return get_model_service()


def get_digit_model() -> DigitModelService:
    """
    Dependency to get digit model service.

    Returns:
        DigitModelService instance
    """
    return get_digit_model_service()


def get_image_processor() -> ImageService:
    """
    Dependency to get image service.

    Returns:
        ImageService instance
    """
    return get_image_service()
