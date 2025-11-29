/**
 * Loading Spinner Component
 * 
 * Animated spinner for loading states.
 */

interface LoadingSpinnerProps {
  size?: 'sm' | 'md' | 'lg';
  message?: string;
}

const LoadingSpinner: React.FC<LoadingSpinnerProps> = ({ 
  size = 'md',
  message = 'Processing...' 
}) => {
  const sizeClasses = {
    sm: 'w-6 h-6',
    md: 'w-10 h-10',
    lg: 'w-16 h-16',
  };

  return (
    <div className="flex flex-col items-center justify-center space-y-3">
      <div className={`spinner ${sizeClasses[size]}`} />
      {message && (
        <p className="text-gray-600 text-sm animate-pulse">{message}</p>
      )}
    </div>
  );
};

export default LoadingSpinner;
