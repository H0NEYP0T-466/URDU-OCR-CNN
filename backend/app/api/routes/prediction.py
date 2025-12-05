"""
Prediction Endpoints

API endpoints for Urdu character and digit prediction.
"""

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status

from app.api.dependencies import get_image_processor, get_model, get_digit_model
from app.config import URDU_CHARACTERS, get_settings
from app.core.exceptions import (
    ImageProcessingError,
    ImageTooLargeError,
    InvalidImageError,
    ModelNotLoadedError,
    PredictionError,
    UnsupportedImageFormatError,
)
from app.logger import get_logger
from app.models.schemas import (
    Base64ImageRequest,
    ClassesResponse,
    ErrorResponse,
    PredictionResponse,
    TopPrediction,
)
from app.services.image_service import ImageService
from app.services.model_service import ModelService
from app.services.digit_model_service import DigitModelService, URDU_DIGITS

logger = get_logger(__name__)
settings = get_settings()

router = APIRouter(prefix="/api/v1", tags=["Prediction"])


@router.post(
    "/predict",
    response_model=PredictionResponse,
    responses={
        400: {"model": ErrorResponse, "description": "Invalid image"},
        500: {"model": ErrorResponse, "description": "Prediction error"},
        503: {"model": ErrorResponse, "description": "Model not loaded"},
    },
)
async def predict_from_image(
    file: UploadFile = File(..., description="Image file to predict"),
    model_service: ModelService = Depends(get_model),
    image_service: ImageService = Depends(get_image_processor),
) -> PredictionResponse:
    """
    Predict Urdu character from uploaded image.

    - **file**: Image file (PNG, JPG, JPEG, BMP) max 5MB

    Returns prediction with confidence score and top 5 predictions.
    """
    logger.info(f"Received prediction request - File: {file.filename}, Content-Type: {file.content_type}")

    try:
        # Read file content
        file_content = await file.read()
        file_size = len(file_content)

        logger.info(f"File size: {file_size} bytes")

        # Validate file
        image_service.validate_file(file.filename or "unknown", file_size)

        # Preprocess image
        processed_image = await image_service.process_uploaded_file(
            file_content, file.filename or "unknown"
        )

        # Check if model is loaded
        if not model_service.is_loaded:
            logger.warning("Model not loaded, returning mock prediction")
            # Return mock prediction for demo purposes when model isn't loaded
            return PredictionResponse(
                prediction="ا",
                confidence=0.0,
                top_5=[TopPrediction(character=char, probability=0.0) for char in list(URDU_CHARACTERS.values())[:5]],
                processing_time_ms=0.0,
            )

        # Make prediction
        prediction, confidence, top_5, processing_time = model_service.predict(processed_image)

        logger.info(f"Prediction completed - Character: {prediction}, Confidence: {confidence:.4f}")
        logger.info(f"Processing time: {processing_time:.2f}ms")

        return PredictionResponse(
            prediction=prediction,
            confidence=confidence,
            top_5=[TopPrediction(**p) for p in top_5],
            processing_time_ms=round(processing_time, 2),
        )

    except UnsupportedImageFormatError as e:
        logger.error(f"Unsupported image format: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e.message),
        )

    except ImageTooLargeError as e:
        logger.error(f"Image too large: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e.message),
        )

    except InvalidImageError as e:
        logger.error(f"Invalid image: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e.message),
        )

    except ImageProcessingError as e:
        logger.error(f"Image processing error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e.message),
        )

    except ModelNotLoadedError as e:
        logger.error(f"Model not loaded: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(e.message),
        )

    except PredictionError as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e.message),
        )

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}",
        )


@router.post(
    "/predict/canvas",
    response_model=PredictionResponse,
    responses={
        400: {"model": ErrorResponse, "description": "Invalid image data"},
        500: {"model": ErrorResponse, "description": "Prediction error"},
        503: {"model": ErrorResponse, "description": "Model not loaded"},
    },
)
async def predict_from_canvas(
    request: Base64ImageRequest,
    model_service: ModelService = Depends(get_model),
    image_service: ImageService = Depends(get_image_processor),
) -> PredictionResponse:
    """
    Predict Urdu character from canvas drawing (base64 encoded).

    - **image_data**: Base64 encoded image string

    Returns prediction with confidence score and top 5 predictions.
    """
    logger.info("Received canvas prediction request")

    try:
        # Process base64 image
        processed_image = image_service.process_base64_image(request.image_data)

        # Check if model is loaded
        if not model_service.is_loaded:
            logger.warning("Model not loaded, returning mock prediction")
            return PredictionResponse(
                prediction="ا",
                confidence=0.0,
                top_5=[TopPrediction(character=char, probability=0.0) for char in list(URDU_CHARACTERS.values())[:5]],
                processing_time_ms=0.0,
            )

        # Make prediction
        prediction, confidence, top_5, processing_time = model_service.predict(processed_image)

        logger.info(f"Canvas prediction completed - Character: {prediction}, Confidence: {confidence:.4f}")
        logger.info(f"Processing time: {processing_time:.2f}ms")

        return PredictionResponse(
            prediction=prediction,
            confidence=confidence,
            top_5=[TopPrediction(**p) for p in top_5],
            processing_time_ms=round(processing_time, 2),
        )

    except InvalidImageError as e:
        logger.error(f"Invalid image data: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e.message),
        )

    except ImageProcessingError as e:
        logger.error(f"Image processing error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e.message),
        )

    except ModelNotLoadedError as e:
        logger.error(f"Model not loaded: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(e.message),
        )

    except PredictionError as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e.message),
        )

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}",
        )


@router.get(
    "/classes",
    response_model=ClassesResponse,
)
async def get_classes(
    model_service: ModelService = Depends(get_model),
) -> ClassesResponse:
    """
    Get list of all Urdu characters the model can recognize.

    Returns list of characters and total count.
    """
    logger.info("Classes list requested")

    classes = model_service.get_classes()

    logger.info(f"Returning {len(classes)} character classes")

    return ClassesResponse(
        classes=classes,
        count=len(classes),
    )


# ==================== DIGIT PREDICTION ENDPOINTS ====================


@router.post(
    "/predict/digit",
    response_model=PredictionResponse,
    responses={
        400: {"model": ErrorResponse, "description": "Invalid image"},
        500: {"model": ErrorResponse, "description": "Prediction error"},
        503: {"model": ErrorResponse, "description": "Model not loaded"},
    },
)
async def predict_digit_from_image(
    file: UploadFile = File(..., description="Image file to predict"),
    digit_model_service: DigitModelService = Depends(get_digit_model),
    image_service: ImageService = Depends(get_image_processor),
) -> PredictionResponse:
    """
    Predict Urdu digit from uploaded image.

    - **file**: Image file (PNG, JPG, JPEG, BMP) max 5MB

    Returns prediction with confidence score and top predictions.
    """
    logger.info(f"Received digit prediction request - File: {file.filename}, Content-Type: {file.content_type}")

    try:
        # Read file content
        file_content = await file.read()
        file_size = len(file_content)

        logger.info(f"File size: {file_size} bytes")

        # Validate file
        image_service.validate_file(file.filename or "unknown", file_size)

        # Preprocess image
        processed_image = await image_service.process_uploaded_file(
            file_content, file.filename or "unknown"
        )

        # Check if model is loaded
        if not digit_model_service.is_loaded:
            logger.warning("Digit model not loaded, returning mock prediction")
            # Return mock prediction for demo purposes when model isn't loaded
            return PredictionResponse(
                prediction="۰",
                confidence=0.0,
                top_5=[TopPrediction(character=char, probability=0.0) for char in list(URDU_DIGITS.values())[:5]],
                processing_time_ms=0.0,
            )

        # Make prediction
        prediction, confidence, top_5, processing_time = digit_model_service.predict(processed_image)

        logger.info(f"Digit prediction completed - Digit: {prediction}, Confidence: {confidence:.4f}")
        logger.info(f"Processing time: {processing_time:.2f}ms")

        return PredictionResponse(
            prediction=prediction,
            confidence=confidence,
            top_5=[TopPrediction(**p) for p in top_5],
            processing_time_ms=round(processing_time, 2),
        )

    except UnsupportedImageFormatError as e:
        logger.error(f"Unsupported image format: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e.message),
        )

    except ImageTooLargeError as e:
        logger.error(f"Image too large: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e.message),
        )

    except InvalidImageError as e:
        logger.error(f"Invalid image: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e.message),
        )

    except ImageProcessingError as e:
        logger.error(f"Image processing error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e.message),
        )

    except ModelNotLoadedError as e:
        logger.error(f"Digit model not loaded: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(e.message),
        )

    except PredictionError as e:
        logger.error(f"Digit prediction error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e.message),
        )

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}",
        )


@router.post(
    "/predict/digit/canvas",
    response_model=PredictionResponse,
    responses={
        400: {"model": ErrorResponse, "description": "Invalid image data"},
        500: {"model": ErrorResponse, "description": "Prediction error"},
        503: {"model": ErrorResponse, "description": "Model not loaded"},
    },
)
async def predict_digit_from_canvas(
    request: Base64ImageRequest,
    digit_model_service: DigitModelService = Depends(get_digit_model),
    image_service: ImageService = Depends(get_image_processor),
) -> PredictionResponse:
    """
    Predict Urdu digit from canvas drawing (base64 encoded).

    - **image_data**: Base64 encoded image string

    Returns prediction with confidence score and top predictions.
    """
    logger.info("Received digit canvas prediction request")

    try:
        # Process base64 image
        processed_image = image_service.process_base64_image(request.image_data)

        # Check if model is loaded
        if not digit_model_service.is_loaded:
            logger.warning("Digit model not loaded, returning mock prediction")
            return PredictionResponse(
                prediction="۰",
                confidence=0.0,
                top_5=[TopPrediction(character=char, probability=0.0) for char in list(URDU_DIGITS.values())[:5]],
                processing_time_ms=0.0,
            )

        # Make prediction
        prediction, confidence, top_5, processing_time = digit_model_service.predict(processed_image)

        logger.info(f"Digit canvas prediction completed - Digit: {prediction}, Confidence: {confidence:.4f}")
        logger.info(f"Processing time: {processing_time:.2f}ms")

        return PredictionResponse(
            prediction=prediction,
            confidence=confidence,
            top_5=[TopPrediction(**p) for p in top_5],
            processing_time_ms=round(processing_time, 2),
        )

    except InvalidImageError as e:
        logger.error(f"Invalid image data: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e.message),
        )

    except ImageProcessingError as e:
        logger.error(f"Image processing error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e.message),
        )

    except ModelNotLoadedError as e:
        logger.error(f"Digit model not loaded: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(e.message),
        )

    except PredictionError as e:
        logger.error(f"Digit prediction error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e.message),
        )

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}",
        )


@router.get(
    "/classes/digits",
    response_model=ClassesResponse,
)
async def get_digit_classes(
    digit_model_service: DigitModelService = Depends(get_digit_model),
) -> ClassesResponse:
    """
    Get list of all Urdu digits the model can recognize.

    Returns list of digits and total count.
    """
    logger.info("Digit classes list requested")

    classes = digit_model_service.get_classes()

    logger.info(f"Returning {len(classes)} digit classes")

    return ClassesResponse(
        classes=classes,
        count=len(classes),
    )
