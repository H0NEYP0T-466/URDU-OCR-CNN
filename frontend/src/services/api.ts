/**
 * API Service
 * 
 * Axios-based API calls for the Urdu Character Recognition backend.
 */

import axios, { AxiosError } from 'axios';
import type { 
  PredictionResponse, 
  HealthResponse, 
  ClassesResponse, 
  ErrorResponse 
} from '../types';

// API base URL - use environment variable or default to localhost
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

// Create axios instance with default config
const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 30000, // 30 second timeout for predictions
  headers: {
    'Accept': 'application/json',
  },
});

/**
 * Handle API errors and return user-friendly messages
 */
const handleApiError = (error: unknown): string => {
  if (axios.isAxiosError(error)) {
    const axiosError = error as AxiosError<ErrorResponse>;
    
    if (axiosError.response?.data?.detail) {
      return axiosError.response.data.detail;
    }
    
    if (axiosError.code === 'ECONNREFUSED') {
      return 'Unable to connect to the server. Please ensure the backend is running.';
    }
    
    if (axiosError.code === 'ETIMEDOUT') {
      return 'Request timed out. Please try again.';
    }
    
    return axiosError.message || 'An unexpected error occurred';
  }
  
  return 'An unexpected error occurred';
};

/**
 * Predict character from uploaded image file
 */
export const predictFromImage = async (file: File): Promise<PredictionResponse> => {
  const formData = new FormData();
  formData.append('file', file);

  try {
    const response = await api.post<PredictionResponse>('/api/v1/predict', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  } catch (error) {
    throw new Error(handleApiError(error));
  }
};

/**
 * Predict character from canvas drawing (base64 encoded)
 */
export const predictFromCanvas = async (imageData: string): Promise<PredictionResponse> => {
  try {
    const response = await api.post<PredictionResponse>('/api/v1/predict/canvas', {
      image_data: imageData,
    });
    return response.data;
  } catch (error) {
    throw new Error(handleApiError(error));
  }
};

/**
 * Check API health status
 */
export const healthCheck = async (): Promise<HealthResponse> => {
  try {
    const response = await api.get<HealthResponse>('/health');
    return response.data;
  } catch (error) {
    throw new Error(handleApiError(error));
  }
};

/**
 * Get list of supported character classes
 */
export const getClasses = async (): Promise<string[]> => {
  try {
    const response = await api.get<ClassesResponse>('/api/v1/classes');
    return response.data.classes;
  } catch (error) {
    throw new Error(handleApiError(error));
  }
};

export default api;
