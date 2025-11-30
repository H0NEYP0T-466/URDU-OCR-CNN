"""
Data Preprocessing

Functions for preprocessing the Urdu character dataset.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Tuple

import cv2
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split

# Add parent directory to path for imports
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.logger import setup_logger

logger = setup_logger(name="ml_preprocess", log_level="INFO", log_file="logs/training.log")


def load_dataset(
    data_dir: str,
    image_size: Tuple[int, int] = (64, 64),
) -> Tuple[np.ndarray, np.ndarray, Dict[int, str]]:
    """
    Load and preprocess dataset from directory structure.

    Expected directory structure:
    data_dir/
    ├── character_1/
    │   ├── img001.png
    │   └── ...
    ├── character_2/
    │   └── ...

    Args:
        data_dir: Path to the dataset directory
        image_size: Target image size (width, height)

    Returns:
        Tuple of (images, labels, class_mapping)
    """
    logger.info(f"Loading dataset from: {data_dir}")

    data_path = Path(data_dir)
    if not data_path.exists():
        logger.error(f"Dataset directory not found: {data_dir}")
        raise FileNotFoundError(f"Dataset directory not found: {data_dir}")

    images = []
    labels = []
    class_mapping: Dict[int, str] = {}

    # Get all subdirectories (classes)
    class_dirs = sorted([d for d in data_path.iterdir() if d.is_dir()])
    logger.info(f"Found {len(class_dirs)} classes")

    for class_idx, class_dir in enumerate(class_dirs):
        class_name = class_dir.name
        class_mapping[class_idx] = class_name
        logger.info(f"Processing class {class_idx}: {class_name}")

        # Get all images in the class directory
        image_files = list(class_dir.glob("*.png")) + list(class_dir.glob("*.jpg")) + list(class_dir.glob("*.jpeg")) + list(class_dir.glob("*.bmp"))

        logger.info(f"  Found {len(image_files)} images")

        for img_path in image_files:
            try:
                # Load image
                img = Image.open(img_path)

                # Convert to grayscale
                if img.mode != "L":
                    img = img.convert("L")

                # Resize
                img = img.resize(image_size, Image.Resampling.LANCZOS)

                # Convert to numpy array
                img_array = np.array(img, dtype=np.float32)

                images.append(img_array)
                labels.append(class_idx)

            except Exception as e:
                logger.warning(f"  Failed to load image {img_path}: {str(e)}")

    images = np.array(images)
    labels = np.array(labels)

    logger.info(f"Dataset loaded: {len(images)} images, {len(class_mapping)} classes")
    logger.info(f"Image shape: {images.shape}")

    return images, labels, class_mapping


def load_dataset_with_mapping(
    data_dir: str,
    class_mapping: Dict[int, str],
    image_size: Tuple[int, int] = (64, 64),
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Load dataset using an existing class mapping (for test sets).

    This ensures test set uses the same class indices as the training set.

    Args:
        data_dir: Path to the dataset directory
        class_mapping: Pre-existing class mapping from training set
        image_size: Target image size (width, height)

    Returns:
        Tuple of (images, labels)
    """
    logger.info(f"Loading dataset from: {data_dir} with existing class mapping")

    data_path = Path(data_dir)
    if not data_path.exists():
        logger.error(f"Dataset directory not found: {data_dir}")
        raise FileNotFoundError(f"Dataset directory not found: {data_dir}")

    # Create reverse mapping: class_name -> class_idx
    name_to_idx = {name: idx for idx, name in class_mapping.items()}

    images = []
    labels = []

    # Get all subdirectories (classes)
    class_dirs = sorted([d for d in data_path.iterdir() if d.is_dir()])
    logger.info(f"Found {len(class_dirs)} classes in test set")

    for class_dir in class_dirs:
        class_name = class_dir.name
        if class_name not in name_to_idx:
            logger.warning(f"Skipping unknown class: {class_name}")
            continue

        class_idx = name_to_idx[class_name]
        logger.info(f"Processing class {class_idx}: {class_name}")

        # Get all images in the class directory
        image_files = list(class_dir.glob("*.png")) + list(class_dir.glob("*.jpg")) + list(class_dir.glob("*.jpeg")) + list(class_dir.glob("*.bmp"))

        logger.info(f"  Found {len(image_files)} images")

        for img_path in image_files:
            try:
                # Load image
                img = Image.open(img_path)

                # Convert to grayscale
                if img.mode != "L":
                    img = img.convert("L")

                # Resize
                img = img.resize(image_size, Image.Resampling.LANCZOS)

                # Convert to numpy array
                img_array = np.array(img, dtype=np.float32)

                images.append(img_array)
                labels.append(class_idx)

            except Exception as e:
                logger.warning(f"  Failed to load image {img_path}: {str(e)}")

    images = np.array(images)
    labels = np.array(labels)

    logger.info(f"Dataset loaded: {len(images)} images")
    logger.info(f"Image shape: {images.shape}")

    return images, labels


def load_split_dataset(
    train_dir: str,
    test_dir: str,
    image_size: Tuple[int, int] = (64, 64),
    val_ratio: float = 0.15,
    random_state: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, Dict[int, str]]:
    """
    Load dataset from separate train and test directories.

    Expected directory structure:
    train_dir/
    ├── class_1/
    │   ├── img001.png
    │   └── ...
    ├── class_2/
    │   └── ...
    test_dir/
    ├── class_1/
    │   ├── img001.png
    │   └── ...
    ├── class_2/
    │   └── ...

    Args:
        train_dir: Path to the training dataset directory
        test_dir: Path to the test dataset directory
        image_size: Target image size (width, height)
        val_ratio: Ratio of training data to use for validation
        random_state: Random seed for reproducibility

    Returns:
        Tuple of (X_train, X_val, X_test, y_train, y_val, y_test, class_mapping)
        Returns empty arrays and empty mapping if no data is found.
    """
    logger.info("=" * 60)
    logger.info("Loading split dataset")
    logger.info(f"Train directory: {train_dir}")
    logger.info(f"Test directory: {test_dir}")
    logger.info("=" * 60)

    # Load training data and get class mapping
    train_images, train_labels, class_mapping = load_dataset(train_dir, image_size)

    # Check if we actually loaded any data
    if len(train_images) == 0 or len(class_mapping) == 0:
        logger.warning("No training images found!")
        # Return empty arrays with the correct structure
        empty_images = np.array([]).reshape(0, image_size[0], image_size[1], 1)
        empty_labels = np.array([], dtype=np.int64)
        return empty_images, empty_images, empty_images, empty_labels, empty_labels, empty_labels, class_mapping

    # Load test data using the same class mapping
    test_images, test_labels = load_dataset_with_mapping(test_dir, class_mapping, image_size)

    # Preprocess images
    train_images = preprocess_images(train_images)
    test_images = preprocess_images(test_images)

    # Split training data into train and validation sets
    X_train, X_val, y_train, y_val = train_test_split(
        train_images, train_labels,
        test_size=val_ratio,
        random_state=random_state,
        stratify=train_labels,
    )

    logger.info(f"Train set: {len(X_train)} samples")
    logger.info(f"Validation set: {len(X_val)} samples")
    logger.info(f"Test set: {len(test_images)} samples")

    return X_train, X_val, test_images, y_train, y_val, test_labels, class_mapping


def get_dataset_paths(base_dir: str, dataset_type: str = "characters") -> Tuple[str, str]:
    """
    Get train and test directory paths based on dataset type.

    Args:
        base_dir: Base directory containing the raw data (e.g., 'data/raw')
        dataset_type: Type of dataset ('characters' or 'digits')

    Returns:
        Tuple of (train_dir, test_dir)
    """
    base_path = Path(base_dir)

    if dataset_type == "characters":
        train_dir = base_path / "characters_train_set"
        test_dir = base_path / "characters_test_set"
    elif dataset_type == "digits":
        train_dir = base_path / "digits_train_set"
        test_dir = base_path / "digits_test_set"
    else:
        raise ValueError(f"Unknown dataset type: {dataset_type}. Use 'characters' or 'digits'.")

    return str(train_dir), str(test_dir)


def check_dataset_structure(base_dir: str) -> Dict[str, bool]:
    """
    Check which dataset directories exist.

    Args:
        base_dir: Base directory containing the raw data

    Returns:
        Dictionary indicating which datasets are available
    """
    base_path = Path(base_dir)

    datasets = {
        "characters_train": (base_path / "characters_train_set").exists(),
        "characters_test": (base_path / "characters_test_set").exists(),
        "digits_train": (base_path / "digits_train_set").exists(),
        "digits_test": (base_path / "digits_test_set").exists(),
    }

    logger.info("Dataset structure check:")
    for name, exists in datasets.items():
        status = "✓" if exists else "✗"
        logger.info(f"  {status} {name}")

    return datasets


def preprocess_images(images: np.ndarray) -> np.ndarray:
    """
    Preprocess images for model training.

    Steps:
    1. Normalize pixel values to [0, 1]
    2. Add channel dimension

    Args:
        images: Array of images with shape (N, H, W)

    Returns:
        Preprocessed images with shape (N, H, W, 1)
    """
    logger.info("Preprocessing images...")
    logger.info(f"Input shape: {images.shape}")

    # Normalize to [0, 1]
    images = images / 255.0
    logger.info("Normalized pixel values to [0, 1]")

    # Add channel dimension
    images = np.expand_dims(images, axis=-1)
    logger.info(f"Output shape: {images.shape}")

    return images


def split_dataset(
    images: np.ndarray,
    labels: np.ndarray,
    train_ratio: float = 0.7,
    val_ratio: float = 0.15,
    test_ratio: float = 0.15,
    random_state: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Split dataset into train, validation, and test sets.

    Args:
        images: Image data
        labels: Label data
        train_ratio: Ratio for training set
        val_ratio: Ratio for validation set
        test_ratio: Ratio for test set
        random_state: Random seed for reproducibility

    Returns:
        Tuple of (X_train, X_val, X_test, y_train, y_val, y_test)
    """
    logger.info("Splitting dataset...")
    logger.info(f"Ratios - Train: {train_ratio}, Val: {val_ratio}, Test: {test_ratio}")

    # First split: train vs (val + test)
    X_train, X_temp, y_train, y_temp = train_test_split(
        images, labels,
        test_size=(val_ratio + test_ratio),
        random_state=random_state,
        stratify=labels,
    )

    # Second split: val vs test
    val_test_ratio = test_ratio / (val_ratio + test_ratio)
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp,
        test_size=val_test_ratio,
        random_state=random_state,
        stratify=y_temp,
    )

    logger.info(f"Train set: {len(X_train)} samples")
    logger.info(f"Validation set: {len(X_val)} samples")
    logger.info(f"Test set: {len(X_test)} samples")

    return X_train, X_val, X_test, y_train, y_val, y_test


def save_class_mapping(class_mapping: Dict[int, str], output_path: str) -> None:
    """
    Save class mapping to JSON file.

    Args:
        class_mapping: Dictionary mapping indices to class names
        output_path: Path to save the JSON file
    """
    logger.info(f"Saving class mapping to: {output_path}")

    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(class_mapping, f, ensure_ascii=False, indent=2)

    logger.info(f"Saved {len(class_mapping)} class labels")


def save_processed_data(
    X_train: np.ndarray,
    X_val: np.ndarray,
    X_test: np.ndarray,
    y_train: np.ndarray,
    y_val: np.ndarray,
    y_test: np.ndarray,
    output_dir: str,
) -> None:
    """
    Save processed data to numpy files.

    Args:
        X_train, X_val, X_test: Image data splits
        y_train, y_val, y_test: Label data splits
        output_dir: Directory to save files
    """
    logger.info(f"Saving processed data to: {output_dir}")

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    np.save(output_path / "X_train.npy", X_train)
    np.save(output_path / "X_val.npy", X_val)
    np.save(output_path / "X_test.npy", X_test)
    np.save(output_path / "y_train.npy", y_train)
    np.save(output_path / "y_val.npy", y_val)
    np.save(output_path / "y_test.npy", y_test)

    logger.info("Processed data saved successfully")


def load_processed_data(data_dir: str) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Load processed data from numpy files.

    Args:
        data_dir: Directory containing processed data

    Returns:
        Tuple of (X_train, X_val, X_test, y_train, y_val, y_test)
    """
    logger.info(f"Loading processed data from: {data_dir}")

    data_path = Path(data_dir)

    X_train = np.load(data_path / "X_train.npy")
    X_val = np.load(data_path / "X_val.npy")
    X_test = np.load(data_path / "X_test.npy")
    y_train = np.load(data_path / "y_train.npy")
    y_val = np.load(data_path / "y_val.npy")
    y_test = np.load(data_path / "y_test.npy")

    logger.info(f"Loaded - Train: {len(X_train)}, Val: {len(X_val)}, Test: {len(X_test)}")

    return X_train, X_val, X_test, y_train, y_val, y_test


if __name__ == "__main__":
    # Example usage
    import argparse

    parser = argparse.ArgumentParser(description="Preprocess Urdu character dataset")
    parser.add_argument("--data-dir", type=str, default="data/raw", help="Path to raw dataset base directory")
    parser.add_argument("--output-dir", type=str, default="data/processed", help="Path to save processed data")
    parser.add_argument("--image-size", type=int, default=64, help="Target image size")
    parser.add_argument("--dataset-type", type=str, default="characters",
                       choices=["characters", "digits"], help="Dataset type to preprocess")
    parser.add_argument("--use-split", action="store_true",
                       help="Use separate train/test directories (characters_train_set, etc.)")

    args = parser.parse_args()

    # Check dataset structure
    check_dataset_structure(args.data_dir)

    if args.use_split:
        # Use separate train/test directories
        train_dir, test_dir = get_dataset_paths(args.data_dir, args.dataset_type)
        logger.info(f"Using split dataset: {args.dataset_type}")

        X_train, X_val, X_test, y_train, y_val, y_test, class_mapping = load_split_dataset(
            train_dir, test_dir,
            image_size=(args.image_size, args.image_size),
        )
    else:
        # Legacy mode: single directory
        logger.info("Using legacy single-directory mode")
        images, labels, class_mapping = load_dataset(args.data_dir, (args.image_size, args.image_size))
        images = preprocess_images(images)
        X_train, X_val, X_test, y_train, y_val, y_test = split_dataset(images, labels)

    # Create output directory based on dataset type
    output_dir = Path(args.output_dir) / args.dataset_type if args.use_split else Path(args.output_dir)

    # Save
    save_processed_data(X_train, X_val, X_test, y_train, y_val, y_test, str(output_dir))
    save_class_mapping(class_mapping, str(output_dir / "class_labels.json"))

    logger.info("Preprocessing complete!")
