/**
 * How It Works Page
 * 
 * Explains the prediction process and model architecture.
 */

import './HowItWorksPage.css';

const HowItWorksPage: React.FC = () => {
  const steps = [
    {
      number: 1,
      title: 'Input',
      description: 'Upload an image of a handwritten Urdu character or draw one on the canvas.',
      icon: (
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
        </svg>
      ),
    },
    {
      number: 2,
      title: 'Preprocessing',
      description: 'The image is converted to grayscale, resized to 64x64 pixels, and normalized.',
      icon: (
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
        </svg>
      ),
    },
    {
      number: 3,
      title: 'CNN Analysis',
      description: 'The preprocessed image passes through our Convolutional Neural Network.',
      icon: (
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
        </svg>
      ),
    },
    {
      number: 4,
      title: 'Prediction',
      description: 'The model outputs probability scores for each character class.',
      icon: (
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
        </svg>
      ),
    },
  ];

  const modelLayers = [
    { name: 'Input Layer', details: '64×64×1 grayscale image' },
    { name: 'Conv2D Block 1', details: '32 filters, 3×3, BatchNorm, ReLU, MaxPool, Dropout(0.25)' },
    { name: 'Conv2D Block 2', details: '64 filters, 3×3, BatchNorm, ReLU, MaxPool, Dropout(0.25)' },
    { name: 'Conv2D Block 3', details: '128 filters, 3×3, BatchNorm, ReLU, MaxPool, Dropout(0.25)' },
    { name: 'Conv2D Block 4', details: '256 filters, 3×3, BatchNorm, ReLU, MaxPool, Dropout(0.25)' },
    { name: 'Flatten', details: 'Flatten to 1D vector' },
    { name: 'Dense Block 1', details: '512 units, BatchNorm, ReLU, Dropout(0.5)' },
    { name: 'Dense Block 2', details: '256 units, BatchNorm, ReLU, Dropout(0.5)' },
    { name: 'Output Layer', details: '46 classes, Softmax activation' },
  ];

  return (
    <div className="how-it-works-page">
      {/* Hero Section */}
      <div className="how-it-works-hero">
        <h1 className="how-it-works-hero-title">How It Works</h1>
        <p className="how-it-works-hero-text">
          Learn about the process and technology behind our Urdu character recognition system.
        </p>
      </div>

      {/* Process Steps */}
      <div className="how-it-works-section">
        <h2 className="how-it-works-section-title">Recognition Process</h2>
        <div className="how-it-works-steps">
          {steps.map((step) => (
            <div key={step.number} className="how-it-works-step">
              <div className="how-it-works-step-card">
                <div className="how-it-works-step-icon">
                  {step.icon}
                </div>
                <div className="how-it-works-step-number">
                  {step.number}
                </div>
                <h3 className="how-it-works-step-title">{step.title}</h3>
                <p className="how-it-works-step-text">{step.description}</p>
              </div>
              {step.number < 4 && (
                <div className="how-it-works-arrow">
                  <svg fill="currentColor" viewBox="0 0 24 24">
                    <path d="M8.59 16.59L13.17 12 8.59 7.41 10 6l6 6-6 6-1.41-1.41z" />
                  </svg>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>

      {/* Model Architecture */}
      <div className="how-it-works-architecture">
        <h2 className="how-it-works-section-title">CNN Architecture</h2>
        <div className="how-it-works-architecture-card">
          <div className="how-it-works-layers">
            {modelLayers.map((layer, index) => (
              <div
                key={index}
                className={`how-it-works-layer ${
                  index === 0 ? 'input' :
                  index === modelLayers.length - 1 ? 'output' :
                  'middle'
                }`}
              >
                <div className="how-it-works-layer-number">
                  {index + 1}
                </div>
                <div className="how-it-works-layer-content">
                  <h4 className="how-it-works-layer-name">{layer.name}</h4>
                  <p className="how-it-works-layer-details">{layer.details}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Training Info */}
      <div className="how-it-works-training">
        <h2 className="how-it-works-section-title">Training Details</h2>
        <div className="how-it-works-training-grid">
          <div className="how-it-works-training-card">
            <h3>Optimization</h3>
            <ul className="how-it-works-optimization-list">
              <li>
                <span>Optimizer:</span>
                <span>Adam</span>
              </li>
              <li>
                <span>Loss Function:</span>
                <span>Categorical Cross-entropy</span>
              </li>
              <li>
                <span>Initial Learning Rate:</span>
                <span>0.001</span>
              </li>
            </ul>
          </div>

          <div className="how-it-works-training-card">
            <h3>Data Augmentation</h3>
            <ul className="how-it-works-augmentation-list">
              <li>
                <svg fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                </svg>
                Rotation (±15°)
              </li>
              <li>
                <svg fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                </svg>
                Width/Height Shift (10%)
              </li>
              <li>
                <svg fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                </svg>
                Zoom (10%)
              </li>
              <li>
                <svg fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                </svg>
                Shear (10%)
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HowItWorksPage;
