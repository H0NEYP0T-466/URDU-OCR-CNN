# Urdu Character Recognition

<div align="center">

![Urdu OCR](https://img.shields.io/badge/Urdu-OCR-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-green?style=for-the-badge&logo=python)
![React](https://img.shields.io/badge/React-18+-61DAFB?style=for-the-badge&logo=react)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-FF6F00?style=for-the-badge&logo=tensorflow)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688?style=for-the-badge&logo=fastapi)

A full-stack web application for recognizing handwritten Urdu characters using Convolutional Neural Networks (CNN).

</div>

## 📝 Description

This application uses deep learning to recognize handwritten Urdu alphabets and digits. Users can either upload images of handwritten characters or draw them directly on a canvas. The CNN model analyzes the input and provides predictions with confidence scores.

## ✨ Features

- 🖼️ **Image Upload**: Drag and drop or click to upload images
- ✏️ **Drawing Canvas**: Draw characters directly in the browser
- 🧠 **AI-Powered**: CNN model for accurate character recognition
- ⚡ **Fast Predictions**: Results in milliseconds
- 📊 **Top-5 Predictions**: View confidence scores for top predictions
- 🌐 **RESTful API**: Well-documented API endpoints
- 📱 **Responsive Design**: Works on desktop and mobile
- 🎨 **Modern UI**: Built with TailwindCSS

## 🔤 Supported Characters

### Urdu Alphabets (36)
```
ا ب پ ت ٹ ث ج چ ح خ د ڈ ذ ر ڑ ز ژ س ش ص ض ط ظ ع غ ف ق ک گ ل م ن و ہ ی ے
```

### Urdu Digits (10)
```
۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹
```

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI
- **ML/DL**: TensorFlow/Keras
- **Image Processing**: OpenCV, Pillow
- **Server**: Uvicorn
- **Testing**: Pytest

### Frontend
- **Framework**: React 18
- **Language**: TypeScript
- **Build Tool**: Vite
- **Styling**: TailwindCSS
- **HTTP Client**: Axios
- **Testing**: Vitest

## 📁 Project Structure

```
urdu-character-recognition/
│
├── README.md
├── .gitignore
├── docker-compose.yml
│
├── backend/
│   ├── app/
│   │   ├── main.py                 # FastAPI entry point
│   │   ├── config.py               # Configuration
│   │   ├── logger.py               # Custom logger
│   │   ├── api/
│   │   │   ├── dependencies.py
│   │   │   └── routes/
│   │   │       ├── prediction.py
│   │   │       └── health.py
│   │   ├── models/
│   │   │   ├── cnn_model.py
│   │   │   └── schemas.py
│   │   ├── services/
│   │   │   ├── model_service.py
│   │   │   └── image_service.py
│   │   ├── utils/
│   │   │   └── helpers.py
│   │   └── core/
│   │       └── exceptions.py
│   ├── ml/
│   │   ├── train.py
│   │   ├── evaluate.py
│   │   ├── preprocess.py
│   │   └── augmentation.py
│   ├── data/
│   │   ├── raw/
│   │   └── processed/
│   ├── saved_models/
│   ├── logs/
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ImageUploader.tsx
│   │   │   ├── DrawingCanvas.tsx
│   │   │   ├── PredictionResult.tsx
│   │   │   ├── Header.tsx
│   │   │   ├── Footer.tsx
│   │   │   └── LoadingSpinner.tsx
│   │   ├── pages/
│   │   │   ├── HomePage.tsx
│   │   │   ├── AboutPage.tsx
│   │   │   └── HowItWorksPage.tsx
│   │   ├── services/
│   │   │   └── api.ts
│   │   ├── hooks/
│   │   │   └── usePrediction.ts
│   │   ├── types/
│   │   │   └── index.ts
│   │   └── utils/
│   │       └── imageUtils.ts
│   ├── package.json
│   ├── vite.config.ts
│   ├── tailwind.config.js
│   └── Dockerfile
│
└── docs/
    ├── API.md
    ├── MODEL.md
    └── SETUP.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- npm or yarn

### Installation

#### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env
```

#### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Copy environment file
cp .env.example .env
```

### Running the Application

#### Development Mode

**Backend:**
```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd frontend
npm run dev
```

**Access:**
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

#### Using Docker

```bash
# Build and run
docker-compose up --build

# Run in background
docker-compose up -d
```

## 📊 Training the Model

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

### 2. Train

```bash
cd backend
python -m ml.train
```

### 3. Evaluate

```bash
python -m ml.evaluate
```

## 📚 Datasets

### Recommended Datasets

1. **UNHD Dataset** (Urdu Nastaliq Handwritten Dataset)
   - URL: https://github.com/Wikipedia-Urdu/UNHD-Dataset
   - Contains: Urdu characters in Nastaliq script

2. **UCOM Offline Dataset**
   - URL: https://drive.google.com/drive/folders/1K7rKt7e2oKnCQwP9g3UG5MQxkj_JjvZl
   - Research paper: Search for "UCOM Urdu Character Dataset"

3. **Urdu-Handwritten-Characters Dataset (Kaggle)**
   - URL: https://www.kaggle.com/datasets/hazratali/urdu-handwritten-characters-dataset
   - Contains: 38 classes of Urdu characters

4. **CALAM Dataset**
   - URL: Contact researchers at FAST-NUCES Pakistan
   - Contains: Comprehensive Urdu handwriting samples

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/` | Welcome message |
| POST | `/api/v1/predict` | Predict from image upload |
| POST | `/api/v1/predict/canvas` | Predict from canvas drawing |
| GET | `/api/v1/classes` | Get supported characters |

### Example API Call

```bash
curl -X POST "http://localhost:8000/api/v1/predict" \
  -F "file=@path/to/image.png"
```

## 🧪 Testing

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

## 📖 Documentation

- [API Documentation](docs/API.md)
- [Model Architecture](docs/MODEL.md)
- [Setup Instructions](docs/SETUP.md)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- TensorFlow/Keras team for the deep learning framework
- FastAPI team for the excellent web framework
- React team for the frontend library
- All contributors to the Urdu handwritten character datasets

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

<div align="center">
Built with ❤️ for the Urdu language
</div>
