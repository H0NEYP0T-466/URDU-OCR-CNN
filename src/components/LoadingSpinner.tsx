/**
 * Loading Spinner Component
 * 
 * Animated spinner for loading states.
 */

import './LoadingSpinner.css';

interface LoadingSpinnerProps {
  size?: 'sm' | 'md' | 'lg';
  message?: string;
}

const LoadingSpinner: React.FC<LoadingSpinnerProps> = ({ 
  size = 'md',
  message = 'Processing...' 
}) => {
  return (
    <div className="loading-spinner-container">
      <div className={`loading-spinner ${size}`} />
      {message && (
        <p className="loading-spinner-message">{message}</p>
      )}
    </div>
  );
};

export default LoadingSpinner;
