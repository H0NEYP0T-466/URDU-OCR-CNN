"""
FastAPI Application Entry Point

Main application file for the Urdu Character Recognition API.
"""

import sys
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.routes import health, prediction
from app.config import get_settings
from app.core.exceptions import UrduOCRException
from app.logger import get_logger, setup_logger
from app.services.model_service import get_model_service
from app.services.digit_model_service import get_digit_model_service

# Initialize settings
settings = get_settings()

# Setup logger
logger = setup_logger(
    name="urdu_ocr",
    log_level=settings.LOG_LEVEL,
    log_file=str(settings.log_file_resolved),
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan events handler.
    Handles startup and shutdown events.
    """
    # Startup
    logger.info("=" * 50)
    logger.info("URDU CHARACTER RECOGNITION API")
    logger.info("=" * 50)
    logger.info(f"Environment: {settings.ENVIRONMENT}")
    logger.info(f"Debug Mode: {settings.DEBUG}")
    logger.info("Initializing application components...")

    logger.info("Starting Urdu Character Recognition API Server...")
    logger.info("Loading configuration...")

    # Initialize character model service
    logger.info("Initializing character model service...")
    model_service = get_model_service()

    try:
        model_path = settings.model_path_resolved
        logger.info(f"Attempting to load character model from: {model_path}")

        if model_path.exists():
            model_service.load_model(str(model_path))
            logger.info(f"Character model loaded successfully from {model_path}")
            logger.info(f"Model input shape: {model_service.model.input_shape}")
            logger.info(f"Number of classes: {model_service.num_classes}")
        else:
            logger.warning(f"Character model file not found at: {model_path}")
            logger.info("Running in demo mode without trained character model")
            logger.info("To train a character model, run: python -m ml.train")

    except Exception as e:
        logger.warning(f"Could not load character model: {str(e)}")
        logger.info("Running in demo mode without trained character model")

    # Initialize digit model service
    logger.info("Initializing digit model service...")
    digit_model_service = get_digit_model_service()

    try:
        digit_model_path = settings.digit_model_path_resolved
        logger.info(f"Attempting to load digit model from: {digit_model_path}")

        if digit_model_path.exists():
            digit_model_service.load_model(str(digit_model_path))
            logger.info(f"Digit model loaded successfully from {digit_model_path}")
            logger.info(f"Model input shape: {digit_model_service.model.input_shape}")
            logger.info(f"Number of classes: {digit_model_service.num_classes}")
        else:
            logger.warning(f"Digit model file not found at: {digit_model_path}")
            logger.info("Running in demo mode without trained digit model")
            logger.info("To train a digit model, run: python -m ml.digit_cnn.train")

    except Exception as e:
        logger.warning(f"Could not load digit model: {str(e)}")
        logger.info("Running in demo mode without trained digit model")

    logger.info("Server ready to accept requests")
    logger.info(f"API documentation available at: http://{settings.HOST}:{settings.PORT}/docs")

    yield

    # Shutdown
    logger.info("Shutting down server...")
    logger.info("Cleaning up resources...")

    # Unload models to free memory
    model_service.unload_model()
    digit_model_service.unload_model()

    logger.info("Server shutdown complete")


# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    description="""
    ## Urdu Character Recognition API

    This API provides handwritten Urdu character recognition using a Convolutional Neural Network (CNN).

    ### Features:
    - Upload images of handwritten Urdu characters for prediction
    - Draw characters on canvas and get predictions
    - Support for 46 Urdu characters including digits

    ### Endpoints:
    - **POST /api/v1/predict** - Predict character from uploaded image
    - **POST /api/v1/predict/canvas** - Predict character from canvas drawing
    - **GET /api/v1/classes** - Get list of supported characters
    - **GET /api/v1/health** - Check API health status
    """,
    version=settings.VERSION,
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Global exception handler for custom exceptions
@app.exception_handler(UrduOCRException)
async def urdu_ocr_exception_handler(request: Request, exc: UrduOCRException):
    """Handle custom application exceptions."""
    logger.error(f"Application error: {exc.message}")
    logger.debug(f"Error details: {exc.details}")

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "detail": exc.message,
            "error_type": type(exc).__name__,
        },
    )


# Global exception handler for unexpected errors
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Handle unexpected exceptions."""
    logger.error(f"Unexpected error: {str(exc)}")
    logger.exception("Full traceback:")

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "detail": "An unexpected error occurred. Please try again.",
            "error_type": "InternalServerError",
        },
    )


# Include routers
app.include_router(health.router)
app.include_router(prediction.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )
