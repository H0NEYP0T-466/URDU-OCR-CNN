"""
Custom Exceptions

Custom exception classes for the Urdu Character Recognition API.
"""

from typing import Any, Dict, Optional


class UrduOCRException(Exception):
    """Base exception for Urdu OCR application."""

    def __init__(
        self,
        message: str = "An error occurred in the Urdu OCR application",
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.message = message
        self.details = details or {}
        super().__init__(self.message)


class ModelLoadError(UrduOCRException):
    """Exception raised when model loading fails."""

    def __init__(
        self,
        message: str = "Failed to load the ML model",
        model_path: Optional[str] = None,
    ) -> None:
        details = {"model_path": model_path} if model_path else {}
        super().__init__(message, details)


class ModelNotLoadedError(UrduOCRException):
    """Exception raised when prediction is attempted without a loaded model."""

    def __init__(
        self,
        message: str = "Model is not loaded. Please ensure the model is loaded before making predictions.",
    ) -> None:
        super().__init__(message)


class InvalidImageError(UrduOCRException):
    """Exception raised for invalid image input."""

    def __init__(
        self,
        message: str = "Invalid image provided",
        filename: Optional[str] = None,
    ) -> None:
        details = {"filename": filename} if filename else {}
        super().__init__(message, details)


class ImageTooLargeError(InvalidImageError):
    """Exception raised when image file size exceeds limit."""

    def __init__(
        self,
        message: str = "Image file size exceeds the maximum allowed size",
        file_size: Optional[int] = None,
        max_size: Optional[int] = None,
    ) -> None:
        super().__init__(message)
        self.details["file_size"] = file_size
        self.details["max_size"] = max_size


class UnsupportedImageFormatError(InvalidImageError):
    """Exception raised for unsupported image formats."""

    def __init__(
        self,
        message: str = "Unsupported image format",
        format: Optional[str] = None,
        supported_formats: Optional[list] = None,
    ) -> None:
        super().__init__(message)
        self.details["format"] = format
        self.details["supported_formats"] = supported_formats


class ImageProcessingError(UrduOCRException):
    """Exception raised during image preprocessing."""

    def __init__(
        self,
        message: str = "Error occurred during image processing",
        step: Optional[str] = None,
    ) -> None:
        details = {"processing_step": step} if step else {}
        super().__init__(message, details)


class PredictionError(UrduOCRException):
    """Exception raised during prediction."""

    def __init__(
        self,
        message: str = "Error occurred during prediction",
        original_error: Optional[str] = None,
    ) -> None:
        details = {"original_error": original_error} if original_error else {}
        super().__init__(message, details)


class ClassLabelsNotFoundError(UrduOCRException):
    """Exception raised when class labels file is not found."""

    def __init__(
        self,
        message: str = "Class labels file not found",
        path: Optional[str] = None,
    ) -> None:
        details = {"path": path} if path else {}
        super().__init__(message, details)
