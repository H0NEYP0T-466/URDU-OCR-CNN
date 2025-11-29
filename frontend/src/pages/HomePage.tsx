/**
 * Home Page
 * 
 * Main page with image upload and drawing canvas for character prediction.
 */

import { useState } from 'react';
import ImageUploader from '../components/ImageUploader';
import DrawingCanvas from '../components/DrawingCanvas';
import PredictionResult from '../components/PredictionResult';
import { usePrediction } from '../hooks/usePrediction';
import './HomePage.css';

type InputMode = 'upload' | 'draw';

const HomePage: React.FC = () => {
  const [inputMode, setInputMode] = useState<InputMode>('upload');
  const { state, predictImage, predictCanvas, reset } = usePrediction();

  const handleImageSelect = (file: File) => {
    predictImage(file);
  };

  const handleCanvasSubmit = (imageData: string) => {
    predictCanvas(imageData);
  };

  return (
    <div className="home-container">
      {/* Hero Section */}
      <div className="home-hero">
        <h1>
          Urdu Character Recognition
        </h1>
        <p>
          Upload an image or draw a handwritten Urdu character, and our AI will recognize it using
          deep learning technology.
        </p>
      </div>

      {/* Mode Selector */}
      <div className="mode-selector">
        <div className="mode-selector-buttons">
          <button
            onClick={() => setInputMode('upload')}
            className={`mode-selector-btn ${
              inputMode === 'upload' ? 'active' : ''
            }`}
          >
            Upload Image
          </button>
          <button
            onClick={() => setInputMode('draw')}
            className={`mode-selector-btn ${
              inputMode === 'draw' ? 'active' : ''
            }`}
          >
            Draw Character
          </button>
        </div>
      </div>

      {/* Main Content */}
      <div className="home-main-content">
        {/* Input Section */}
        <div className="home-input-section">
          <h2 className="home-section-title">
            {inputMode === 'upload' ? 'Upload Image' : 'Draw Character'}
          </h2>
          
          {inputMode === 'upload' ? (
            <ImageUploader
              onImageSelect={handleImageSelect}
              isLoading={state.isLoading}
            />
          ) : (
            <DrawingCanvas
              onSubmit={handleCanvasSubmit}
              isLoading={state.isLoading}
            />
          )}
        </div>

        {/* Result Section */}
        <div>
          <h2 className="home-section-title">Prediction Result</h2>
          <PredictionResult
            result={state.result}
            isLoading={state.isLoading}
            error={state.error}
            onReset={reset}
          />
        </div>
      </div>

      {/* Feature Cards */}
      <div className="feature-cards">
        <div className="feature-card">
          <div className="feature-card-icon blue">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
            </svg>
          </div>
          <h3>AI-Powered</h3>
          <p>
            Uses deep learning CNN to accurately recognize handwritten Urdu characters.
          </p>
        </div>

        <div className="feature-card">
          <div className="feature-card-icon green">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
          </div>
          <h3>Fast & Accurate</h3>
          <p>
            Get predictions in milliseconds with high confidence scores.
          </p>
        </div>

        <div className="feature-card">
          <div className="feature-card-icon purple">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
            </svg>
          </div>
          <h3>46+ Characters</h3>
          <p>
            Supports all Urdu alphabets and digits for comprehensive recognition.
          </p>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
