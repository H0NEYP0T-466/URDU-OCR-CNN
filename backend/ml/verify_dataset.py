"""
Dataset Verification Script

Script to verify the dataset structure and test data loading.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.config import FOLDER_TO_CHARACTER, FOLDER_TO_DIGIT, get_urdu_character_from_folder
from app.logger import setup_logger
from ml.preprocess import check_dataset_structure, get_dataset_paths, get_image_files, load_dataset

logger = setup_logger(name="verify_dataset", log_level="INFO", log_file="logs/verify.log")


def verify_dataset(base_dir: str = "data/raw") -> None:
    """
    Verify the dataset structure and report findings.

    Args:
        base_dir: Base directory containing the raw data
    """
    logger.info("=" * 60)
    logger.info("DATASET VERIFICATION")
    logger.info("=" * 60)
    logger.info(f"Base directory: {base_dir}")
    logger.info("")

    # Check overall structure
    logger.info("Checking dataset structure...")
    datasets = check_dataset_structure(base_dir)
    logger.info("")

    # Verify each available dataset
    base_path = Path(base_dir)

    if datasets.get("characters_train"):
        verify_character_dataset(base_path / "characters_train_set", "Characters Train")

    if datasets.get("characters_test"):
        verify_character_dataset(base_path / "characters_test_set", "Characters Test")

    if datasets.get("digits_train"):
        verify_digit_dataset(base_path / "digits_train_set", "Digits Train")

    if datasets.get("digits_test"):
        verify_digit_dataset(base_path / "digits_test_set", "Digits Test")

    logger.info("=" * 60)
    logger.info("VERIFICATION COMPLETE")
    logger.info("=" * 60)


def verify_character_dataset(data_path: Path, name: str) -> None:
    """
    Verify a character dataset directory.

    Args:
        data_path: Path to the dataset directory
        name: Name of the dataset for logging
    """
    logger.info("-" * 40)
    logger.info(f"Verifying {name}: {data_path}")
    logger.info("-" * 40)

    if not data_path.exists():
        logger.error(f"Directory not found: {data_path}")
        return

    # Get all subdirectories
    class_dirs = sorted([d for d in data_path.iterdir() if d.is_dir()])
    logger.info(f"Found {len(class_dirs)} class folders")

    # Check each class
    total_images = 0
    unknown_folders = []

    for class_dir in class_dirs:
        folder_name = class_dir.name
        urdu_char = get_urdu_character_from_folder(folder_name)

        # Count images
        image_files = get_image_files(class_dir)
        num_images = len(image_files)
        total_images += num_images

        if folder_name not in FOLDER_TO_CHARACTER:
            unknown_folders.append(folder_name)
            logger.warning(f"  Unknown folder: {folder_name} ({num_images} images) -> '{urdu_char}'")
        else:
            logger.info(f"  {folder_name}: {num_images} images -> '{urdu_char}'")

    logger.info(f"Total images: {total_images}")
    if unknown_folders:
        logger.warning(f"Unknown folders (not in mapping): {unknown_folders}")
    logger.info("")


def verify_digit_dataset(data_path: Path, name: str) -> None:
    """
    Verify a digit dataset directory.

    Args:
        data_path: Path to the dataset directory
        name: Name of the dataset for logging
    """
    logger.info("-" * 40)
    logger.info(f"Verifying {name}: {data_path}")
    logger.info("-" * 40)

    if not data_path.exists():
        logger.error(f"Directory not found: {data_path}")
        return

    # Get all subdirectories
    class_dirs = sorted([d for d in data_path.iterdir() if d.is_dir()])
    logger.info(f"Found {len(class_dirs)} class folders")

    # Check each class
    total_images = 0
    unknown_folders = []

    for class_dir in class_dirs:
        folder_name = class_dir.name
        urdu_digit = get_urdu_character_from_folder(folder_name)

        # Count images
        image_files = get_image_files(class_dir)
        num_images = len(image_files)
        total_images += num_images

        if folder_name not in FOLDER_TO_DIGIT:
            unknown_folders.append(folder_name)
            logger.warning(f"  Unknown folder: {folder_name} ({num_images} images) -> '{urdu_digit}'")
        else:
            logger.info(f"  {folder_name}: {num_images} images -> '{urdu_digit}'")

    logger.info(f"Total images: {total_images}")
    if unknown_folders:
        logger.warning(f"Unknown folders (not in mapping): {unknown_folders}")
    logger.info("")


def test_data_loading(base_dir: str = "data/raw", dataset_type: str = "characters") -> None:
    """
    Test loading a small sample of the dataset.

    Args:
        base_dir: Base directory containing the raw data
        dataset_type: Type of dataset ('characters' or 'digits')
    """
    logger.info("=" * 60)
    logger.info(f"TESTING DATA LOADING: {dataset_type}")
    logger.info("=" * 60)

    try:
        train_dir, test_dir = get_dataset_paths(base_dir, dataset_type)
        logger.info(f"Train directory: {train_dir}")
        logger.info(f"Test directory: {test_dir}")

        # Try loading training data
        logger.info("Loading training data...")
        train_images, train_labels, class_mapping = load_dataset(train_dir)
        logger.info(f"Training data loaded successfully!")
        logger.info(f"  Images shape: {train_images.shape}")
        logger.info(f"  Labels shape: {train_labels.shape}")
        logger.info(f"  Number of classes: {len(class_mapping)}")

        # Show class mapping
        logger.info("Class mapping:")
        for idx, name in sorted(class_mapping.items()):
            urdu_char = get_urdu_character_from_folder(name)
            logger.info(f"  {idx}: {name} -> '{urdu_char}'")

    except Exception as e:
        logger.error(f"Error loading data: {str(e)}")
        raise


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Verify dataset structure")
    parser.add_argument("--data-dir", type=str, default="data/raw", help="Path to raw dataset base directory")
    parser.add_argument("--test-load", action="store_true", help="Test loading the dataset")
    parser.add_argument("--dataset-type", type=str, default="characters",
                       choices=["characters", "digits"], help="Dataset type to verify/load")

    args = parser.parse_args()

    # Verify structure
    verify_dataset(args.data_dir)

    # Test loading if requested
    if args.test_load:
        test_data_loading(args.data_dir, args.dataset_type)
