"""
Pydantic Schemas

Request and response schemas for the API.
"""

from typing import List, Optional

from pydantic import BaseModel, Field


class TopPrediction(BaseModel):
    """Single prediction result with character and probability."""

    character: str = Field(..., description="Predicted Urdu character")
    probability: float = Field(..., ge=0, le=1, description="Prediction probability")


class PredictionResponse(BaseModel):
    """Response schema for prediction endpoint."""

    prediction: str = Field(..., description="Top predicted Urdu character")
    confidence: float = Field(..., ge=0, le=1, description="Confidence score of the prediction")
    top_5: List[TopPrediction] = Field(..., description="Top 5 predictions with probabilities")
    processing_time_ms: float = Field(..., ge=0, description="Processing time in milliseconds")

    class Config:
        json_schema_extra = {
            "example": {
                "prediction": "ا",
                "confidence": 0.95,
                "top_5": [
                    {"character": "ا", "probability": 0.95},
                    {"character": "ب", "probability": 0.02},
                    {"character": "پ", "probability": 0.01},
                    {"character": "ت", "probability": 0.01},
                    {"character": "ٹ", "probability": 0.01},
                ],
                "processing_time_ms": 45.23,
            }
        }


class HealthResponse(BaseModel):
    """Response schema for health check endpoint."""

    status: str = Field(..., description="Health status of the API")
    model_loaded: bool = Field(..., description="Whether the ML model is loaded")
    version: str = Field(..., description="API version")

    class Config:
        json_schema_extra = {
            "example": {
                "status": "healthy",
                "model_loaded": True,
                "version": "1.0.0",
            }
        }


class ClassesResponse(BaseModel):
    """Response schema for classes endpoint."""

    classes: List[str] = Field(..., description="List of Urdu characters the model can recognize")
    count: int = Field(..., description="Total number of classes")

    class Config:
        json_schema_extra = {
            "example": {
                "classes": ["ا", "ب", "پ", "ت", "ٹ"],
                "count": 46,
            }
        }


class ErrorResponse(BaseModel):
    """Response schema for error responses."""

    detail: str = Field(..., description="Error message")
    error_type: Optional[str] = Field(None, description="Type of error")

    class Config:
        json_schema_extra = {
            "example": {
                "detail": "Invalid image format",
                "error_type": "InvalidImageError",
            }
        }


class Base64ImageRequest(BaseModel):
    """Request schema for base64 encoded image predictions."""

    image_data: str = Field(..., description="Base64 encoded image data")

    class Config:
        json_schema_extra = {
            "example": {
                "image_data": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=="
            }
        }
