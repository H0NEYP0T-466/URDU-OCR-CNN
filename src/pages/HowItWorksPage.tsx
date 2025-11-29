/**
 * How It Works Page
 * 
 * Explains the prediction process and model architecture.
 */

const HowItWorksPage: React.FC = () => {
  const steps = [
    {
      number: 1,
      title: 'Input',
      description: 'Upload an image of a handwritten Urdu character or draw one on the canvas.',
      icon: (
        <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
        </svg>
      ),
    },
    {
      number: 2,
      title: 'Preprocessing',
      description: 'The image is converted to grayscale, resized to 64x64 pixels, and normalized.',
      icon: (
        <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
        </svg>
      ),
    },
    {
      number: 3,
      title: 'CNN Analysis',
      description: 'The preprocessed image passes through our Convolutional Neural Network.',
      icon: (
        <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
        </svg>
      ),
    },
    {
      number: 4,
      title: 'Prediction',
      description: 'The model outputs probability scores for each character class.',
      icon: (
        <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
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
    <div className="container mx-auto px-4 py-8">
      {/* Hero Section */}
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold text-gray-800 mb-4">How It Works</h1>
        <p className="text-lg text-gray-600 max-w-2xl mx-auto">
          Learn about the process and technology behind our Urdu character recognition system.
        </p>
      </div>

      {/* Process Steps */}
      <div className="max-w-5xl mx-auto mb-16">
        <h2 className="text-2xl font-semibold text-gray-800 mb-8 text-center">Recognition Process</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {steps.map((step) => (
            <div key={step.number} className="relative">
              <div className="bg-white rounded-xl shadow-lg p-6 h-full">
                <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center text-blue-600 mb-4">
                  {step.icon}
                </div>
                <div className="absolute -top-3 -left-3 w-8 h-8 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold text-sm">
                  {step.number}
                </div>
                <h3 className="text-lg font-semibold text-gray-800 mb-2">{step.title}</h3>
                <p className="text-sm text-gray-600">{step.description}</p>
              </div>
              {step.number < 4 && (
                <div className="hidden lg:block absolute top-1/2 -right-3 w-6 text-gray-300">
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
      <div className="max-w-4xl mx-auto mb-16">
        <h2 className="text-2xl font-semibold text-gray-800 mb-8 text-center">CNN Architecture</h2>
        <div className="bg-white rounded-xl shadow-lg p-8">
          <div className="space-y-4">
            {modelLayers.map((layer, index) => (
              <div
                key={index}
                className={`flex items-center p-4 rounded-lg ${
                  index === 0 ? 'bg-green-50 border-l-4 border-green-500' :
                  index === modelLayers.length - 1 ? 'bg-blue-50 border-l-4 border-blue-500' :
                  'bg-gray-50 border-l-4 border-gray-300'
                }`}
              >
                <div className="flex-shrink-0 w-8 h-8 rounded-full bg-gray-200 flex items-center justify-center text-sm font-medium text-gray-600 mr-4">
                  {index + 1}
                </div>
                <div className="flex-grow">
                  <h4 className="font-medium text-gray-800">{layer.name}</h4>
                  <p className="text-sm text-gray-600">{layer.details}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Training Info */}
      <div className="max-w-4xl mx-auto">
        <h2 className="text-2xl font-semibold text-gray-800 mb-8 text-center">Training Details</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h3 className="text-lg font-semibold text-gray-800 mb-4">Optimization</h3>
            <ul className="space-y-2 text-gray-600">
              <li className="flex justify-between">
                <span>Optimizer:</span>
                <span className="font-medium">Adam</span>
              </li>
              <li className="flex justify-between">
                <span>Loss Function:</span>
                <span className="font-medium">Categorical Cross-entropy</span>
              </li>
              <li className="flex justify-between">
                <span>Initial Learning Rate:</span>
                <span className="font-medium">0.001</span>
              </li>
            </ul>
          </div>

          <div className="bg-white rounded-xl shadow-lg p-6">
            <h3 className="text-lg font-semibold text-gray-800 mb-4">Data Augmentation</h3>
            <ul className="space-y-2 text-gray-600">
              <li className="flex items-center">
                <svg className="w-4 h-4 text-green-500 mr-2" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                </svg>
                Rotation (±15°)
              </li>
              <li className="flex items-center">
                <svg className="w-4 h-4 text-green-500 mr-2" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                </svg>
                Width/Height Shift (10%)
              </li>
              <li className="flex items-center">
                <svg className="w-4 h-4 text-green-500 mr-2" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                </svg>
                Zoom (10%)
              </li>
              <li className="flex items-center">
                <svg className="w-4 h-4 text-green-500 mr-2" fill="currentColor" viewBox="0 0 20 20">
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
