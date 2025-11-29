"""
Model Service

Service for loading and using the ML model for predictions.
Uses singleton pattern for model instance management.
"""

import json
import os
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any

import numpy as np

from app.config import URDU_CHARACTERS, get_settings
from app.core.exceptions import (
    ClassLabelsNotFoundError,
    ModelLoadError,
    ModelNotLoadedError,
    PredictionError,
)
from app.logger import get_logger
from app.utils.helpers import format_confidence, get_top_k_predictions

logger = get_logger(__name__)
settings = get_settings()


class ModelService:
    """
    Service for ML model management and predictions.
    Implements singleton pattern for efficient model handling.
    """

    _instance: Optional["ModelService"] = None
    _model = None
    _class_labels: Dict[int, str] = {}
    _is_loaded: bool = False

    def __new__(cls) -> "ModelService":
        """Implement singleton pattern."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """Initialize the model service."""
        # Only initialize once
        if hasattr(self, "_initialized") and self._initialized:
            return

        self._initialized = True
        logger.info("ModelService instance created")

    @property
    def is_loaded(self) -> bool:
        """Check if the model is loaded."""
        return self._is_loaded

    @property
    def model(self):
        """Get the loaded model."""
        if not self._is_loaded or self._model is None:
            raise ModelNotLoadedError()
        return self._model

    @property
    def class_labels(self) -> Dict[int, str]:
        """Get class labels."""
        if not self._class_labels:
            return URDU_CHARACTERS
        return self._class_labels

    @property
    def num_classes(self) -> int:
        """Get number of classes."""
        return len(self.class_labels)

    def load_model(self, model_path: Optional[str] = None) -> bool:
        """
        Load the trained model from file.

        Args:
            model_path: Path to the model file. Uses settings if not provided.

        Returns:
            True if model loaded successfully

        Raises:
            ModelLoadError: If model loading fails
        """
        # Import TensorFlow here to avoid import errors if not installed
        try:
            from tensorflow import keras
        except ImportError as e:
            logger.error(f"TensorFlow is not installed: {str(e)}")
            raise ModelLoadError(
                message="TensorFlow is not installed. Please install it to use the model service.",
            )

        if model_path is None:
            model_path = str(settings.model_path_resolved)

        logger.info(f"Attempting to load model from: {model_path}")

        if not os.path.exists(model_path):
            logger.warning(f"Model file not found at: {model_path}")
            logger.info("Model will need to be trained first. Using placeholder mode.")
            self._is_loaded = False
            return False

        try:
            # Log file size
            file_size = os.path.getsize(model_path)
            logger.info(f"Model file size: {file_size / 1024 / 1024:.2f} MB")

            # Load model
            self._model = keras.models.load_model(model_path)
            self._is_loaded = True

            logger.info("Model loaded successfully")
            logger.info(f"Model input shape: {self._model.input_shape}")
            logger.info(f"Model output shape: {self._model.output_shape}")

            # Log model summary
            logger.info("Model architecture summary:")
            self._model.summary(print_fn=lambda x: logger.info(x))

            # Load class labels if available
            self._load_class_labels()

            logger.info(f"Number of classes: {self.num_classes}")

            return True

        except Exception as e:
            logger.error(f"Failed to load model: {str(e)}")
            self._is_loaded = False
            raise ModelLoadError(
                message=f"Failed to load model: {str(e)}",
                model_path=model_path,
            )

    def _load_class_labels(self, labels_path: Optional[str] = None) -> None:
        """
        Load class labels from JSON file.

        Args:
            labels_path: Path to class labels JSON file
        """
        if labels_path is None:
            labels_path = str(settings.class_labels_path_resolved)

        logger.info(f"Attempting to load class labels from: {labels_path}")

        if not os.path.exists(labels_path):
            logger.warning(f"Class labels file not found at: {labels_path}")
            logger.info("Using default Urdu character mappings")
            self._class_labels = URDU_CHARACTERS
            return

        try:
            with open(labels_path, "r", encoding="utf-8") as f:
                labels = json.load(f)

            # Convert string keys to integers
            self._class_labels = {int(k): v for k, v in labels.items()}
            logger.info(f"Loaded {len(self._class_labels)} class labels")

        except Exception as e:
            logger.warning(f"Failed to load class labels: {str(e)}")
            logger.info("Using default Urdu character mappings")
            self._class_labels = URDU_CHARACTERS

    def predict(self, image_array: np.ndarray) -> Tuple[str, float, List[Dict[str, Any]], float]:
        """
        Make a prediction on a preprocessed image.

        Args:
            image_array: Preprocessed image array with shape (1, 64, 64, 1)

        Returns:
            Tuple of (prediction, confidence, top_5_predictions, processing_time_ms)

        Raises:
            ModelNotLoadedError: If model is not loaded
            PredictionError: If prediction fails
        """
        if not self._is_loaded or self._model is None:
            logger.error("Prediction attempted without loaded model")
            raise ModelNotLoadedError()

        logger.info(f"Making prediction on image with shape: {image_array.shape}")

        try:
            start_time = time.perf_counter()

            # Make prediction
            predictions = self._model.predict(image_array, verbose=0)
            prediction_probs = predictions[0].tolist()

            end_time = time.perf_counter()
            processing_time_ms = (end_time - start_time) * 1000

            # Get top prediction
            top_index = int(np.argmax(predictions[0]))
            confidence = float(predictions[0][top_index])
            prediction = self.class_labels.get(top_index, "Unknown")

            # Get top 5 predictions
            top_5 = get_top_k_predictions(prediction_probs, self.class_labels, k=5)

            logger.info(f"Prediction completed - Character: {prediction}, Confidence: {confidence:.4f}")
            logger.info(f"Processing time: {processing_time_ms:.2f}ms")
            logger.debug(f"Top 5 predictions: {top_5}")

            return prediction, format_confidence(confidence), top_5, processing_time_ms

        except Exception as e:
            logger.error(f"Prediction failed: {str(e)}")
            raise PredictionError(
                message=f"Prediction failed: {str(e)}",
                original_error=str(e),
            )

    def get_classes(self) -> List[str]:
        """
        Get list of all character classes.

        Returns:
            List of Urdu characters
        """
        return list(self.class_labels.values())

    def unload_model(self) -> None:
        """Unload the model to free memory."""
        logger.info("Unloading model...")
        self._model = None
        self._is_loaded = False
        logger.info("Model unloaded")


# Singleton instance
model_service = ModelService()


def get_model_service() -> ModelService:
    """Get the model service instance."""
    return model_service
