/**
 * TypeScript interfaces for the Urdu Character Recognition application
 */

export interface TopPrediction {
  character: string;
  probability: number;
}

export interface PredictionResponse {
  prediction: string;
  confidence: number;
  top_5: TopPrediction[];
  processing_time_ms: number;
}

export interface HealthResponse {
  status: string;
  model_loaded: boolean;
  version: string;
}

export interface ClassesResponse {
  classes: string[];
  count: number;
}

export interface ErrorResponse {
  detail: string;
  error_type?: string;
}

export interface PredictionState {
  isLoading: boolean;
  error: string | null;
  result: PredictionResponse | null;
}

export interface CanvasDrawingState {
  isDrawing: boolean;
  brushSize: number;
  brushColor: string;
}

export interface ImageUploaderProps {
  onImageSelect: (file: File) => void;
  isLoading?: boolean;
  disabled?: boolean;
}

export interface PredictionResultProps {
  result: PredictionResponse | null;
  isLoading: boolean;
  error: string | null;
  onReset: () => void;
}

export interface DrawingCanvasProps {
  onSubmit: (imageData: string) => void;
  isLoading?: boolean;
  disabled?: boolean;
}

export interface HeaderProps {
  title?: string;
}

export interface FooterProps {
  year?: number;
}
