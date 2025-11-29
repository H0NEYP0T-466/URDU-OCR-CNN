# Setup Instructions

## Prerequisites

- **Python**: 3.10 or higher
- **Node.js**: 18 or higher
- **npm**: 8 or higher
- **Git**: For version control

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/urdu-character-recognition.git
cd urdu-character-recognition
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment variables
cp .env.example .env
```

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Copy environment variables
cp .env.example .env
```

## Running the Application

### Development Mode

**Start the Backend:**
```bash
cd backend
source venv/bin/activate  # Activate venv if not already
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Start the Frontend:**
```bash
cd frontend
npm run dev
```

**Access the Application:**
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

### Using Docker Compose

```bash
# Build and start all services
docker-compose up --build

# Run in background
docker-compose up -d

# Stop services
docker-compose down
```

## Training the Model

### 1. Prepare Dataset

Download an Urdu handwritten character dataset and place it in `backend/data/raw/`:

```
backend/data/raw/
├── alif/
│   ├── img001.png
│   └── ...
├── bay/
│   ├── img001.png
│   └── ...
└── ...
```

### 2. Run Training

```bash
cd backend
python -m ml.train
```

### Training Options

```bash
python -m ml.train \
  --data-dir data/raw \
  --model-path saved_models/urdu_cnn_model.h5 \
  --batch-size 32 \
  --epochs 100 \
  --lr 0.001
```

### 3. Evaluate Model

```bash
cd backend
python -m ml.evaluate
```

## Dataset Sources

### Recommended Datasets

1. **UNHD Dataset** (Urdu Nastaliq Handwritten Dataset)
   - URL: https://github.com/Wikipedia-Urdu/UNHD-Dataset

2. **UCOM Offline Dataset**
   - URL: https://drive.google.com/drive/folders/1K7rKt7e2oKnCQwP9g3UG5MQxkj_JjvZl

3. **Kaggle Urdu Dataset**
   - URL: https://www.kaggle.com/datasets/hazratali/urdu-handwritten-characters-dataset

### Dataset Format

- Each class should be in a separate folder
- Folder name should represent the character (e.g., "alif", "bay")
- Images should be in PNG, JPG, JPEG, or BMP format
- Recommended image size: 64×64 pixels or larger

## Environment Variables

### Backend (.env)

```env
APP_NAME=Urdu Character Recognition API
VERSION=1.0.0
DEBUG=false
ENVIRONMENT=development
MODEL_PATH=saved_models/urdu_cnn_model.h5
CLASS_LABELS_PATH=saved_models/class_labels.json
MAX_FILE_SIZE=5242880
LOG_LEVEL=INFO
LOG_FILE=logs/app.log
CORS_ORIGINS=["http://localhost:5173", "http://localhost:3000"]
HOST=0.0.0.0
PORT=8000
```

### Frontend (.env)

```env
VITE_API_URL=http://localhost:8000
```

## Troubleshooting

### Common Issues

**1. TensorFlow not found**
```bash
pip install tensorflow
```

**2. CORS errors**
Ensure the frontend URL is in `CORS_ORIGINS` in backend `.env`

**3. Model not found**
Train a model first or create a demo model:
```bash
cd backend
python -m ml.train
```

**4. Port already in use**
```bash
# Kill process on port 8000
kill -9 $(lsof -t -i:8000)
# Or use different port
uvicorn app.main:app --port 8001
```

### Checking Logs

Backend logs are stored in `backend/logs/app.log`

```bash
tail -f backend/logs/app.log
```

## Running Tests

### Backend Tests

```bash
cd backend
pytest tests/ -v
```

### Frontend Tests

```bash
cd frontend
npm run test
```

## Building for Production

### Backend

```bash
cd backend
docker build -t urdu-ocr-backend .
```

### Frontend

```bash
cd frontend
npm run build
docker build -t urdu-ocr-frontend .
```

## Need Help?

- Check the API documentation at `/docs`
- Review the model documentation in `docs/MODEL.md`
- Open an issue on GitHub
