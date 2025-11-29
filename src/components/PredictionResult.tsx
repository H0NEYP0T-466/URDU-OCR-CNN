/**
 * Prediction Result Component
 * 
 * Displays prediction results with confidence scores.
 */

import type { PredictionResultProps } from '../types';
import LoadingSpinner from './LoadingSpinner';

const PredictionResult: React.FC<PredictionResultProps> = ({
  result,
  isLoading,
  error,
  onReset,
}) => {
  if (isLoading) {
    return (
      <div className="prediction-card text-center">
        <LoadingSpinner message="Analyzing character..." />
      </div>
    );
  }

  if (error) {
    return (
      <div className="prediction-card bg-red-50 border border-red-200">
        <div className="text-center">
          <svg
            className="w-12 h-12 text-red-500 mx-auto mb-3"
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
          <h3 className="text-lg font-semibold text-red-700 mb-2">Error</h3>
          <p className="text-red-600 mb-4">{error}</p>
          <button onClick={onReset} className="btn-primary">
            Try Again
          </button>
        </div>
      </div>
    );
  }

  if (!result) {
    return (
      <div className="prediction-card bg-gray-50">
        <div className="text-center text-gray-500">
          <svg
            className="w-16 h-16 mx-auto mb-4 text-gray-300"
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
          <p className="text-lg">Upload or draw a character to see prediction</p>
        </div>
      </div>
    );
  }

  const confidencePercent = Math.round(result.confidence * 100);

  return (
    <div className="prediction-card">
      {/* Main Prediction */}
      <div className="text-center mb-6">
        <p className="text-sm text-gray-500 uppercase tracking-wide mb-2">Predicted Character</p>
        <div className="urdu-text text-8xl font-bold text-blue-600 mb-4">
          {result.prediction}
        </div>
        
        {/* Confidence Bar */}
        <div className="max-w-xs mx-auto">
          <div className="flex justify-between text-sm text-gray-600 mb-1">
            <span>Confidence</span>
            <span className="font-medium">{confidencePercent}%</span>
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
      <div className="text-center mb-6">
        <span className="text-xs text-gray-400">
          Processing time: {result.processing_time_ms.toFixed(2)}ms
        </span>
      </div>

      {/* Top 5 Predictions */}
      <div className="border-t pt-6">
        <h4 className="text-sm font-semibold text-gray-700 mb-3">Top 5 Predictions</h4>
        <div className="space-y-2">
          {result.top_5.map((pred, index) => (
            <div
              key={index}
              className="flex items-center justify-between bg-gray-50 rounded-lg px-4 py-2"
            >
              <div className="flex items-center space-x-3">
                <span className="text-xs text-gray-400 w-4">{index + 1}.</span>
                <span className="urdu-text text-2xl">{pred.character}</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-24 h-2 bg-gray-200 rounded-full overflow-hidden">
                  <div
                    className="h-full bg-blue-400"
                    style={{ width: `${pred.probability * 100}%` }}
                  />
                </div>
                <span className="text-sm text-gray-600 w-12 text-right">
                  {(pred.probability * 100).toFixed(1)}%
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Try Again Button */}
      <div className="mt-6 text-center">
        <button onClick={onReset} className="btn-secondary">
          Try Another Image
        </button>
      </div>
    </div>
  );
};

export default PredictionResult;
