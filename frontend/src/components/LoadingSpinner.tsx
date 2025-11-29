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
  const sizeClasses: Record<string, string> = {
    sm: 'spinner-sm',
    md: 'spinner-md',
    lg: 'spinner-lg',
  };

  return (
    <div className="loading-spinner-container">
      <div className={`spinner ${sizeClasses[size]}`} />
      {message && (
        <p className="loading-spinner-message">{message}</p>
      )}
    </div>
  );
};

export default LoadingSpinner;
