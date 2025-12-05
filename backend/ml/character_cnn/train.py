"""
Model Training Script

Script to train the CNN model for Urdu character recognition.
"""

import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

import numpy as np
from tensorflow import keras
from tensorflow.keras.utils import to_categorical

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.config import URDU_CHARACTERS
from app.logger import setup_logger
from app.models.cnn_model import compile_model, create_cnn_model, get_callbacks
from ml.augmentation import create_data_generator, get_training_generator
from ml.preprocess import (
    check_dataset_structure,
    get_dataset_paths,
    load_dataset,
    load_processed_data,
    load_split_dataset,
    preprocess_images,
    save_class_mapping,
    save_processed_data,
    split_dataset,
)

logger = setup_logger(name="ml_train", log_level="INFO", log_file="logs/training.log")


def train_model(
    data_dir: str = "data/raw",
    processed_dir: str = "data/processed",
    model_save_path: str = "saved_models/urdu_cnn_model.h5",
    class_labels_path: str = "saved_models/class_labels.json",
    image_size: int = 64,
    batch_size: int = 32,
    epochs: int = 100,
    learning_rate: float = 0.001,
    use_augmentation: bool = True,
    use_processed: bool = False,
    dataset_type: str = "characters",
    use_split_dirs: bool = True,
) -> None:
    """
    Train the CNN model for Urdu character recognition.

    Args:
        data_dir: Path to raw dataset base directory
        processed_dir: Path to save/load processed data
        model_save_path: Path to save the trained model
        class_labels_path: Path to save class labels
        image_size: Target image size
        batch_size: Training batch size
        epochs: Maximum number of epochs
        learning_rate: Initial learning rate
        use_augmentation: Whether to use data augmentation
        use_processed: Whether to load pre-processed data
        dataset_type: Type of dataset ('characters' or 'digits')
        use_split_dirs: Whether to use separate train/test directories
    """
    logger.info("=" * 60)
    logger.info("URDU CHARACTER RECOGNITION MODEL TRAINING")
    logger.info("=" * 60)

    start_time = time.time()
    logger.info(f"Training started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Log training configuration
    logger.info("Training Configuration:")
    logger.info(f"  Data directory: {data_dir}")
    logger.info(f"  Processed directory: {processed_dir}")
    logger.info(f"  Model save path: {model_save_path}")
    logger.info(f"  Image size: {image_size}x{image_size}")
    logger.info(f"  Batch size: {batch_size}")
    logger.info(f"  Max epochs: {epochs}")
    logger.info(f"  Learning rate: {learning_rate}")
    logger.info(f"  Use augmentation: {use_augmentation}")
    logger.info(f"  Dataset type: {dataset_type}")
    logger.info(f"  Use split directories: {use_split_dirs}")

    # Ensure directories exist
    Path(model_save_path).parent.mkdir(parents=True, exist_ok=True)
    Path(processed_dir).mkdir(parents=True, exist_ok=True)

    # Load data
    if use_processed and Path(processed_dir, "X_train.npy").exists():
        logger.info("Loading pre-processed data...")
        X_train, X_val, X_test, y_train, y_val, y_test = load_processed_data(processed_dir)

        # Load class mapping from the processed directory first, then fallback to class_labels_path
        processed_labels_path = Path(processed_dir) / "class_labels.json"
        labels_path = processed_labels_path if processed_labels_path.exists() else class_labels_path

        with open(labels_path, "r", encoding="utf-8") as f:
            class_mapping = {int(k): v for k, v in json.load(f).items()}

    else:
        logger.info("Loading and preprocessing raw data...")

        # Check dataset structure
        datasets_available = check_dataset_structure(data_dir)

        # Check if split directories should be used
        if use_split_dirs:
            train_dir_key = f"{dataset_type}_train"
            test_dir_key = f"{dataset_type}_test"

            if datasets_available.get(train_dir_key) and datasets_available.get(test_dir_key):
                # Use separate train/test directories
                train_dir, test_dir = get_dataset_paths(data_dir, dataset_type)
                logger.info(f"Using split dataset: {dataset_type}")

                X_train, X_val, X_test, y_train, y_val, y_test, class_mapping = load_split_dataset(
                    train_dir, test_dir,
                    image_size=(image_size, image_size),
                )

                # Check if we loaded any data
                if len(X_train) == 0 or len(class_mapping) == 0:
                    logger.warning(f"No images found in {dataset_type} dataset directories!")
                    logger.info("The directories exist but contain no images.")
                    logger.info("Creating a demo model with default character classes...")
                    logger.info("")
                    logger.info("Please add images to the dataset directories:")
                    logger.info(f"  Train: {train_dir}")
                    logger.info(f"  Test: {test_dir}")
                    logger.info("")
                    logger.info("Expected structure for characters:")
                    logger.info("  characters_train_set/")
                    logger.info("  ├── alif/")
                    logger.info("  │   ├── img001.png")
                    logger.info("  │   └── ...")
                    logger.info("  └── baa/")
                    logger.info("      └── ...")
                    logger.info("")
                    create_demo_model(model_save_path, class_labels_path)
                    return

                # Save processed data
                save_processed_data(X_train, X_val, X_test, y_train, y_val, y_test, processed_dir)
                save_class_mapping(class_mapping, class_labels_path)
                # Also save to processed dir for consistency
                save_class_mapping(class_mapping, str(Path(processed_dir) / "class_labels.json"))
            else:
                # Fallback to checking for any subdirectory structure
                logger.warning(f"Split directories for {dataset_type} not found")
                if not Path(data_dir).exists() or not list(Path(data_dir).iterdir()):
                    logger.warning(f"No dataset found in {data_dir}")
                    logger.info("Creating a demo model with default character classes...")
                    logger.info("")
                    logger.info("To train with real data, please:")
                    logger.info("1. Download an Urdu handwritten character dataset")
                    logger.info("2. Place it in backend/data/raw/ with the following structure:")
                    logger.info("   data/raw/")
                    logger.info("   ├── characters_train_set/")
                    logger.info("   │   ├── alif/")
                    logger.info("   │   │   ├── img001.png")
                    logger.info("   │   │   └── ...")
                    logger.info("   │   └── baa/")
                    logger.info("   │       └── ...")
                    logger.info("   └── characters_test_set/")
                    logger.info("       └── ...")
                    logger.info("")
                    logger.info("Or for digits:")
                    logger.info("   data/raw/")
                    logger.info("   ├── digits_train_set/")
                    logger.info("   │   ├── 0/")
                    logger.info("   │   ├── 1/")
                    logger.info("   │   └── ...")
                    logger.info("   └── digits_test_set/")
                    logger.info("       └── ...")
                    logger.info("")

                    # Create a simple demo model without training
                    create_demo_model(model_save_path, class_labels_path)
                    return
        else:
            # Legacy single directory mode
            if not Path(data_dir).exists() or not list(Path(data_dir).iterdir()):
                logger.warning(f"No dataset found in {data_dir}")
                create_demo_model(model_save_path, class_labels_path)
                return

            # Load dataset
            images, labels, class_mapping = load_dataset(data_dir, (image_size, image_size))

            # Preprocess
            images = preprocess_images(images)

            # Split
            X_train, X_val, X_test, y_train, y_val, y_test = split_dataset(images, labels)

            # Save processed data
            save_processed_data(X_train, X_val, X_test, y_train, y_val, y_test, processed_dir)
            save_class_mapping(class_mapping, class_labels_path)

    # Get number of classes
    num_classes = len(class_mapping)
    logger.info(f"Number of classes: {num_classes}")

    # Convert labels to categorical
    y_train_cat = to_categorical(y_train, num_classes)
    y_val_cat = to_categorical(y_val, num_classes)
    y_test_cat = to_categorical(y_test, num_classes)

    logger.info(f"Training set: {X_train.shape[0]} samples")
    logger.info(f"Validation set: {X_val.shape[0]} samples")
    logger.info(f"Test set: {X_test.shape[0]} samples")

    # Create model
    logger.info("Creating CNN model...")
    model = create_cnn_model(
        input_shape=(image_size, image_size, 1),
        num_classes=num_classes,
    )

    # Compile model
    model = compile_model(model, learning_rate=learning_rate)

    # Get callbacks
    callbacks = get_callbacks(
        model_checkpoint_path=model_save_path,
        log_dir="logs/tensorboard",
    )

    # Train model
    logger.info("Starting model training...")
    logger.info("-" * 40)

    if use_augmentation:
        # Use data generator with augmentation
        train_datagen = create_data_generator()
        train_generator = train_datagen.flow(X_train, y_train_cat, batch_size=batch_size)
        steps_per_epoch = len(X_train) // batch_size

        history = model.fit(
            train_generator,
            steps_per_epoch=steps_per_epoch,
            epochs=epochs,
            validation_data=(X_val, y_val_cat),
            callbacks=callbacks,
            verbose=1,
        )
    else:
        history = model.fit(
            X_train, y_train_cat,
            batch_size=batch_size,
            epochs=epochs,
            validation_data=(X_val, y_val_cat),
            callbacks=callbacks,
            verbose=1,
        )

    logger.info("-" * 40)
    logger.info("Training completed!")

    # Evaluate on test set
    logger.info("Evaluating model on test set...")
    test_loss, test_accuracy = model.evaluate(X_test, y_test_cat, verbose=0)
    logger.info(f"Test Loss: {test_loss:.4f}")
    logger.info(f"Test Accuracy: {test_accuracy:.4f}")

    # Save training history
    history_path = Path(model_save_path).parent / "training_history.json"
    save_training_history(history, history_path)

    # Log final summary
    total_time = time.time() - start_time
    logger.info("=" * 60)
    logger.info("TRAINING SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Total training time: {total_time / 60:.2f} minutes")
    logger.info(f"Final training accuracy: {history.history['accuracy'][-1]:.4f}")
    logger.info(f"Final validation accuracy: {history.history['val_accuracy'][-1]:.4f}")
    logger.info(f"Test accuracy: {test_accuracy:.4f}")
    logger.info(f"Model saved to: {model_save_path}")
    logger.info(f"Class labels saved to: {class_labels_path}")
    logger.info("=" * 60)


def create_demo_model(model_save_path: str, class_labels_path: str) -> None:
    """
    Create a demo model for testing purposes when no dataset is available.

    Args:
        model_save_path: Path to save the model
        class_labels_path: Path to save class labels
    """
    logger.info("Creating demo model...")

    # Create model with default number of classes
    num_classes = len(URDU_CHARACTERS)
    model = create_cnn_model(input_shape=(64, 64, 1), num_classes=num_classes)
    model = compile_model(model)

    # Save model
    model.save(model_save_path)
    logger.info(f"Demo model saved to: {model_save_path}")

    # Save class labels
    save_class_mapping(URDU_CHARACTERS, class_labels_path)
    logger.info(f"Class labels saved to: {class_labels_path}")

    logger.info("Demo model created successfully!")
    logger.info("Note: This is an untrained model for demonstration purposes.")


def save_training_history(history, output_path: Path) -> None:
    """
    Save training history to JSON file.

    Args:
        history: Keras training history object
        output_path: Path to save the JSON file
    """
    logger.info(f"Saving training history to: {output_path}")

    history_dict = {k: [float(v) for v in vals] for k, vals in history.history.items()}

    with open(output_path, "w") as f:
        json.dump(history_dict, f, indent=2)

    logger.info("Training history saved")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Train Urdu character recognition model")
    parser.add_argument("--data-dir", type=str, default="data/raw", help="Path to raw dataset base directory")
    parser.add_argument("--processed-dir", type=str, default="data/processed", help="Path for processed data")
    parser.add_argument("--model-path", type=str, default="saved_models/urdu_cnn_model.h5", help="Model save path")
    parser.add_argument("--labels-path", type=str, default="saved_models/class_labels.json", help="Class labels path")
    parser.add_argument("--image-size", type=int, default=64, help="Image size")
    parser.add_argument("--batch-size", type=int, default=32, help="Batch size")
    parser.add_argument("--epochs", type=int, default=100, help="Number of epochs")
    parser.add_argument("--lr", type=float, default=0.001, help="Learning rate")
    parser.add_argument("--no-augmentation", action="store_true", help="Disable data augmentation")
    parser.add_argument("--use-processed", action="store_true", help="Use pre-processed data")
    parser.add_argument("--dataset-type", type=str, default="characters",
                       choices=["characters", "digits"], help="Dataset type to train on")
    parser.add_argument("--no-split-dirs", action="store_true",
                       help="Disable split train/test directories (use legacy single directory mode)")

    args = parser.parse_args()

    train_model(
        data_dir=args.data_dir,
        processed_dir=args.processed_dir,
        model_save_path=args.model_path,
        class_labels_path=args.labels_path,
        image_size=args.image_size,
        batch_size=args.batch_size,
        epochs=args.epochs,
        learning_rate=args.lr,
        use_augmentation=not args.no_augmentation,
        use_processed=args.use_processed,
        dataset_type=args.dataset_type,
        use_split_dirs=not args.no_split_dirs,
    )
