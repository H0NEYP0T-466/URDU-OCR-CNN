"""
Data Augmentation

Functions for data augmentation to improve model training.
"""

from typing import Tuple

import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.logger import setup_logger

logger = setup_logger(name="ml_augmentation", log_level="INFO", log_file="logs/training.log")


def create_data_generator(
    rotation_range: int = 15,
    width_shift_range: float = 0.1,
    height_shift_range: float = 0.1,
    zoom_range: float = 0.1,
    shear_range: float = 0.1,
    horizontal_flip: bool = False,
    vertical_flip: bool = False,
    fill_mode: str = "nearest",
) -> ImageDataGenerator:
    """
    Create a data generator with augmentation settings.

    Args:
        rotation_range: Degree range for random rotations
        width_shift_range: Fraction of total width for random horizontal shifts
        height_shift_range: Fraction of total height for random vertical shifts
        zoom_range: Range for random zoom
        shear_range: Shear intensity
        horizontal_flip: Whether to flip horizontally (usually False for text)
        vertical_flip: Whether to flip vertically (usually False for text)
        fill_mode: Points outside boundaries fill mode

    Returns:
        Configured ImageDataGenerator
    """
    logger.info("Creating data generator with augmentation settings:")
    logger.info(f"  rotation_range: {rotation_range}")
    logger.info(f"  width_shift_range: {width_shift_range}")
    logger.info(f"  height_shift_range: {height_shift_range}")
    logger.info(f"  zoom_range: {zoom_range}")
    logger.info(f"  shear_range: {shear_range}")
    logger.info(f"  horizontal_flip: {horizontal_flip}")
    logger.info(f"  vertical_flip: {vertical_flip}")

    datagen = ImageDataGenerator(
        rotation_range=rotation_range,
        width_shift_range=width_shift_range,
        height_shift_range=height_shift_range,
        zoom_range=zoom_range,
        shear_range=shear_range,
        horizontal_flip=horizontal_flip,
        vertical_flip=vertical_flip,
        fill_mode=fill_mode,
    )

    logger.info("Data generator created successfully")
    return datagen


def create_validation_generator() -> ImageDataGenerator:
    """
    Create a data generator for validation data (no augmentation).

    Returns:
        ImageDataGenerator with no augmentation
    """
    logger.info("Creating validation data generator (no augmentation)")
    return ImageDataGenerator()


def augment_dataset(
    images: np.ndarray,
    labels: np.ndarray,
    augmentation_factor: int = 2,
    datagen: ImageDataGenerator = None,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Augment dataset by generating additional samples.

    Args:
        images: Original image data
        labels: Original labels
        augmentation_factor: Number of augmented samples per original sample
        datagen: ImageDataGenerator to use for augmentation

    Returns:
        Tuple of (augmented_images, augmented_labels)
    """
    logger.info(f"Augmenting dataset with factor: {augmentation_factor}")
    logger.info(f"Original dataset size: {len(images)}")

    if datagen is None:
        datagen = create_data_generator()

    augmented_images = []
    augmented_labels = []

    # Add original images
    augmented_images.extend(images)
    augmented_labels.extend(labels)

    # Generate augmented images
    for i, (img, label) in enumerate(zip(images, labels)):
        # Reshape for generator (needs batch dimension)
        img_batch = np.expand_dims(img, axis=0)

        # Generate augmented samples
        aug_iter = datagen.flow(img_batch, batch_size=1)

        for _ in range(augmentation_factor - 1):  # -1 because original is already added
            aug_img = next(aug_iter)[0]
            augmented_images.append(aug_img)
            augmented_labels.append(label)

        if (i + 1) % 1000 == 0:
            logger.info(f"  Processed {i + 1}/{len(images)} images")

    augmented_images = np.array(augmented_images)
    augmented_labels = np.array(augmented_labels)

    logger.info(f"Augmented dataset size: {len(augmented_images)}")

    return augmented_images, augmented_labels


def get_training_generator(
    X_train: np.ndarray,
    y_train: np.ndarray,
    batch_size: int = 32,
    datagen: ImageDataGenerator = None,
):
    """
    Get a training data generator for model.fit().

    Args:
        X_train: Training images
        y_train: Training labels
        batch_size: Batch size for training
        datagen: ImageDataGenerator for augmentation

    Returns:
        Data generator for training
    """
    logger.info(f"Creating training generator with batch_size: {batch_size}")

    if datagen is None:
        datagen = create_data_generator()

    return datagen.flow(X_train, y_train, batch_size=batch_size)
