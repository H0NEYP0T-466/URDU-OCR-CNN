# Model Architecture Documentation

## Overview

The Urdu Character Recognition model is a Convolutional Neural Network (CNN) designed to recognize handwritten Urdu characters and digits.

## Model Architecture

### Input
- **Shape**: (64, 64, 1)
- **Format**: Grayscale images normalized to [0, 1]

### Convolutional Blocks

The model consists of 4 convolutional blocks, each with:
- Conv2D layer
- Batch Normalization
- ReLU Activation
- Max Pooling (2×2)
- Dropout (0.25)

| Block | Filters | Kernel | Output Shape |
|-------|---------|--------|--------------|
| 1 | 32 | 3×3 | (32, 32, 32) |
| 2 | 64 | 3×3 | (16, 16, 64) |
| 3 | 128 | 3×3 | (8, 8, 128) |
| 4 | 256 | 3×3 | (4, 4, 256) |

### Dense Layers

After flattening:

| Layer | Units | Dropout |
|-------|-------|---------|
| Dense 1 | 512 | 0.5 |
| Dense 2 | 256 | 0.5 |
| Output | 46 | - |

### Output
- **Activation**: Softmax
- **Classes**: 46 (36 alphabets + 10 digits)

## Architecture Diagram

```
Input (64×64×1)
      │
      ▼
┌─────────────────────────────────────┐
│  Conv2D(32, 3×3) → BN → ReLU       │
│  MaxPool(2×2) → Dropout(0.25)       │
└─────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────┐
│  Conv2D(64, 3×3) → BN → ReLU       │
│  MaxPool(2×2) → Dropout(0.25)       │
└─────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────┐
│  Conv2D(128, 3×3) → BN → ReLU      │
│  MaxPool(2×2) → Dropout(0.25)       │
└─────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────┐
│  Conv2D(256, 3×3) → BN → ReLU      │
│  MaxPool(2×2) → Dropout(0.25)       │
└─────────────────────────────────────┘
      │
      ▼
    Flatten
      │
      ▼
┌─────────────────────────────────────┐
│  Dense(512) → BN → ReLU → Drop(0.5)│
└─────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────┐
│  Dense(256) → BN → ReLU → Drop(0.5)│
└─────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────┐
│  Dense(46) → Softmax               │
└─────────────────────────────────────┘
      │
      ▼
Output (46 classes)
```

## Training Configuration

### Optimizer
- **Type**: Adam
- **Initial Learning Rate**: 0.001
- **Learning Rate Schedule**: ReduceLROnPlateau
  - Factor: 0.5
  - Patience: 5 epochs
  - Min LR: 1e-7

### Loss Function
- Categorical Cross-entropy

### Callbacks
1. **EarlyStopping**
   - Monitor: val_loss
   - Patience: 10 epochs
   - Restore best weights: Yes

2. **ModelCheckpoint**
   - Monitor: val_accuracy
   - Save best only: Yes

3. **ReduceLROnPlateau**
   - Monitor: val_loss
   - Factor: 0.5
   - Patience: 5

4. **TensorBoard**
   - Histogram frequency: 1

## Data Augmentation

The following augmentations are applied during training:

| Augmentation | Value |
|--------------|-------|
| Rotation | ±15° |
| Width Shift | 10% |
| Height Shift | 10% |
| Zoom | 10% |
| Shear | 10% |
| Horizontal Flip | No |
| Vertical Flip | No |

## Supported Characters

### Urdu Alphabets (36)
ا ب پ ت ٹ ث ج چ ح خ د ڈ ذ ر ڑ ز ژ س ش ص ض ط ظ ع غ ف ق ک گ ل م ن و ہ ی ے

### Urdu Digits (10)
۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹

## Model Files

| File | Description |
|------|-------------|
| `urdu_cnn_model.h5` | Trained model weights |
| `class_labels.json` | Class index to character mapping |
| `training_history.json` | Training metrics history |

## Performance Metrics

Performance depends on the training dataset. Expected metrics with proper training:

| Metric | Expected Value |
|--------|----------------|
| Training Accuracy | ~98% |
| Validation Accuracy | ~95% |
| Test Accuracy | ~94% |

## Usage

### Loading the Model

```python
from tensorflow import keras

model = keras.models.load_model('saved_models/urdu_cnn_model.h5')
```

### Making Predictions

```python
import numpy as np
from PIL import Image

# Load and preprocess image
img = Image.open('character.png').convert('L')
img = img.resize((64, 64))
img_array = np.array(img) / 255.0
img_array = img_array.reshape(1, 64, 64, 1)

# Predict
predictions = model.predict(img_array)
predicted_class = np.argmax(predictions[0])
confidence = predictions[0][predicted_class]
```
