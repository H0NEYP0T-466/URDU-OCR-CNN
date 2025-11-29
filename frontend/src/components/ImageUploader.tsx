/**
 * Image Uploader Component
 * 
 * Drag and drop zone for image upload with preview.
 */

import { useCallback, useState } from 'react';
import { useDropzone } from 'react-dropzone';
import { validateImage, createImagePreview, revokeImagePreview, formatFileSize } from '../utils/imageUtils';
import type { ImageUploaderProps } from '../types';

const ImageUploader: React.FC<ImageUploaderProps> = ({ 
  onImageSelect, 
  isLoading = false,
  disabled = false 
}) => {
  const [preview, setPreview] = useState<string | null>(null);
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [error, setError] = useState<string | null>(null);

  const onDrop = useCallback((acceptedFiles: File[]) => {
    const file = acceptedFiles[0];
    if (!file) return;

    // Validate file
    const validation = validateImage(file);
    if (!validation.valid) {
      setError(validation.error || 'Invalid file');
      return;
    }

    // Clear previous preview
    if (preview) {
      revokeImagePreview(preview);
    }

    // Set new preview and file
    setError(null);
    setSelectedFile(file);
    setPreview(createImagePreview(file));
  }, [preview]);

  const handleSubmit = useCallback(() => {
    if (selectedFile && !isLoading) {
      onImageSelect(selectedFile);
    }
  }, [selectedFile, isLoading, onImageSelect]);

  const handleClear = useCallback(() => {
    if (preview) {
      revokeImagePreview(preview);
    }
    setPreview(null);
    setSelectedFile(null);
    setError(null);
  }, [preview]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'image/png': ['.png'],
      'image/jpeg': ['.jpg', '.jpeg'],
      'image/bmp': ['.bmp'],
    },
    maxFiles: 1,
    disabled: disabled || isLoading,
  });

  return (
    <div className="w-full">
      {/* Drop Zone */}
      <div
        {...getRootProps()}
        className={`dropzone ${isDragActive ? 'active' : ''} ${
          disabled || isLoading ? 'opacity-50 cursor-not-allowed' : ''
        }`}
      >
        <input {...getInputProps()} />
        
        {preview ? (
          <div className="flex flex-col items-center">
            <img
              src={preview}
              alt="Preview"
              className="max-h-48 max-w-full rounded-lg mb-4 shadow-md"
            />
            <p className="text-sm text-gray-600">{selectedFile?.name}</p>
            <p className="text-xs text-gray-500">{selectedFile && formatFileSize(selectedFile.size)}</p>
          </div>
        ) : (
          <div className="flex flex-col items-center">
            <svg
              className="w-16 h-16 text-gray-400 mb-4"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
              />
            </svg>
            <p className="text-lg text-gray-600 mb-2">
              {isDragActive ? 'Drop the image here...' : 'Drag & drop an image here'}
            </p>
            <p className="text-sm text-gray-500">or click to select a file</p>
            <p className="text-xs text-gray-400 mt-2">PNG, JPG, JPEG, BMP (max 5MB)</p>
          </div>
        )}
      </div>

      {/* Error Message */}
      {error && (
        <div className="mt-3 p-3 bg-red-50 border border-red-200 rounded-lg">
          <p className="text-red-600 text-sm">{error}</p>
        </div>
      )}

      {/* Action Buttons */}
      {preview && (
        <div className="mt-4 flex justify-center space-x-4">
          <button
            onClick={handleClear}
            className="btn-secondary"
            disabled={isLoading}
          >
            Clear
          </button>
          <button
            onClick={handleSubmit}
            className="btn-primary"
            disabled={isLoading}
          >
            {isLoading ? 'Processing...' : 'Predict Character'}
          </button>
        </div>
      )}
    </div>
  );
};

export default ImageUploader;
