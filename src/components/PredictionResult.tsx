/**
 * Prediction Result Component
 * 
 * Displays prediction results with confidence scores.
 */

import type { PredictionResultProps } from '../types';
import LoadingSpinner from './LoadingSpinner';
import { getFormattedCharacter, isDigitPrediction } from '../utils/characterMapping';
import './PredictionResult.css';

const PredictionResult: React.FC<PredictionResultProps> = ({
  result,
  isLoading,
  error,
  onReset,
}) => {
  if (isLoading) {
    return (
      <div className="prediction-result prediction-result-loading">
        <LoadingSpinner message="Analyzing character..." />
      </div>
    );
  }

  if (error) {
    return (
      <div className="prediction-result prediction-result-error">
        <div className="prediction-result-error-content">
          <svg
            className="prediction-result-error-icon"
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
          <h3 className="prediction-result-error-title">Error</h3>
          <p className="prediction-result-error-message">{error}</p>
          <button onClick={onReset} className="btn-primary">
            Try Again
          </button>
        </div>
      </div>
    );
  }

  if (!result) {
    return (
      <div className="prediction-result prediction-result-placeholder">
        <div className="prediction-result-placeholder-content">
          <svg
            className="prediction-result-placeholder-icon"
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
          <p className="prediction-result-placeholder-text">Upload or draw a character to see prediction</p>
        </div>
      </div>
    );
  }

  const confidencePercent = Math.round(result.confidence * 100);
  const isDigit = isDigitPrediction(result.prediction);
  const formattedPrediction = getFormattedCharacter(result.prediction, isDigit);

  return (
    <div className="prediction-result">
      {/* Main Prediction */}
      <div className="prediction-result-main">
        <p className="prediction-result-label">Predicted Character</p>
        <div className="prediction-result-character urdu-text">
          {formattedPrediction}
        </div>
        
        {/* Confidence Bar */}
        <div className="prediction-result-confidence">
          <div className="prediction-result-confidence-header">
            <span>Confidence</span>
            <span className="prediction-result-confidence-value">{confidencePercent}%</span>
          </div>
          <div className="prediction-result-confidence-bar">
            <div
              className="prediction-result-confidence-fill"
              style={{ width: `${confidencePercent}%` }}
            />
          </div>
        </div>
      </div>

      {/* Processing Time */}
      <div className="prediction-result-time">
        <span>
          Processing time: {result.processing_time_ms.toFixed(2)}ms
        </span>
      </div>

      {/* Top 5 Predictions */}
      <div className="prediction-result-top5">
        <h4 className="prediction-result-top5-title">Top 5 Predictions</h4>
        <div className="prediction-result-top5-list">
          {result.top_5.map((pred, index) => {
            const predIsDigit = isDigitPrediction(pred.character);
            const formattedChar = getFormattedCharacter(pred.character, predIsDigit);
            return (
              <div
                key={index}
                className="prediction-result-top5-item"
              >
                <div className="prediction-result-top5-item-left">
                  <span className="prediction-result-top5-item-rank">{index + 1}.</span>
                  <span className="prediction-result-top5-item-character urdu-text">{formattedChar}</span>
                </div>
                <div className="prediction-result-top5-item-right">
                  <div className="prediction-result-top5-item-bar">
                    <div
                      className="prediction-result-top5-item-bar-fill"
                      style={{ width: `${pred.probability * 100}%` }}
                    />
                  </div>
                  <span className="prediction-result-top5-item-percent">
                    {(pred.probability * 100).toFixed(1)}%
                  </span>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Try Again Button */}
      <div className="prediction-result-actions">
        <button onClick={onReset} className="btn-secondary">
          Try Another Image
        </button>
      </div>
    </div>
  );
};

export default PredictionResult;
