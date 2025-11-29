/**
 * About Page
 * 
 * Information about the project and technology.
 */

import './AboutPage.css';

const AboutPage: React.FC = () => {
  const urduCharacters = [
    'ا', 'ب', 'پ', 'ت', 'ٹ', 'ث', 'ج', 'چ', 'ح', 'خ',
    'د', 'ڈ', 'ذ', 'ر', 'ڑ', 'ز', 'ژ', 'س', 'ش', 'ص',
    'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل',
    'م', 'ن', 'و', 'ہ', 'ی', 'ے',
  ];

  const urduDigits = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];

  return (
    <div className="about-page">
      {/* Hero Section */}
      <div className="about-hero">
        <h1 className="about-hero-title">About Urdu OCR</h1>
        <p className="about-hero-text">
          A deep learning-powered application for recognizing handwritten Urdu characters
          using Convolutional Neural Networks.
        </p>
      </div>

      {/* Project Overview */}
      <div className="about-section">
        <div className="about-card">
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
      <div className="about-section">
        <h2 className="about-section-title">Technology Stack</h2>
        <div className="about-tech-grid">
          {/* Frontend */}
          <div className="about-tech-card">
            <h3 className="blue">Frontend</h3>
            <ul className="about-tech-list">
              {['React 18', 'TypeScript', 'Vite', 'CSS', 'Axios', 'React Router'].map((tech) => (
                <li key={tech}>
                  <svg fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                  </svg>
                  {tech}
                </li>
              ))}
            </ul>
          </div>

          {/* Backend */}
          <div className="about-tech-card">
            <h3 className="green">Backend</h3>
            <ul className="about-tech-list">
              {['FastAPI', 'Python 3.10+', 'TensorFlow/Keras', 'OpenCV', 'NumPy', 'Pillow'].map((tech) => (
                <li key={tech}>
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
      <div className="about-section">
        <div className="about-characters-card">
          <h2>Supported Characters</h2>
          
          {/* Urdu Alphabets */}
          <div className="about-characters-section">
            <h3>Urdu Alphabets (36)</h3>
            <div className="about-characters-grid">
              {urduCharacters.map((char, index) => (
                <span
                  key={index}
                  className="about-character urdu-text blue"
                >
                  {char}
                </span>
              ))}
            </div>
          </div>

          {/* Urdu Digits */}
          <div className="about-characters-section">
            <h3>Urdu Digits (10)</h3>
            <div className="about-characters-grid">
              {urduDigits.map((digit, index) => (
                <span
                  key={index}
                  className="about-character urdu-text green"
                >
                  {digit}
                </span>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Dataset Information */}
      <div className="about-section">
        <div className="about-dataset-card">
          <h2>Dataset Information</h2>
          <p>
            The model can be trained on various Urdu handwritten character datasets:
          </p>
          <ul className="about-dataset-list">
            <li>
              <span className="about-dataset-bullet">•</span>
              <div className="about-dataset-item">
                <strong>UNHD Dataset</strong> - Urdu Nastaliq Handwritten Dataset
              </div>
            </li>
            <li>
              <span className="about-dataset-bullet">•</span>
              <div className="about-dataset-item">
                <strong>UCOM Offline Dataset</strong> - Research dataset for Urdu characters
              </div>
            </li>
            <li>
              <span className="about-dataset-bullet">•</span>
              <div className="about-dataset-item">
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
