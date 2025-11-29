"""
Utility Helper Functions

Various utility functions for the Urdu Character Recognition API.
"""

import base64
import io
import os
import time
from pathlib import Path
from typing import Callable, Any, TypeVar

from PIL import Image

from app.logger import get_logger

logger = get_logger(__name__)

T = TypeVar("T")


def time_execution(func: Callable[..., T]) -> Callable[..., tuple[T, float]]:
    """
    Decorator to measure function execution time.

    Args:
        func: Function to time

    Returns:
        Wrapper function that returns (result, execution_time_ms)
    """

    def wrapper(*args: Any, **kwargs: Any) -> tuple[T, float]:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time_ms = (end_time - start_time) * 1000
        return result, execution_time_ms

    return wrapper


def get_file_extension(filename: str) -> str:
    """
    Get the file extension from a filename.

    Args:
        filename: Name of the file

    Returns:
        File extension (lowercase, including dot)
    """
    return Path(filename).suffix.lower()


def validate_file_extension(filename: str, allowed_extensions: list[str]) -> bool:
    """
    Validate if file extension is allowed.

    Args:
        filename: Name of the file
        allowed_extensions: List of allowed extensions

    Returns:
        True if extension is allowed, False otherwise
    """
    ext = get_file_extension(filename)
    return ext in [e.lower() for e in allowed_extensions]


def get_file_size_mb(file_size_bytes: int) -> float:
    """
    Convert file size from bytes to megabytes.

    Args:
        file_size_bytes: File size in bytes

    Returns:
        File size in megabytes
    """
    return file_size_bytes / (1024 * 1024)


def base64_to_image(base64_string: str) -> Image.Image:
    """
    Convert a base64 string to a PIL Image.

    Args:
        base64_string: Base64 encoded image string

    Returns:
        PIL Image object
    """
    # Remove data URL prefix if present
    if "," in base64_string:
        base64_string = base64_string.split(",")[1]

    image_data = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(image_data))
    logger.debug(f"Converted base64 to image: {image.size}, mode: {image.mode}")
    return image


def image_to_base64(image: Image.Image, format: str = "PNG") -> str:
    """
    Convert a PIL Image to base64 string.

    Args:
        image: PIL Image object
        format: Image format (PNG, JPEG, etc.)

    Returns:
        Base64 encoded string
    """
    buffered = io.BytesIO()
    image.save(buffered, format=format)
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def ensure_directory_exists(path: str | Path) -> Path:
    """
    Ensure a directory exists, create if it doesn't.

    Args:
        path: Directory path

    Returns:
        Path object for the directory
    """
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def format_confidence(confidence: float, decimal_places: int = 4) -> float:
    """
    Format confidence score to specified decimal places.

    Args:
        confidence: Raw confidence score
        decimal_places: Number of decimal places

    Returns:
        Formatted confidence score
    """
    return round(confidence, decimal_places)


def get_top_k_predictions(
    predictions: list[float],
    labels: dict[int, str],
    k: int = 5,
) -> list[dict[str, Any]]:
    """
    Get top k predictions with their labels and probabilities.

    Args:
        predictions: List of prediction probabilities
        labels: Dictionary mapping indices to labels
        k: Number of top predictions to return

    Returns:
        List of dictionaries with character and probability
    """
    # Get indices sorted by probability in descending order
    sorted_indices = sorted(range(len(predictions)), key=lambda i: predictions[i], reverse=True)

    top_k = []
    for i in sorted_indices[:k]:
        if i in labels:
            top_k.append(
                {
                    "character": labels[i],
                    "probability": format_confidence(predictions[i]),
                }
            )

    return top_k
