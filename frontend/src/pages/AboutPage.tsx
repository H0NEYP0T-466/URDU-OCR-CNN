/**
 * About Page
 * 
 * Information about the project and technology.
 */

import './AboutPage.css';

const FRONTEND_TECHNOLOGIES = ['React 18', 'TypeScript', 'Vite', 'CSS', 'Axios', 'React Router'];
const BACKEND_TECHNOLOGIES = ['FastAPI', 'Python 3.10+', 'TensorFlow/Keras', 'OpenCV', 'NumPy', 'Pillow'];

const AboutPage: React.FC = () => {
  const urduCharacters = [
    'ا', 'ب', 'پ', 'ت', 'ٹ', 'ث', 'ج', 'چ', 'ح', 'خ',
    'د', 'ڈ', 'ذ', 'ر', 'ڑ', 'ز', 'ژ', 'س', 'ش', 'ص',
    'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل',
    'م', 'ن', 'و', 'ہ', 'ی', 'ے',
  ];

  const urduDigits = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];

  return (
    <div className="about-container">
      {/* Hero Section */}
      <div className="about-hero">
        <h1>About Urdu OCR</h1>
        <p>
          A deep learning-powered application for recognizing handwritten Urdu characters
          using Convolutional Neural Networks.
        </p>
      </div>

      {/* Project Overview */}
      <div className="about-card">
        <div className="about-card-inner">
          <h2>Project Overview</h2>
          <p>
            The Urdu Character Recognition System is a full-stack web application that uses
            machine learning to identify handwritten Urdu characters. Users can either upload
            an image of a handwritten character or draw one directly on the canvas.
          </p>
          <p>
            The system uses a Convolutional Neural Network (CNN) trained on a dataset of
            handwritten Urdu characters to make predictions. It can recognize 36 Urdu alphabets
            and 10 Urdu digits with high accuracy.
          </p>
        </div>
      </div>

      {/* Tech Stack */}
      <div className="tech-stack-section">
        <h2 className="tech-stack-title">Technology Stack</h2>
        <div className="tech-stack-grid">
          {/* Frontend */}
          <div className="tech-stack-card">
            <h3 className="frontend">Frontend</h3>
            <ul className="tech-list">
              {FRONTEND_TECHNOLOGIES.map((tech) => (
                <li key={tech} className="tech-list-item">
                  <svg fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                  </svg>
                  {tech}
                </li>
              ))}
            </ul>
          </div>

          {/* Backend */}
          <div className="tech-stack-card">
            <h3 className="backend">Backend</h3>
            <ul className="tech-list">
              {BACKEND_TECHNOLOGIES.map((tech) => (
                <li key={tech} className="tech-list-item">
                  <svg fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                  </svg>
                  {tech}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>

      {/* Supported Characters */}
      <div className="characters-section">
        <div className="characters-card">
          <h2 className="characters-title">Supported Characters</h2>
          
          {/* Urdu Alphabets */}
          <div className="characters-group">
            <h3>Urdu Alphabets (36)</h3>
            <div className="characters-grid">
              {urduCharacters.map((char, index) => (
                <span
                  key={index}
                  className="urdu-text character-item alphabet"
                >
                  {char}
                </span>
              ))}
            </div>
          </div>

          {/* Urdu Digits */}
          <div className="characters-group">
            <h3>Urdu Digits (10)</h3>
            <div className="characters-grid">
              {urduDigits.map((digit, index) => (
                <span
                  key={index}
                  className="urdu-text character-item digit"
                >
                  {digit}
                </span>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Dataset Information */}
      <div className="dataset-section">
        <div className="dataset-card">
          <h2 className="dataset-title">Dataset Information</h2>
          <p className="dataset-intro">
            The model can be trained on various Urdu handwritten character datasets:
          </p>
          <ul className="dataset-list">
            <li>
              <span className="dataset-list-bullet">•</span>
              <div>
                <strong>UNHD Dataset</strong> - Urdu Nastaliq Handwritten Dataset
              </div>
            </li>
            <li>
              <span className="dataset-list-bullet">•</span>
              <div>
                <strong>UCOM Offline Dataset</strong> - Research dataset for Urdu characters
              </div>
            </li>
            <li>
              <span className="dataset-list-bullet">•</span>
              <div>
                <strong>Kaggle Urdu Dataset</strong> - 38 classes of Urdu characters
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default AboutPage;
