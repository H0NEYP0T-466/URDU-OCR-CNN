/**
 * Prediction Result Component
 * 
 * Displays prediction results with confidence scores.
 */

import type { PredictionResultProps } from '../types';
import LoadingSpinner from './LoadingSpinner';
import './PredictionResult.css';

const PredictionResult: React.FC<PredictionResultProps> = ({
  result,
  isLoading,
  error,
  onReset,
}) => {
  if (isLoading) {
    return (
      <div className="prediction-card" style={{ textAlign: 'center' }}>
        <LoadingSpinner message="Analyzing character..." />
      </div>
    );
  }

  if (error) {
    return (
      <div className="prediction-card error">
        <div className="prediction-error-content">
          <svg
            className="prediction-error-icon"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
          <h3 className="prediction-error-title">Error</h3>
          <p className="prediction-error-message">{error}</p>
          <button onClick={onReset} className="btn-primary">
            Try Again
          </button>
        </div>
      </div>
    );
  }

  if (!result) {
    return (
      <div className="prediction-card empty">
        <div className="prediction-empty-content">
          <svg
            className="prediction-empty-icon"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"
            />
          </svg>
          <p className="prediction-empty-text">Upload or draw a character to see prediction</p>
        </div>
      </div>
    );
  }

  const confidencePercent = Math.round(result.confidence * 100);

  return (
    <div className="prediction-card">
      {/* Main Prediction */}
      <div className="prediction-main">
        <p className="prediction-label">Predicted Character</p>
        <div className="urdu-text prediction-character">
          {result.prediction}
        </div>
        
        {/* Confidence Bar */}
        <div className="confidence-container">
          <div className="confidence-header">
            <span>Confidence</span>
            <span className="confidence-value">{confidencePercent}%</span>
          </div>
          <div className="progress-bar">
            <div
              className="progress-fill"
              style={{ width: `${confidencePercent}%` }}
            />
          </div>
        </div>
      </div>

      {/* Processing Time */}
      <div className="processing-time">
        <span>
          Processing time: {result.processing_time_ms.toFixed(2)}ms
        </span>
      </div>

      {/* Top 5 Predictions */}
      <div className="top-predictions">
        <h4 className="top-predictions-title">Top 5 Predictions</h4>
        <div className="top-predictions-list">
          {result.top_5.map((pred, index) => (
            <div
              key={index}
              className="top-prediction-item"
            >
              <div className="top-prediction-left">
                <span className="top-prediction-rank">{index + 1}.</span>
                <span className="urdu-text top-prediction-char">{pred.character}</span>
              </div>
              <div className="top-prediction-right">
                <div className="top-prediction-bar">
                  <div
                    className="top-prediction-bar-fill"
                    style={{ width: `${pred.probability * 100}%` }}
                  />
                </div>
                <span className="top-prediction-percent">
                  {(pred.probability * 100).toFixed(1)}%
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Try Again Button */}
      <div className="prediction-reset">
        <button onClick={onReset} className="btn-secondary">
          Try Another Image
        </button>
      </div>
    </div>
  );
};

export default PredictionResult;
