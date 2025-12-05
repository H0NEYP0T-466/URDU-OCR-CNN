"""
Model Evaluation Script

Script to evaluate the trained CNN model and generate reports.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
from tensorflow import keras
from tensorflow.keras.utils import to_categorical

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.logger import setup_logger
from ml.preprocess import load_processed_data

logger = setup_logger(name="ml_evaluate", log_level="INFO", log_file="logs/training.log")


def load_model_and_labels(
    model_path: str = "saved_models/urdu_cnn_model.h5",
    labels_path: str = "saved_models/class_labels.json",
) -> Tuple[keras.Model, Dict[int, str]]:
    """
    Load trained model and class labels.

    Args:
        model_path: Path to the saved model
        labels_path: Path to class labels JSON

    Returns:
        Tuple of (model, class_labels)
    """
    logger.info(f"Loading model from: {model_path}")
    model = keras.models.load_model(model_path)
    logger.info("Model loaded successfully")

    logger.info(f"Loading class labels from: {labels_path}")
    with open(labels_path, "r", encoding="utf-8") as f:
        class_labels = {int(k): v for k, v in json.load(f).items()}
    logger.info(f"Loaded {len(class_labels)} class labels")

    return model, class_labels


def evaluate_model(
    model: keras.Model,
    X_test: np.ndarray,
    y_test: np.ndarray,
    class_labels: Dict[int, str],
) -> Dict:
    """
    Evaluate model on test data.

    Args:
        model: Trained Keras model
        X_test: Test images
        y_test: Test labels
        class_labels: Class label mapping

    Returns:
        Dictionary with evaluation metrics
    """
    logger.info("Evaluating model on test set...")
    logger.info(f"Test set size: {len(X_test)}")

    num_classes = len(class_labels)
    y_test_cat = to_categorical(y_test, num_classes)

    # Get test loss and accuracy
    test_loss, test_accuracy = model.evaluate(X_test, y_test_cat, verbose=0)
    logger.info(f"Test Loss: {test_loss:.4f}")
    logger.info(f"Test Accuracy: {test_accuracy:.4f}")

    # Get predictions
    logger.info("Making predictions...")
    y_pred_probs = model.predict(X_test, verbose=0)
    y_pred = np.argmax(y_pred_probs, axis=1)

    # Generate classification report
    logger.info("Generating classification report...")
    target_names = [class_labels[i] for i in range(num_classes)]
    report = classification_report(y_test, y_pred, target_names=target_names, output_dict=True)

    # Log per-class metrics
    logger.info("\nPer-class Performance:")
    for i, name in enumerate(target_names[:10]):  # Show first 10 classes
        precision = report[name]["precision"]
        recall = report[name]["recall"]
        f1 = report[name]["f1-score"]
        logger.info(f"  {name}: Precision={precision:.3f}, Recall={recall:.3f}, F1={f1:.3f}")

    # Generate confusion matrix
    logger.info("Generating confusion matrix...")
    cm = confusion_matrix(y_test, y_pred)

    return {
        "test_loss": test_loss,
        "test_accuracy": test_accuracy,
        "classification_report": report,
        "confusion_matrix": cm,
        "y_true": y_test,
        "y_pred": y_pred,
        "class_labels": class_labels,
    }


def plot_confusion_matrix(
    cm: np.ndarray,
    class_labels: Dict[int, str],
    output_path: str = "logs/confusion_matrix.png",
    figsize: Tuple[int, int] = (20, 20),
) -> None:
    """
    Plot and save confusion matrix.

    Args:
        cm: Confusion matrix
        class_labels: Class label mapping
        output_path: Path to save the plot
        figsize: Figure size
    """
    logger.info(f"Plotting confusion matrix to: {output_path}")

    plt.figure(figsize=figsize)

    # Get labels
    labels = [class_labels[i] for i in range(len(class_labels))]

    # Create heatmap
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=labels,
        yticklabels=labels,
    )

    plt.title("Confusion Matrix - Urdu Character Recognition", fontsize=16)
    plt.xlabel("Predicted", fontsize=12)
    plt.ylabel("True", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0)
    plt.tight_layout()

    # Save plot
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=150)
    plt.close()

    logger.info("Confusion matrix saved")


def plot_training_history(
    history_path: str = "saved_models/training_history.json",
    output_dir: str = "logs",
) -> None:
    """
    Plot training history.

    Args:
        history_path: Path to training history JSON
        output_dir: Directory to save plots
    """
    logger.info(f"Loading training history from: {history_path}")

    with open(history_path, "r") as f:
        history = json.load(f)

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Plot accuracy
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    plt.plot(history["accuracy"], label="Training")
    plt.plot(history["val_accuracy"], label="Validation")
    plt.title("Model Accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.grid(True)

    # Plot loss
    plt.subplot(1, 2, 2)
    plt.plot(history["loss"], label="Training")
    plt.plot(history["val_loss"], label="Validation")
    plt.title("Model Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    output_path = Path(output_dir) / "training_history.png"
    plt.savefig(output_path, dpi=150)
    plt.close()

    logger.info(f"Training history plot saved to: {output_path}")


def save_evaluation_report(
    results: Dict,
    output_path: str = "logs/evaluation_report.json",
) -> None:
    """
    Save evaluation results to JSON.

    Args:
        results: Evaluation results dictionary
        output_path: Path to save the report
    """
    logger.info(f"Saving evaluation report to: {output_path}")

    # Prepare serializable data
    report = {
        "test_loss": float(results["test_loss"]),
        "test_accuracy": float(results["test_accuracy"]),
        "classification_report": results["classification_report"],
        "confusion_matrix": results["confusion_matrix"].tolist(),
    }

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    logger.info("Evaluation report saved")


def evaluate(
    model_path: str = "saved_models/urdu_cnn_model.h5",
    labels_path: str = "saved_models/class_labels.json",
    data_dir: str = "data/processed",
) -> None:
    """
    Run full model evaluation.

    Args:
        model_path: Path to the saved model
        labels_path: Path to class labels JSON
        data_dir: Directory containing processed data
    """
    logger.info("=" * 60)
    logger.info("URDU CHARACTER RECOGNITION MODEL EVALUATION")
    logger.info("=" * 60)

    # Load model and labels
    model, class_labels = load_model_and_labels(model_path, labels_path)

    # Load test data
    logger.info(f"Loading test data from: {data_dir}")
    _, _, X_test, _, _, y_test = load_processed_data(data_dir)

    # Evaluate
    results = evaluate_model(model, X_test, y_test, class_labels)

    # Generate visualizations
    plot_confusion_matrix(results["confusion_matrix"], class_labels)

    # Try to plot training history if available
    history_path = Path(model_path).parent / "training_history.json"
    if history_path.exists():
        plot_training_history(str(history_path))

    # Save report
    save_evaluation_report(results)

    logger.info("=" * 60)
    logger.info("EVALUATION SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Test Accuracy: {results['test_accuracy']:.4f}")
    logger.info(f"Test Loss: {results['test_loss']:.4f}")
    logger.info("=" * 60)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Evaluate Urdu character recognition model")
    parser.add_argument("--model-path", type=str, default="saved_models/urdu_cnn_model.h5", help="Model path")
    parser.add_argument("--labels-path", type=str, default="saved_models/class_labels.json", help="Labels path")
    parser.add_argument("--data-dir", type=str, default="data/processed", help="Processed data directory")

    args = parser.parse_args()

    evaluate(
        model_path=args.model_path,
        labels_path=args.labels_path,
        data_dir=args.data_dir,
    )
