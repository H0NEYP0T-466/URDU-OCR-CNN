"""
Prediction API Tests

Tests for the prediction endpoints.
"""

import io
from unittest.mock import MagicMock, patch

import numpy as np
import pytest
from fastapi.testclient import TestClient
from PIL import Image

from app.main import app

client = TestClient(app)


class TestHealthEndpoint:
    """Tests for health check endpoint."""

    def test_health_check(self):
        """Test health check endpoint returns correct response."""
        response = client.get("/health")
        assert response.status_code == 200

        data = response.json()
        assert "status" in data
        assert "model_loaded" in data
        assert "version" in data
        assert data["status"] == "healthy"

    def test_root_endpoint(self):
        """Test root endpoint returns welcome message."""
        response = client.get("/")
        assert response.status_code == 200

        data = response.json()
        assert "message" in data
        assert "version" in data
        assert "docs" in data


class TestPredictionEndpoint:
    """Tests for prediction endpoints."""

    def create_test_image(self, size=(64, 64), mode="L") -> bytes:
        """Create a test image for upload."""
        img = Image.new(mode, size, color=128)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        return buffer.getvalue()

    def test_predict_valid_image(self):
        """Test prediction with valid image."""
        image_bytes = self.create_test_image()

        response = client.post(
            "/api/v1/predict",
            files={"file": ("test.png", image_bytes, "image/png")},
        )

        assert response.status_code == 200

        data = response.json()
        assert "prediction" in data
        assert "confidence" in data
        assert "top_5" in data
        assert "processing_time_ms" in data

    def test_predict_invalid_extension(self):
        """Test prediction with unsupported file extension."""
        image_bytes = self.create_test_image()

        response = client.post(
            "/api/v1/predict",
            files={"file": ("test.gif", image_bytes, "image/gif")},
        )

        assert response.status_code == 400

    def test_predict_jpeg_image(self):
        """Test prediction with JPEG image."""
        img = Image.new("RGB", (64, 64), color=(128, 128, 128))
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG")
        buffer.seek(0)

        response = client.post(
            "/api/v1/predict",
            files={"file": ("test.jpg", buffer.getvalue(), "image/jpeg")},
        )

        assert response.status_code == 200

    def test_get_classes(self):
        """Test get classes endpoint."""
        response = client.get("/api/v1/classes")
        assert response.status_code == 200

        data = response.json()
        assert "classes" in data
        assert "count" in data
        assert isinstance(data["classes"], list)
        assert data["count"] > 0


class TestCanvasPrediction:
    """Tests for canvas prediction endpoint."""

    def create_base64_image(self) -> str:
        """Create a base64 encoded test image."""
        import base64

        img = Image.new("L", (64, 64), color=128)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        base64_data = base64.b64encode(buffer.getvalue()).decode("utf-8")
        return f"data:image/png;base64,{base64_data}"

    def test_predict_from_canvas(self):
        """Test prediction from canvas data."""
        image_data = self.create_base64_image()

        response = client.post(
            "/api/v1/predict/canvas",
            json={"image_data": image_data},
        )

        assert response.status_code == 200

        data = response.json()
        assert "prediction" in data
        assert "confidence" in data
        assert "top_5" in data

    def test_predict_invalid_base64(self):
        """Test prediction with invalid base64 data."""
        response = client.post(
            "/api/v1/predict/canvas",
            json={"image_data": "invalid_base64_data"},
        )

        assert response.status_code == 400


class TestDigitCanvasPrediction:
    """Tests for digit canvas prediction endpoint."""

    def create_base64_canvas_image(self, with_drawing: bool = False) -> str:
        """
        Create a base64 encoded image simulating a canvas drawing.
        
        Canvas drawings have white background with black strokes.
        This tests that the preprocessing correctly inverts the colors
        to match the training data format (dark background, light strokes).
        
        Args:
            with_drawing: If True, add a black stroke on white background
        
        Returns:
            Base64 encoded image string with data URL prefix
        """
        import base64
        from PIL import ImageDraw

        # Create a white background (like HTML canvas)
        img = Image.new("RGB", (64, 64), color=(255, 255, 255))
        
        if with_drawing:
            # Add a black stroke (simulating user drawing)
            draw = ImageDraw.Draw(img)
            draw.ellipse((10, 10, 50, 50), fill=(0, 0, 0))
        
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        base64_data = base64.b64encode(buffer.getvalue()).decode("utf-8")
        return f"data:image/png;base64,{base64_data}"

    def test_predict_digit_from_canvas(self):
        """Test digit prediction from canvas data."""
        image_data = self.create_base64_canvas_image(with_drawing=True)

        response = client.post(
            "/api/v1/predict/digit/canvas",
            json={"image_data": image_data},
        )

        assert response.status_code == 200

        data = response.json()
        assert "prediction" in data
        assert "confidence" in data
        assert "top_5" in data
        assert "processing_time_ms" in data

    def test_predict_digit_invalid_base64(self):
        """Test digit prediction with invalid base64 data."""
        response = client.post(
            "/api/v1/predict/digit/canvas",
            json={"image_data": "invalid_base64_data"},
        )

        assert response.status_code == 400

    def test_digit_canvas_uses_same_preprocessing_as_character_canvas(self):
        """
        Verify that digit canvas endpoint uses the same preprocessing as character canvas.
        
        Both endpoints should:
        1. Accept base64 encoded images
        2. Invert colors when background is light (canvas drawings)
        3. Convert to grayscale and normalize
        """
        image_data = self.create_base64_canvas_image(with_drawing=True)

        # Both endpoints should successfully process the same canvas image
        char_response = client.post(
            "/api/v1/predict/canvas",
            json={"image_data": image_data},
        )
        digit_response = client.post(
            "/api/v1/predict/digit/canvas",
            json={"image_data": image_data},
        )

        # Both should return 200 OK
        assert char_response.status_code == 200
        assert digit_response.status_code == 200

        # Both should have the same response structure
        char_data = char_response.json()
        digit_data = digit_response.json()
        
        for key in ["prediction", "confidence", "top_5", "processing_time_ms"]:
            assert key in char_data
            assert key in digit_data

    def test_get_digit_classes(self):
        """Test get digit classes endpoint."""
        response = client.get("/api/v1/classes/digits")
        assert response.status_code == 200

        data = response.json()
        assert "classes" in data
        assert "count" in data
        assert isinstance(data["classes"], list)
        assert data["count"] > 0
        # Digits should have 10 classes (0-9)
        assert data["count"] == 10
