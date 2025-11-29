/**
 * Drawing Canvas Component
 * 
 * HTML5 Canvas for drawing Urdu characters.
 */

import { useRef, useState, useEffect, useCallback } from 'react';
import type { DrawingCanvasProps } from '../types';

const DrawingCanvas: React.FC<DrawingCanvasProps> = ({
  onSubmit,
  isLoading = false,
  disabled = false,
}) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [isDrawing, setIsDrawing] = useState(false);
  const [brushSize, setBrushSize] = useState(15);
  const [hasContent, setHasContent] = useState(false);

  // Initialize canvas with white background
  const initCanvas = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    // Set white background
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    // Set drawing style
    ctx.strokeStyle = 'black';
    ctx.lineWidth = brushSize;
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
  }, [brushSize]);

  useEffect(() => {
    initCanvas();
  }, [initCanvas]);

  // Update brush size when changed
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (ctx) {
      ctx.lineWidth = brushSize;
    }
  }, [brushSize]);

  const getCoordinates = (e: React.MouseEvent | React.TouchEvent): { x: number; y: number } | null => {
    const canvas = canvasRef.current;
    if (!canvas) return null;

    const rect = canvas.getBoundingClientRect();
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;

    if ('touches' in e) {
      const touch = e.touches[0];
      return {
        x: (touch.clientX - rect.left) * scaleX,
        y: (touch.clientY - rect.top) * scaleY,
      };
    }

    return {
      x: (e.clientX - rect.left) * scaleX,
      y: (e.clientY - rect.top) * scaleY,
    };
  };

  const startDrawing = (e: React.MouseEvent | React.TouchEvent) => {
    if (disabled || isLoading) return;
    
    const canvas = canvasRef.current;
    const ctx = canvas?.getContext('2d');
    const coords = getCoordinates(e);
    
    if (!ctx || !coords) return;

    ctx.beginPath();
    ctx.moveTo(coords.x, coords.y);
    setIsDrawing(true);
    setHasContent(true);
  };

  const draw = (e: React.MouseEvent | React.TouchEvent) => {
    if (!isDrawing || disabled || isLoading) return;

    const canvas = canvasRef.current;
    const ctx = canvas?.getContext('2d');
    const coords = getCoordinates(e);

    if (!ctx || !coords) return;

    ctx.lineTo(coords.x, coords.y);
    ctx.stroke();
  };

  const stopDrawing = () => {
    setIsDrawing(false);
  };

  const clearCanvas = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    setHasContent(false);
  };

  const handleSubmit = () => {
    const canvas = canvasRef.current;
    if (!canvas || !hasContent || isLoading) return;

    const imageData = canvas.toDataURL('image/png');
    onSubmit(imageData);
  };

  return (
    <div className="w-full">
      {/* Canvas Container */}
      <div className="relative">
        <canvas
          ref={canvasRef}
          width={400}
          height={400}
          className={`drawing-canvas w-full max-w-md mx-auto block ${
            disabled || isLoading ? 'opacity-50 cursor-not-allowed' : ''
          }`}
          onMouseDown={startDrawing}
          onMouseMove={draw}
          onMouseUp={stopDrawing}
          onMouseLeave={stopDrawing}
          onTouchStart={startDrawing}
          onTouchMove={draw}
          onTouchEnd={stopDrawing}
        />
        
        {/* Instructions overlay */}
        {!hasContent && (
          <div className="absolute inset-0 flex items-center justify-center pointer-events-none">
            <p className="text-gray-400 text-lg">Draw an Urdu character here</p>
          </div>
        )}
      </div>

      {/* Brush Size Control */}
      <div className="mt-4 flex items-center justify-center space-x-4">
        <label className="text-sm text-gray-600">Brush Size:</label>
        <input
          type="range"
          min="5"
          max="30"
          value={brushSize}
          onChange={(e) => setBrushSize(parseInt(e.target.value))}
          className="w-32"
          disabled={disabled || isLoading}
        />
        <span className="text-sm text-gray-600 w-8">{brushSize}px</span>
      </div>

      {/* Action Buttons */}
      <div className="mt-4 flex justify-center space-x-4">
        <button
          onClick={clearCanvas}
          className="btn-secondary"
          disabled={isLoading || !hasContent}
        >
          Clear
        </button>
        <button
          onClick={handleSubmit}
          className="btn-primary"
          disabled={isLoading || !hasContent}
        >
          {isLoading ? 'Processing...' : 'Predict Character'}
        </button>
      </div>
    </div>
  );
};

export default DrawingCanvas;
