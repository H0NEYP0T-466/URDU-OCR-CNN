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

    def test_preprocess_canvas_image_inverts_colors(self):
        """
        Test that canvas images with light backgrounds are inverted.
        
        Canvas drawings typically have:
        - White background (255)
        - Black strokes (0)
        
        The model expects:
        - Dark background (~0)
        - Light strokes (~255)
        
        So the preprocessing should invert the colors.
        """
        from PIL import Image, ImageDraw

        from app.services.image_service import get_image_service

        service = get_image_service()

        # Create canvas-like image: white background with black stroke
        img = Image.new("L", (64, 64), color=255)  # White background
        draw = ImageDraw.Draw(img)
        draw.ellipse((20, 20, 44, 44), fill=0)  # Black circle

        # Get original pixel values
        original_bg = np.array(img)[0, 0]  # Corner (background) = 255
        original_stroke = np.array(img)[32, 32]  # Center (stroke) = 0

        # Process with inversion enabled (like canvas processing does)
        result = service.preprocess_image(img, "canvas.png", invert_if_light_background=True)

        # After inversion:
        # - Background should be dark (close to 0)
        # - Stroke should be light (close to 1, normalized)
        result_bg = result[0, 0, 0, 0]  # Corner (background) 
        result_stroke = result[0, 32, 32, 0]  # Center (stroke)

        # Background was white (255), after inversion should be 0
        assert result_bg == 0.0, f"Background should be 0 after inversion, got {result_bg}"
        # Stroke was black (0), after inversion should be ~1 (normalized)
        assert result_stroke == 1.0, f"Stroke should be 1 after inversion, got {result_stroke}"

    def test_base64_canvas_image_processing(self):
        """
        Test that base64 canvas images are processed correctly with inversion.
        
        This simulates the actual flow when a user draws on the canvas
        and the image is sent as base64 to the API.
        """
        import base64
        import io
        from PIL import Image, ImageDraw

        from app.services.image_service import get_image_service

        service = get_image_service()

        # Create canvas-like image: white background with black stroke
        img = Image.new("RGB", (64, 64), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.ellipse((20, 20, 44, 44), fill=(0, 0, 0))

        # Convert to base64 (simulating canvas.toDataURL())
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        base64_data = f"data:image/png;base64,{base64.b64encode(buffer.getvalue()).decode('utf-8')}"

        # Process using the same method as the API endpoint
        result = service.process_base64_image(base64_data)

        # Verify shape and range
        assert result.shape == (1, 64, 64, 1)
        assert result.dtype == np.float32
        assert result.min() >= 0
        assert result.max() <= 1

        # Verify inversion happened correctly
        result_bg = result[0, 0, 0, 0]  # Corner (background)
        result_stroke = result[0, 32, 32, 0]  # Center (stroke)

        # After inversion: background=0, stroke=1
        assert result_bg == 0.0, f"Background should be 0 after inversion, got {result_bg}"
        assert result_stroke == 1.0, f"Stroke should be 1 after inversion, got {result_stroke}"
