"""
Model Tests

Tests for the CNN model and model service.
"""

from unittest.mock import MagicMock, patch

import numpy as np
import pytest


class TestCNNModel:
    """Tests for CNN model architecture."""

    def test_create_model_default_params(self):
        """Test model creation with default parameters."""
        with patch("app.models.cnn_model.logger"):
            from app.models.cnn_model import create_cnn_model

            model = create_cnn_model()

            assert model is not None
            assert model.input_shape == (None, 64, 64, 1)
            assert model.output_shape == (None, 46)

    def test_create_model_custom_params(self):
        """Test model creation with custom parameters."""
        with patch("app.models.cnn_model.logger"):
            from app.models.cnn_model import create_cnn_model

            model = create_cnn_model(
                input_shape=(32, 32, 1),
                num_classes=38,
            )

            assert model is not None
            assert model.input_shape == (None, 32, 32, 1)
            assert model.output_shape == (None, 38)

    def test_compile_model(self):
        """Test model compilation."""
        with patch("app.models.cnn_model.logger"):
            from app.models.cnn_model import compile_model, create_cnn_model

            model = create_cnn_model()
            compiled_model = compile_model(model)

            assert compiled_model.optimizer is not None


class TestModelService:
    """Tests for model service."""

    def test_model_service_singleton(self):
        """Test that model service is a singleton."""
        from app.services.model_service import ModelService

        service1 = ModelService()
        service2 = ModelService()

        assert service1 is service2

    def test_get_classes(self):
        """Test getting character classes."""
        from app.services.model_service import get_model_service

        service = get_model_service()
        classes = service.get_classes()

        assert isinstance(classes, list)
        assert len(classes) > 0
        assert "ا" in classes  # Alif should be in the list


class TestImageService:
    """Tests for image service."""

    def test_validate_file_valid_extension(self):
        """Test file validation with valid extension."""
        from app.services.image_service import get_image_service

        service = get_image_service()

        # Should not raise exception
        service.validate_file("test.png", 1000)
        service.validate_file("test.jpg", 1000)
        service.validate_file("test.jpeg", 1000)

    def test_validate_file_invalid_extension(self):
        """Test file validation with invalid extension."""
        from app.core.exceptions import UnsupportedImageFormatError
        from app.services.image_service import get_image_service

        service = get_image_service()

        with pytest.raises(UnsupportedImageFormatError):
            service.validate_file("test.gif", 1000)

    def test_validate_file_too_large(self):
        """Test file validation with file too large."""
        from app.core.exceptions import ImageTooLargeError
        from app.services.image_service import get_image_service

        service = get_image_service()

        with pytest.raises(ImageTooLargeError):
            service.validate_file("test.png", 10 * 1024 * 1024)  # 10MB

    def test_preprocess_image(self):
        """Test image preprocessing."""
        from PIL import Image

        from app.services.image_service import get_image_service

        service = get_image_service()

        # Create test image
        img = Image.new("RGB", (100, 100), color=(128, 128, 128))
        result = service.preprocess_image(img, "test.png")

        assert result.shape == (1, 64, 64, 1)
        assert result.dtype == np.float32
        assert result.min() >= 0
        assert result.max() <= 1
