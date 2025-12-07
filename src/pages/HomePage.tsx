/**
 * Home Page
 * 
 * Main page with image upload and drawing canvas for character and digit prediction.
 */

import { useState } from 'react';
import ImageUploader from '../components/ImageUploader';
import DrawingCanvas from '../components/DrawingCanvas';
import PredictionResult from '../components/PredictionResult';
import { usePrediction, ModelType } from '../hooks/usePrediction';
import { getAllCharacters, getAllDigits } from '../utils/characterMapping';
import './HomePage.css';

type InputMode = 'upload' | 'draw';

const HomePage: React.FC = () => {
  const [inputMode, setInputMode] = useState<InputMode>('upload');
  const [modelType, setModelType] = useState<ModelType>('character');
  const { state, predictImage, predictCanvas, reset } = usePrediction();

  const handleImageSelect = (file: File) => {
    predictImage(file, modelType);
  };

  const handleCanvasSubmit = (imageData: string) => {
    predictCanvas(imageData, modelType);
  };

  const handleModelTypeChange = (newModelType: ModelType) => {
    setModelType(newModelType);
    reset(); // Reset prediction when model type changes
  };

  return (
    <div className="home-page">
      {/* Hero Section */}
      <div className="home-hero">
        <h1 className="home-hero-title">
          Urdu {modelType === 'character' ? 'Character' : 'Digit'} Recognition
        </h1>
        <p className="home-hero-text">
          Upload an image or draw a handwritten Urdu {modelType === 'character' ? 'character' : 'digit'}, and our AI will recognize it using
          deep learning technology.
        </p>
      </div>

      {/* Model Type Selector */}
      <div className="home-model-selector">
        <span className="home-model-label">Select Model:</span>
        <div className="home-model-buttons">
          <button
            onClick={() => handleModelTypeChange('character')}
            className={`home-model-button ${
              modelType === 'character' ? 'active' : ''
            }`}
          >
            Character Recognition
          </button>
          <button
            onClick={() => handleModelTypeChange('digit')}
            className={`home-model-button ${
              modelType === 'digit' ? 'active' : ''
            }`}
          >
            Digit Recognition
          </button>
        </div>
      </div>

      {/* Mode Selector */}
      <div className="home-mode-selector">
        <div className="home-mode-buttons">
          <button
            onClick={() => setInputMode('upload')}
            className={`home-mode-button ${
              inputMode === 'upload' ? 'active' : ''
            }`}
          >
            Upload Image
          </button>
          <button
            onClick={() => setInputMode('draw')}
            className={`home-mode-button ${
              inputMode === 'draw' ? 'active' : ''
            }`}
          >
            Draw {modelType === 'character' ? 'Character' : 'Digit'}
          </button>
        </div>
      </div>

      {/* Main Content */}
      <div className="home-main-content">
        {/* Input Section */}
        <div className="home-input-section">
          <h2 className="home-section-title">
            {inputMode === 'upload' ? 'Upload Image' : `Draw ${modelType === 'character' ? 'Character' : 'Digit'}`}
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
              instructionText={modelType === 'character' ? 'Draw an Urdu character here' : 'Draw an Urdu digit here (۰-۹)'}
              submitButtonText={modelType === 'character' ? 'Predict Character' : 'Predict Digit'}
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
      <div className="home-feature-cards">
        <div className="home-feature-card">
          <div className="home-feature-icon blue">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
            </svg>
          </div>
          <h3 className="home-feature-title">AI-Powered</h3>
          <p className="home-feature-text">
            Uses deep learning CNN to accurately recognize handwritten Urdu characters and digits.
          </p>
        </div>

        <div className="home-feature-card">
          <div className="home-feature-icon green">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
          </div>
          <h3 className="home-feature-title">Fast & Accurate</h3>
          <p className="home-feature-text">
            Get predictions in milliseconds with high confidence scores.
          </p>
        </div>

        <div className="home-feature-card">
          <div className="home-feature-icon purple">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
            </svg>
          </div>
          <h3 className="home-feature-title">{getAllCharacters().length} Characters & {getAllDigits().length} Digits</h3>
          <p className="home-feature-text">
            Supports all Urdu alphabets and digits for comprehensive recognition.
          </p>
        </div>
      </div>

      {/* Supported Characters Section */}
      <div className="home-characters-section">
        <h2 className="home-section-title">Supported Characters</h2>
        
        {/* Urdu Alphabets */}
        <div className="home-characters-subsection">
          <h3 className="home-characters-subtitle">Urdu Alphabets ({getAllCharacters().length})</h3>
          <div className="home-characters-grid">
            {getAllCharacters().map((char, index) => (
              <div key={index} className="home-character-card">
                <span className="home-character-urdu urdu-text">{char.urdu}</span>
                <span className="home-character-name">{char.name}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Urdu Digits */}
        <div className="home-characters-subsection">
          <h3 className="home-characters-subtitle">Urdu Digits ({getAllDigits().length})</h3>
          <div className="home-characters-grid">
            {getAllDigits().map((digit, index) => (
              <div key={index} className="home-character-card">
                <span className="home-character-urdu urdu-text">{digit.urdu}</span>
                <span className="home-character-name">{digit.name}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
