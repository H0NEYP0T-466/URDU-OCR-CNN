# URDU-OCR-CNN

<p align="center">

  <!-- Core -->
  ![GitHub License](https://img.shields.io/github/license/H0NEYP0T-466/URDU-OCR-CNN?style=for-the-badge&color=brightgreen)
  ![GitHub Stars](https://img.shields.io/github/stars/H0NEYP0T-466/URDU-OCR-CNN?style=for-the-badge&color=yellow)
  ![GitHub Forks](https://img.shields.io/github/forks/H0NEYP0T-466/URDU-OCR-CNN?style=for-the-badge&color=blue)
  ![GitHub Issues](https://img.shields.io/github/issues/H0NEYP0T-466/URDU-OCR-CNN?style=for-the-badge&color=red)
  ![GitHub Pull Requests](https://img.shields.io/github/issues-pr/H0NEYP0T-466/URDU-OCR-CNN?style=for-the-badge&color=orange)
  ![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge)

  <!-- Activity -->
  ![Last Commit](https://img.shields.io/github/last-commit/H0NEYP0T-466/URDU-OCR-CNN?style=for-the-badge&color=purple)
  ![Commit Activity](https://img.shields.io/github/commit-activity/m/H0NEYP0T-466/URDU-OCR-CNN?style=for-the-badge&color=teal)
  ![Repo Size](https://img.shields.io/github/repo-size/H0NEYP0T-466/URDU-OCR-CNN?style=for-the-badge&color=blueviolet)
  ![Code Size](https://img.shields.io/github/languages/code-size/H0NEYP0T-466/URDU-OCR-CNN?style=for-the-badge&color=indigo)

  <!-- Languages -->
  ![Top Language](https://img.shields.io/github/languages/top/H0NEYP0T-466/URDU-OCR-CNN?style=for-the-badge&color=critical)
  ![Languages Count](https://img.shields.io/github/languages/count/H0NEYP0T-466/URDU-OCR-CNN?style=for-the-badge&color=success)

  <!-- Community -->
  ![Documentation](https://img.shields.io/badge/Docs-Available-green?style=for-the-badge&logo=readthedocs&logoColor=white)
  ![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red?style=for-the-badge)

</p>

<div align="center">

A full-stack web application for recognizing handwritten Urdu characters using Convolutional Neural Networks (CNN).

</div>

## 🔗 Quick Links

- [📖 Documentation](docs/)
- [🐛 Report Bug](https://github.com/H0NEYP0T-466/URDU-OCR-CNN/issues/new?template=bug_report.yml)
- [💡 Request Feature](https://github.com/H0NEYP0T-466/URDU-OCR-CNN/issues/new?template=feature_request.yml)
- [🤝 Contributing Guide](CONTRIBUTING.md)

---

## 📑 Table of Contents

- [📝 Description](#-description)
- [✨ Features](#-features)
- [🔤 Supported Characters](#-supported-characters)
- [🛠️ Tech Stack](#️-tech-stack)
- [📦 Dependencies & Packages](#-dependencies--packages)
- [📁 Project Structure](#-project-structure)
- [🚀 Getting Started](#-getting-started)
- [📊 Training the Model](#-training-the-model)
- [📚 Datasets](#-datasets)
- [🔌 API Endpoints](#-api-endpoints)
- [🧪 Testing](#-testing)
- [📖 Documentation](#-documentation)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [🛡 Security](#-security)
- [📏 Code of Conduct](#-code-of-conduct)
- [🙏 Acknowledgments](#-acknowledgments)

---

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
- 🎨 **Modern UI**: Built with custom CSS styling

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

### Languages
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)

### Frameworks & Libraries

**Backend:**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![scikit--learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

**Frontend:**

![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![Axios](https://img.shields.io/badge/Axios-5A29E4?style=for-the-badge&logo=axios&logoColor=white)

### DevOps / CI / Tools
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

### Testing
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Vitest](https://img.shields.io/badge/Vitest-6E9F18?style=for-the-badge&logo=vitest&logoColor=white)

---

## 📦 Dependencies & Packages

<details>
<summary><b>Backend Runtime Dependencies</b></summary>

### Web Framework & Server
[![fastapi](https://img.shields.io/pypi/v/fastapi?style=for-the-badge&label=fastapi&color=009688)](https://pypi.org/project/fastapi/)
[![uvicorn](https://img.shields.io/pypi/v/uvicorn?style=for-the-badge&label=uvicorn&color=2196F3)](https://pypi.org/project/uvicorn/)
[![python-multipart](https://img.shields.io/pypi/v/python-multipart?style=for-the-badge&label=python-multipart&color=4CAF50)](https://pypi.org/project/python-multipart/)

### Machine Learning & Data Science
[![tensorflow](https://img.shields.io/pypi/v/tensorflow?style=for-the-badge&label=tensorflow&color=FF6F00)](https://pypi.org/project/tensorflow/)
[![numpy](https://img.shields.io/pypi/v/numpy?style=for-the-badge&label=numpy&color=013243)](https://pypi.org/project/numpy/)
[![scikit-learn](https://img.shields.io/pypi/v/scikit-learn?style=for-the-badge&label=scikit-learn&color=F7931E)](https://pypi.org/project/scikit-learn/)
[![matplotlib](https://img.shields.io/pypi/v/matplotlib?style=for-the-badge&label=matplotlib&color=11557c)](https://pypi.org/project/matplotlib/)
[![seaborn](https://img.shields.io/pypi/v/seaborn?style=for-the-badge&label=seaborn&color=76b7b2)](https://pypi.org/project/seaborn/)

### Image Processing
[![opencv-python](https://img.shields.io/pypi/v/opencv-python?style=for-the-badge&label=opencv-python&color=5C3EE8)](https://pypi.org/project/opencv-python/)
[![pillow](https://img.shields.io/pypi/v/pillow?style=for-the-badge&label=pillow&color=FFD43B)](https://pypi.org/project/pillow/)

### Configuration & Validation
[![python-dotenv](https://img.shields.io/pypi/v/python-dotenv?style=for-the-badge&label=python-dotenv&color=ECD53F)](https://pypi.org/project/python-dotenv/)
[![pydantic](https://img.shields.io/pypi/v/pydantic?style=for-the-badge&label=pydantic&color=E92063)](https://pypi.org/project/pydantic/)
[![pydantic-settings](https://img.shields.io/pypi/v/pydantic-settings?style=for-the-badge&label=pydantic-settings&color=E92063)](https://pypi.org/project/pydantic-settings/)

### Testing
[![pytest](https://img.shields.io/pypi/v/pytest?style=for-the-badge&label=pytest&color=0A9EDC)](https://pypi.org/project/pytest/)
[![httpx](https://img.shields.io/pypi/v/httpx?style=for-the-badge&label=httpx&color=0052CC)](https://pypi.org/project/httpx/)

</details>

<details>
<summary><b>Frontend Dependencies</b></summary>

### Runtime Dependencies
[![axios](https://img.shields.io/npm/v/axios?style=for-the-badge&label=axios&color=5A29E4)](https://www.npmjs.com/package/axios)
[![react](https://img.shields.io/npm/v/react?style=for-the-badge&label=react&color=61DAFB)](https://www.npmjs.com/package/react)
[![react-dom](https://img.shields.io/npm/v/react-dom?style=for-the-badge&label=react-dom&color=61DAFB)](https://www.npmjs.com/package/react-dom)
[![react-dropzone](https://img.shields.io/npm/v/react-dropzone?style=for-the-badge&label=react-dropzone&color=00B8D9)](https://www.npmjs.com/package/react-dropzone)
[![react-icons](https://img.shields.io/npm/v/react-icons?style=for-the-badge&label=react-icons&color=E91E63)](https://www.npmjs.com/package/react-icons)
[![react-router-dom](https://img.shields.io/npm/v/react-router-dom?style=for-the-badge&label=react-router-dom&color=CA4245)](https://www.npmjs.com/package/react-router-dom)

### Dev Dependencies
[![typescript](https://img.shields.io/npm/v/typescript?style=for-the-badge&label=typescript&color=3178C6)](https://www.npmjs.com/package/typescript)
[![vite](https://img.shields.io/npm/v/vite?style=for-the-badge&label=vite&color=646CFF)](https://www.npmjs.com/package/vite)
[![vitest](https://img.shields.io/npm/v/vitest?style=for-the-badge&label=vitest&color=6E9F18)](https://www.npmjs.com/package/vitest)
[![eslint](https://img.shields.io/npm/v/eslint?style=for-the-badge&label=eslint&color=4B32C3)](https://www.npmjs.com/package/eslint)
[![@vitejs/plugin-react](https://img.shields.io/npm/v/@vitejs/plugin-react?style=for-the-badge&label=@vitejs/plugin-react&color=61DAFB)](https://www.npmjs.com/package/@vitejs/plugin-react)
[![@typescript-eslint/eslint-plugin](https://img.shields.io/npm/v/@typescript-eslint/eslint-plugin?style=for-the-badge&label=@typescript-eslint/eslint-plugin&color=3178C6)](https://www.npmjs.com/package/@typescript-eslint/eslint-plugin)
[![@typescript-eslint/parser](https://img.shields.io/npm/v/@typescript-eslint/parser?style=for-the-badge&label=@typescript-eslint/parser&color=3178C6)](https://www.npmjs.com/package/@typescript-eslint/parser)

</details>

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
│   │   ├── augmentation.py
│   │   └── verify_dataset.py
│   ├── data/
│   │   ├── raw/
│   │   │   ├── characters_train_set/
│   │   │   ├── characters_test_set/
│   │   │   ├── digits_train_set/
│   │   │   └── digits_test_set/
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

Download an Urdu handwritten character dataset and place it in `backend/data/raw/`.

#### Recommended Structure (Split Train/Test)

The recommended structure uses separate train and test directories:

```
backend/data/raw/
├── characters_train_set/
│   ├── alif/
│   │   ├── img001.png
│   │   └── ...
│   ├── alif mad aa/
│   ├── ayn/
│   ├── baa/
│   ├── bari yaa/
│   ├── cheey/
│   ├── choti yaa/
│   ├── daal/
│   ├── dhaal/
│   ├── faa/
│   ├── gaaf/
│   ├── ghain/
│   ├── haa1/
│   ├── haa2/
│   ├── haa3/
│   ├── hamza/
│   ├── jeem/
│   ├── kaaf/
│   ├── khaa/
│   ├── laam/
│   ├── meem/
│   ├── noon/
│   ├── noonghunna/
│   ├── paa/
│   ├── qaaf/
│   ├── raa/
│   ├── rhraa/
│   ├── seen/
│   ├── seey/
│   ├── sheen/
│   ├── swaad/
│   ├── taa/
│   ├── ttaa/
│   ├── twa/
│   ├── waw/
│   ├── zaaa/
│   ├── zaal/
│   ├── zhaa/
│   ├── zwaa/
│   └── zwaad/
├── characters_test_set/
│   └── (same structure as train set)
├── digits_train_set/
│   ├── 0/
│   ├── 1/
│   ├── 2/
│   ├── 3/
│   ├── 4/
│   ├── 5/
│   ├── 6/
│   ├── 7/
│   ├── 8/
│   └── 9/
└── digits_test_set/
    └── (same structure as train set)
```

#### Legacy Structure (Single Directory)

You can also use a single directory with all classes:

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

### 2. Verify Dataset

Before training, verify your dataset structure:

```bash
cd backend
python -m ml.verify_dataset --data-dir data/raw
```

To also test data loading:
```bash
python -m ml.verify_dataset --data-dir data/raw --test-load
```

### 3. Train

#### Train Character Model (Recommended)
```bash
cd backend
python -m ml.train --dataset-type characters
```

#### Train Digit Model
```bash
cd backend
python -m ml.train --dataset-type digits --model-path saved_models/urdu_digits_model.h5 --labels-path saved_models/digit_labels.json
```

#### Training Options
```bash
python -m ml.train --help

Options:
  --data-dir          Base directory for raw data (default: data/raw)
  --processed-dir     Directory for processed data (default: data/processed)
  --model-path        Path to save the model (default: saved_models/urdu_cnn_model.h5)
  --labels-path       Path to save class labels (default: saved_models/class_labels.json)
  --dataset-type      Dataset type: 'characters' or 'digits' (default: characters)
  --image-size        Image size (default: 64)
  --batch-size        Batch size (default: 32)
  --epochs            Number of epochs (default: 100)
  --lr                Learning rate (default: 0.001)
  --no-augmentation   Disable data augmentation
  --use-processed     Use pre-processed data if available
  --no-split-dirs     Use legacy single directory mode
```

### 4. Evaluate

```bash
python -m ml.evaluate
```

## 📚 Datasets

### Recommended Datasets

1. **Urdu Handwritten Dataset**
   - URL: https://www.kaggle.com/datasets/surindersinghkhurana/handwritten-urdu-characters-dataset
   - Contains: Urdu characters script

2. **Urdu Nastalique Dataset**
   - URL: https://www.kaggle.com/datasets/saqibraza21/printed-urdu-character-nastalique-font
   - Research paper: Search for "UCOM Urdu Character Dataset"

3. **Urdu-Handwritten-Characters Dataset (Kaggle)**
   - URL: https://www.kaggle.com/datasets/hazrat/uhat-urdu-handwritten-text-dataset
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

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details on:
- How to fork and clone the repository
- Code style and linting rules
- Submitting bug reports and feature requests
- Creating pull requests
- Testing and documentation requirements

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🛡 Security

Security is a priority for this project. If you discover a security vulnerability, please review our [Security Policy](SECURITY.md) for information on how to report it responsibly.

## 📏 Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) to understand our community guidelines and expectations.

## 🙏 Acknowledgments

- TensorFlow/Keras team for the deep learning framework
- FastAPI team for the excellent web framework
- React team for the frontend library
- All contributors to the Urdu handwritten character datasets
- The open-source community for their invaluable tools and libraries

## 📧 Contact

For questions or feedback, please open an issue on GitHub or reach out through our [Discussions](https://github.com/H0NEYP0T-466/URDU-OCR-CNN/discussions).

---

<p align="center">Made with ❤️ by H0NEYP0T-466</p>
