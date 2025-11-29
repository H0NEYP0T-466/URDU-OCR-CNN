"""
Image Service

Service for image preprocessing and validation.
"""

import io
from pathlib import Path
from typing import Tuple, Optional

import cv2
import numpy as np
from PIL import Image

from app.config import get_settings
from app.core.exceptions import (
    ImageProcessingError,
    ImageTooLargeError,
    InvalidImageError,
    UnsupportedImageFormatError,
)
from app.logger import get_logger
from app.utils.helpers import base64_to_image, get_file_extension

logger = get_logger(__name__)
settings = get_settings()


class ImageService:
    """Service for image preprocessing and validation."""

    def __init__(
        self,
        target_size: Tuple[int, int] = (64, 64),
        allowed_extensions: Optional[list] = None,
        max_file_size: Optional[int] = None,
    ) -> None:
        """
        Initialize the image service.

        Args:
            target_size: Target size for preprocessed images (width, height)
            allowed_extensions: List of allowed file extensions
            max_file_size: Maximum file size in bytes
        """
        self.target_size = target_size
        self.allowed_extensions = allowed_extensions or settings.ALLOWED_EXTENSIONS
        self.max_file_size = max_file_size or settings.MAX_FILE_SIZE

        logger.info(f"ImageService initialized with target size: {self.target_size}")
        logger.info(f"Allowed extensions: {self.allowed_extensions}")
        logger.info(f"Max file size: {self.max_file_size / (1024 * 1024):.2f} MB")

    def validate_file(self, filename: str, file_size: int) -> None:
        """
        Validate file extension and size.

        Args:
            filename: Name of the file
            file_size: Size of the file in bytes

        Raises:
            UnsupportedImageFormatError: If file extension is not allowed
            ImageTooLargeError: If file size exceeds limit
        """
        # Validate extension
        ext = get_file_extension(filename)
        if ext not in [e.lower() for e in self.allowed_extensions]:
            logger.warning(f"Unsupported file format: {ext} for file: {filename}")
            raise UnsupportedImageFormatError(
                message=f"Unsupported image format: {ext}",
                format=ext,
                supported_formats=self.allowed_extensions,
            )

        # Validate file size
        if file_size > self.max_file_size:
            logger.warning(
                f"File too large: {file_size / (1024 * 1024):.2f} MB, "
                f"max allowed: {self.max_file_size / (1024 * 1024):.2f} MB"
            )
            raise ImageTooLargeError(
                message=f"File size ({file_size / (1024 * 1024):.2f} MB) exceeds maximum allowed size",
                file_size=file_size,
                max_size=self.max_file_size,
            )

        logger.info(f"File validation passed for: {filename}")

    def preprocess_image(
        self,
        image: Image.Image,
        filename: str = "unknown",
    ) -> np.ndarray:
        """
        Preprocess an image for model prediction.

        Steps:
        1. Convert to grayscale
        2. Resize to target size
        3. Normalize pixel values (0-1)
        4. Add batch dimension

        Args:
            image: PIL Image object
            filename: Filename for logging purposes

        Returns:
            Preprocessed numpy array ready for prediction

        Raises:
            ImageProcessingError: If preprocessing fails
        """
        logger.info(f"Preprocessing image: {filename}")
        logger.info(f"Original size: {image.size}, mode: {image.mode}")

        try:
            # Convert to grayscale
            if image.mode != "L":
                image = image.convert("L")
                logger.debug("Converted image to grayscale")

            # Resize to target size
            image = image.resize(self.target_size, Image.Resampling.LANCZOS)
            logger.debug(f"Resized image to: {self.target_size}")

            # Convert to numpy array
            img_array = np.array(image, dtype=np.float32)

            # Normalize pixel values to [0, 1]
            img_array = img_array / 255.0
            logger.debug("Normalized pixel values to [0, 1]")

            # Add channel dimension (64, 64) -> (64, 64, 1)
            img_array = np.expand_dims(img_array, axis=-1)

            # Add batch dimension (64, 64, 1) -> (1, 64, 64, 1)
            img_array = np.expand_dims(img_array, axis=0)

            logger.info("Image preprocessing completed")
            logger.debug(f"Final shape: {img_array.shape}")

            return img_array

        except Exception as e:
            logger.error(f"Error during image preprocessing: {str(e)}")
            raise ImageProcessingError(
                message=f"Failed to preprocess image: {str(e)}",
                step="preprocessing",
            )

    async def process_uploaded_file(
        self,
        file_content: bytes,
        filename: str,
    ) -> np.ndarray:
        """
        Process an uploaded file for prediction.

        Args:
            file_content: Raw file content bytes
            filename: Name of the uploaded file

        Returns:
            Preprocessed numpy array

        Raises:
            InvalidImageError: If file cannot be opened as image
        """
        logger.info(f"Processing uploaded file: {filename}, size: {len(file_content)} bytes")

        try:
            # Open image from bytes
            image = Image.open(io.BytesIO(file_content))
            logger.debug(f"Opened image: {image.format}, {image.size}, {image.mode}")

            return self.preprocess_image(image, filename)

        except Exception as e:
            if isinstance(e, (ImageProcessingError,)):
                raise
            logger.error(f"Failed to open image file: {str(e)}")
            raise InvalidImageError(
                message=f"Failed to open image file: {str(e)}",
                filename=filename,
            )

    def process_base64_image(self, base64_string: str) -> np.ndarray:
        """
        Process a base64 encoded image for prediction.

        Args:
            base64_string: Base64 encoded image string

        Returns:
            Preprocessed numpy array

        Raises:
            InvalidImageError: If base64 string is invalid
        """
        logger.info("Processing base64 encoded image")

        try:
            image = base64_to_image(base64_string)
            return self.preprocess_image(image, "canvas_image")

        except Exception as e:
            if isinstance(e, (ImageProcessingError,)):
                raise
            logger.error(f"Failed to process base64 image: {str(e)}")
            raise InvalidImageError(
                message=f"Failed to process base64 image: {str(e)}",
            )


# Singleton instance
image_service = ImageService()


def get_image_service() -> ImageService:
    """Get the image service instance."""
    return image_service
