# API Documentation

## Overview

The Urdu Character Recognition API provides endpoints for predicting handwritten Urdu characters using a Convolutional Neural Network (CNN).

**Base URL**: `http://localhost:8000`

**API Version**: `v1`

## Authentication

Currently, the API does not require authentication.

## Endpoints

### Health Check

#### GET `/health`

Check the API health status.

**Response**:
```json
{
  "status": "healthy",
  "model_loaded": true,
  "version": "1.0.0"
}
```

#### GET `/`

Root endpoint with welcome message.

**Response**:
```json
{
  "message": "Welcome to the Urdu Character Recognition API",
  "version": "1.0.0",
  "docs": "/docs"
}
```

---

### Prediction

#### POST `/api/v1/predict`

Predict Urdu character from an uploaded image file.

**Request**:
- Content-Type: `multipart/form-data`
- Body: `file` - Image file (PNG, JPG, JPEG, BMP), max 5MB

**Example using cURL**:
```bash
curl -X POST "http://localhost:8000/api/v1/predict" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@path/to/image.png"
```

**Response** (200 OK):
```json
{
  "prediction": "ا",
  "confidence": 0.95,
  "top_5": [
    {"character": "ا", "probability": 0.95},
    {"character": "ب", "probability": 0.02},
    {"character": "پ", "probability": 0.01},
    {"character": "ت", "probability": 0.01},
    {"character": "ٹ", "probability": 0.01}
  ],
  "processing_time_ms": 45.23
}
```

**Error Responses**:

- `400 Bad Request`: Invalid image format or file too large
- `500 Internal Server Error`: Prediction error
- `503 Service Unavailable`: Model not loaded

---

#### POST `/api/v1/predict/canvas`

Predict Urdu character from a canvas drawing (base64 encoded).

**Request**:
- Content-Type: `application/json`
- Body:
```json
{
  "image_data": "data:image/png;base64,..."
}
```

**Example using cURL**:
```bash
curl -X POST "http://localhost:8000/api/v1/predict/canvas" \
  -H "Content-Type: application/json" \
  -d '{"image_data": "data:image/png;base64,iVBORw0KGgo..."}'
```

**Response** (200 OK):
Same as `/api/v1/predict`

---

### Classes

#### GET `/api/v1/classes`

Get list of all Urdu characters the model can recognize.

**Response**:
```json
{
  "classes": ["ا", "ب", "پ", "ت", "ٹ", "ث", "..."],
  "count": 46
}
```

---

## Error Handling

All error responses follow this format:

```json
{
  "detail": "Error message",
  "error_type": "ErrorTypeName"
}
```

### Error Types

| Error Type | Status Code | Description |
|------------|-------------|-------------|
| `InvalidImageError` | 400 | Image cannot be processed |
| `UnsupportedImageFormatError` | 400 | File format not supported |
| `ImageTooLargeError` | 400 | File exceeds 5MB limit |
| `ImageProcessingError` | 500 | Error during preprocessing |
| `ModelNotLoadedError` | 503 | Model not available |
| `PredictionError` | 500 | Error during prediction |

---

## Rate Limiting

Currently, there are no rate limits implemented. For production use, consider adding rate limiting.

---

## Interactive Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
