/**
 * Custom hook for prediction functionality
 */

import { useState, useCallback } from 'react';
import type { PredictionResponse, PredictionState } from '../types';
import { predictFromImage, predictFromCanvas } from '../services/api';

export interface UsePredictionReturn {
  state: PredictionState;
  predictImage: (file: File) => Promise<void>;
  predictCanvas: (imageData: string) => Promise<void>;
  reset: () => void;
}

const initialState: PredictionState = {
  isLoading: false,
  error: null,
  result: null,
};

export const usePrediction = (): UsePredictionReturn => {
  const [state, setState] = useState<PredictionState>(initialState);

  const predictImage = useCallback(async (file: File) => {
    setState({ isLoading: true, error: null, result: null });
    
    try {
      const result = await predictFromImage(file);
      setState({ isLoading: false, error: null, result });
    } catch (error) {
      setState({ 
        isLoading: false, 
        error: error instanceof Error ? error.message : 'Prediction failed',
        result: null 
      });
    }
  }, []);

  const predictCanvas = useCallback(async (imageData: string) => {
    setState({ isLoading: true, error: null, result: null });
    
    try {
      const result = await predictFromCanvas(imageData);
      setState({ isLoading: false, error: null, result });
    } catch (error) {
      setState({ 
        isLoading: false, 
        error: error instanceof Error ? error.message : 'Prediction failed',
        result: null 
      });
    }
  }, []);

  const reset = useCallback(() => {
    setState(initialState);
  }, []);

  return {
    state,
    predictImage,
    predictCanvas,
    reset,
  };
};

export default usePrediction;
