/**
 * Custom hook for prediction functionality
 */

import { useState, useCallback } from 'react';
import type { PredictionState } from '../types';
import { 
  predictFromImage, 
  predictFromCanvas,
  predictDigitFromImage,
  predictDigitFromCanvas
} from '../services/api';

export type ModelType = 'character' | 'digit';

export interface UsePredictionReturn {
  state: PredictionState;
  predictImage: (file: File, modelType?: ModelType) => Promise<void>;
  predictCanvas: (imageData: string, modelType?: ModelType) => Promise<void>;
  reset: () => void;
}

const initialState: PredictionState = {
  isLoading: false,
  error: null,
  result: null,
};

export const usePrediction = (): UsePredictionReturn => {
  const [state, setState] = useState<PredictionState>(initialState);

  const predictImage = useCallback(async (file: File, modelType: ModelType = 'character') => {
    setState({ isLoading: true, error: null, result: null });
    
    try {
      const predictFn = modelType === 'digit' ? predictDigitFromImage : predictFromImage;
      const result = await predictFn(file);
      setState({ isLoading: false, error: null, result });
    } catch (error) {
      setState({ 
        isLoading: false, 
        error: error instanceof Error ? error.message : 'Prediction failed',
        result: null 
      });
    }
  }, []);

  const predictCanvas = useCallback(async (imageData: string, modelType: ModelType = 'character') => {
    setState({ isLoading: true, error: null, result: null });
    
    try {
      const predictFn = modelType === 'digit' ? predictDigitFromCanvas : predictFromCanvas;
      const result = await predictFn(imageData);
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
