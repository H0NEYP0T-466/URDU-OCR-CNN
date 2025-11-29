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
    <div className="container mx-auto px-4 py-8">
      {/* Hero Section */}
      <div className="text-center mb-10">
        <h1 className="text-4xl font-bold text-gray-800 mb-4">
          Urdu Character Recognition
        </h1>
        <p className="text-lg text-gray-600 max-w-2xl mx-auto">
          Upload an image or draw a handwritten Urdu character, and our AI will recognize it using
          deep learning technology.
        </p>
      </div>

      {/* Mode Selector */}
      <div className="flex justify-center mb-8">
        <div className="bg-gray-100 rounded-lg p-1 inline-flex">
          <button
            onClick={() => setInputMode('upload')}
            className={`px-6 py-2 rounded-lg transition-all duration-200 ${
              inputMode === 'upload'
                ? 'bg-white shadow text-blue-600 font-medium'
                : 'text-gray-600 hover:text-gray-800'
            }`}
          >
            Upload Image
          </button>
          <button
            onClick={() => setInputMode('draw')}
            className={`px-6 py-2 rounded-lg transition-all duration-200 ${
              inputMode === 'draw'
                ? 'bg-white shadow text-blue-600 font-medium'
                : 'text-gray-600 hover:text-gray-800'
            }`}
          >
            Draw Character
          </button>
        </div>
      </div>

      {/* Main Content */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 max-w-6xl mx-auto">
        {/* Input Section */}
        <div className="bg-white rounded-xl shadow-lg p-6">
          <h2 className="text-xl font-semibold text-gray-800 mb-4">
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
          <h2 className="text-xl font-semibold text-gray-800 mb-4">Prediction Result</h2>
          <PredictionResult
            result={state.result}
            isLoading={state.isLoading}
            error={state.error}
            onReset={reset}
          />
        </div>
      </div>

      {/* Feature Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-16 max-w-5xl mx-auto">
        <div className="bg-white rounded-lg shadow p-6 text-center card-hover">
          <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <svg className="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
            </svg>
          </div>
          <h3 className="font-semibold text-gray-800 mb-2">AI-Powered</h3>
          <p className="text-sm text-gray-600">
            Uses deep learning CNN to accurately recognize handwritten Urdu characters.
          </p>
        </div>

        <div className="bg-white rounded-lg shadow p-6 text-center card-hover">
          <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <svg className="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
          </div>
          <h3 className="font-semibold text-gray-800 mb-2">Fast & Accurate</h3>
          <p className="text-sm text-gray-600">
            Get predictions in milliseconds with high confidence scores.
          </p>
        </div>

        <div className="bg-white rounded-lg shadow p-6 text-center card-hover">
          <div className="w-12 h-12 bg-purple-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <svg className="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
            </svg>
          </div>
          <h3 className="font-semibold text-gray-800 mb-2">46+ Characters</h3>
          <p className="text-sm text-gray-600">
            Supports all Urdu alphabets and digits for comprehensive recognition.
          </p>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
