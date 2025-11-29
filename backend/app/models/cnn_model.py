"""
CNN Model Architecture

Defines the Convolutional Neural Network architecture for Urdu character recognition.
"""

from typing import Tuple

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, Model

from app.logger import get_logger

logger = get_logger(__name__)


def create_cnn_model(
    input_shape: Tuple[int, int, int] = (64, 64, 1),
    num_classes: int = 46,
) -> Model:
    """
    Create a CNN model for Urdu character recognition.

    Architecture:
    - Input Layer: (64, 64, 1) grayscale images
    - Conv2D(32, 3x3) -> BatchNorm -> ReLU -> MaxPool(2x2) -> Dropout(0.25)
    - Conv2D(64, 3x3) -> BatchNorm -> ReLU -> MaxPool(2x2) -> Dropout(0.25)
    - Conv2D(128, 3x3) -> BatchNorm -> ReLU -> MaxPool(2x2) -> Dropout(0.25)
    - Conv2D(256, 3x3) -> BatchNorm -> ReLU -> MaxPool(2x2) -> Dropout(0.25)
    - Flatten
    - Dense(512) -> BatchNorm -> ReLU -> Dropout(0.5)
    - Dense(256) -> BatchNorm -> ReLU -> Dropout(0.5)
    - Dense(num_classes, softmax)

    Args:
        input_shape: Shape of input images (height, width, channels)
        num_classes: Number of output classes

    Returns:
        Compiled Keras model
    """
    logger.info(f"Creating CNN model with input shape: {input_shape}")
    logger.info(f"Number of output classes: {num_classes}")

    inputs = keras.Input(shape=input_shape, name="input_layer")

    # First Convolutional Block
    x = layers.Conv2D(32, (3, 3), padding="same", name="conv1")(inputs)
    x = layers.BatchNormalization(name="bn1")(x)
    x = layers.Activation("relu", name="relu1")(x)
    x = layers.MaxPooling2D(pool_size=(2, 2), name="pool1")(x)
    x = layers.Dropout(0.25, name="dropout1")(x)

    # Second Convolutional Block
    x = layers.Conv2D(64, (3, 3), padding="same", name="conv2")(x)
    x = layers.BatchNormalization(name="bn2")(x)
    x = layers.Activation("relu", name="relu2")(x)
    x = layers.MaxPooling2D(pool_size=(2, 2), name="pool2")(x)
    x = layers.Dropout(0.25, name="dropout2")(x)

    # Third Convolutional Block
    x = layers.Conv2D(128, (3, 3), padding="same", name="conv3")(x)
    x = layers.BatchNormalization(name="bn3")(x)
    x = layers.Activation("relu", name="relu3")(x)
    x = layers.MaxPooling2D(pool_size=(2, 2), name="pool3")(x)
    x = layers.Dropout(0.25, name="dropout3")(x)

    # Fourth Convolutional Block
    x = layers.Conv2D(256, (3, 3), padding="same", name="conv4")(x)
    x = layers.BatchNormalization(name="bn4")(x)
    x = layers.Activation("relu", name="relu4")(x)
    x = layers.MaxPooling2D(pool_size=(2, 2), name="pool4")(x)
    x = layers.Dropout(0.25, name="dropout4")(x)

    # Flatten
    x = layers.Flatten(name="flatten")(x)

    # First Dense Block
    x = layers.Dense(512, name="dense1")(x)
    x = layers.BatchNormalization(name="bn_dense1")(x)
    x = layers.Activation("relu", name="relu_dense1")(x)
    x = layers.Dropout(0.5, name="dropout_dense1")(x)

    # Second Dense Block
    x = layers.Dense(256, name="dense2")(x)
    x = layers.BatchNormalization(name="bn_dense2")(x)
    x = layers.Activation("relu", name="relu_dense2")(x)
    x = layers.Dropout(0.5, name="dropout_dense2")(x)

    # Output Layer
    outputs = layers.Dense(num_classes, activation="softmax", name="output")(x)

    model = Model(inputs=inputs, outputs=outputs, name="urdu_cnn_model")

    logger.info("CNN model created successfully")
    logger.info("Model architecture summary:")

    # Print model summary to logger
    model.summary(print_fn=lambda x: logger.info(x))

    return model


def compile_model(
    model: Model,
    learning_rate: float = 0.001,
) -> Model:
    """
    Compile the model with optimizer, loss, and metrics.

    Args:
        model: Keras model to compile
        learning_rate: Initial learning rate for Adam optimizer

    Returns:
        Compiled model
    """
    logger.info(f"Compiling model with learning rate: {learning_rate}")

    optimizer = keras.optimizers.Adam(learning_rate=learning_rate)

    model.compile(
        optimizer=optimizer,
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )

    logger.info("Model compiled successfully")
    return model


def get_callbacks(
    model_checkpoint_path: str = "saved_models/urdu_cnn_model.h5",
    log_dir: str = "logs/tensorboard",
    patience_early_stopping: int = 10,
    patience_reduce_lr: int = 5,
) -> list:
    """
    Get training callbacks.

    Args:
        model_checkpoint_path: Path to save the best model
        log_dir: Directory for TensorBoard logs
        patience_early_stopping: Patience for early stopping
        patience_reduce_lr: Patience for learning rate reduction

    Returns:
        List of Keras callbacks
    """
    logger.info("Setting up training callbacks")

    callbacks = [
        # Early stopping
        keras.callbacks.EarlyStopping(
            monitor="val_loss",
            patience=patience_early_stopping,
            restore_best_weights=True,
            verbose=1,
        ),
        # Model checkpoint
        keras.callbacks.ModelCheckpoint(
            model_checkpoint_path,
            monitor="val_accuracy",
            save_best_only=True,
            verbose=1,
        ),
        # Reduce learning rate on plateau
        keras.callbacks.ReduceLROnPlateau(
            monitor="val_loss",
            factor=0.5,
            patience=patience_reduce_lr,
            min_lr=1e-7,
            verbose=1,
        ),
        # TensorBoard
        keras.callbacks.TensorBoard(
            log_dir=log_dir,
            histogram_freq=1,
        ),
    ]

    logger.info(f"Callbacks configured: EarlyStopping, ModelCheckpoint, ReduceLROnPlateau, TensorBoard")
    return callbacks


def load_model(model_path: str) -> Model:
    """
    Load a trained model from file.

    Args:
        model_path: Path to the saved model file

    Returns:
        Loaded Keras model
    """
    logger.info(f"Loading model from: {model_path}")

    model = keras.models.load_model(model_path)

    logger.info("Model loaded successfully")
    logger.info(f"Model input shape: {model.input_shape}")
    logger.info(f"Model output shape: {model.output_shape}")

    return model
