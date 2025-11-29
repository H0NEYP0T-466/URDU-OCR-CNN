/**
 * About Page
 * 
 * Information about the project and technology.
 */

const AboutPage: React.FC = () => {
  const urduCharacters = [
    'ا', 'ب', 'پ', 'ت', 'ٹ', 'ث', 'ج', 'چ', 'ح', 'خ',
    'د', 'ڈ', 'ذ', 'ر', 'ڑ', 'ز', 'ژ', 'س', 'ش', 'ص',
    'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل',
    'م', 'ن', 'و', 'ہ', 'ی', 'ے',
  ];

  const urduDigits = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];

  return (
    <div className="container mx-auto px-4 py-8">
      {/* Hero Section */}
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold text-gray-800 mb-4">About Urdu OCR</h1>
        <p className="text-lg text-gray-600 max-w-2xl mx-auto">
          A deep learning-powered application for recognizing handwritten Urdu characters
          using Convolutional Neural Networks.
        </p>
      </div>

      {/* Project Overview */}
      <div className="max-w-4xl mx-auto mb-12">
        <div className="bg-white rounded-xl shadow-lg p-8">
          <h2 className="text-2xl font-semibold text-gray-800 mb-4">Project Overview</h2>
          <p className="text-gray-600 mb-4">
            The Urdu Character Recognition System is a full-stack web application that uses
            machine learning to identify handwritten Urdu characters. Users can either upload
            an image of a handwritten character or draw one directly on the canvas.
          </p>
          <p className="text-gray-600">
            The system uses a Convolutional Neural Network (CNN) trained on a dataset of
            handwritten Urdu characters to make predictions. It can recognize 36 Urdu alphabets
            and 10 Urdu digits with high accuracy.
          </p>
        </div>
      </div>

      {/* Tech Stack */}
      <div className="max-w-4xl mx-auto mb-12">
        <h2 className="text-2xl font-semibold text-gray-800 mb-6 text-center">Technology Stack</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Frontend */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h3 className="text-lg font-semibold text-blue-600 mb-4">Frontend</h3>
            <ul className="space-y-2">
              {['React 18', 'TypeScript', 'Vite', 'TailwindCSS', 'Axios', 'React Router'].map((tech) => (
                <li key={tech} className="flex items-center text-gray-600">
                  <svg className="w-4 h-4 text-green-500 mr-2" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                  </svg>
                  {tech}
                </li>
              ))}
            </ul>
          </div>

          {/* Backend */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h3 className="text-lg font-semibold text-green-600 mb-4">Backend</h3>
            <ul className="space-y-2">
              {['FastAPI', 'Python 3.10+', 'TensorFlow/Keras', 'OpenCV', 'NumPy', 'Pillow'].map((tech) => (
                <li key={tech} className="flex items-center text-gray-600">
                  <svg className="w-4 h-4 text-green-500 mr-2" fill="currentColor" viewBox="0 0 20 20">
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
      <div className="max-w-4xl mx-auto mb-12">
        <div className="bg-white rounded-xl shadow-lg p-8">
          <h2 className="text-2xl font-semibold text-gray-800 mb-6 text-center">Supported Characters</h2>
          
          {/* Urdu Alphabets */}
          <div className="mb-6">
            <h3 className="text-lg font-medium text-gray-700 mb-3">Urdu Alphabets (36)</h3>
            <div className="flex flex-wrap gap-2 justify-center">
              {urduCharacters.map((char, index) => (
                <span
                  key={index}
                  className="urdu-text text-2xl w-10 h-10 flex items-center justify-center bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors"
                >
                  {char}
                </span>
              ))}
            </div>
          </div>

          {/* Urdu Digits */}
          <div>
            <h3 className="text-lg font-medium text-gray-700 mb-3">Urdu Digits (10)</h3>
            <div className="flex flex-wrap gap-2 justify-center">
              {urduDigits.map((digit, index) => (
                <span
                  key={index}
                  className="urdu-text text-2xl w-10 h-10 flex items-center justify-center bg-green-50 rounded-lg hover:bg-green-100 transition-colors"
                >
                  {digit}
                </span>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Dataset Information */}
      <div className="max-w-4xl mx-auto">
        <div className="bg-white rounded-xl shadow-lg p-8">
          <h2 className="text-2xl font-semibold text-gray-800 mb-4">Dataset Information</h2>
          <p className="text-gray-600 mb-4">
            The model can be trained on various Urdu handwritten character datasets:
          </p>
          <ul className="space-y-3 text-gray-600">
            <li className="flex items-start">
              <span className="text-blue-500 mr-2">•</span>
              <div>
                <strong>UNHD Dataset</strong> - Urdu Nastaliq Handwritten Dataset
              </div>
            </li>
            <li className="flex items-start">
              <span className="text-blue-500 mr-2">•</span>
              <div>
                <strong>UCOM Offline Dataset</strong> - Research dataset for Urdu characters
              </div>
            </li>
            <li className="flex items-start">
              <span className="text-blue-500 mr-2">•</span>
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
