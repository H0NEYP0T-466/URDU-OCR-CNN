"""
Custom Logger Setup

Comprehensive logging system for the Urdu Character Recognition API.
Uses Python's logging module with custom formatters and handlers.
"""

import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path


class CustomFormatter(logging.Formatter):
    """Custom formatter with color support for console output."""

    grey = "\x1b[38;21m"
    blue = "\x1b[38;5;39m"
    yellow = "\x1b[38;5;226m"
    red = "\x1b[38;5;196m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    format_str = "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format_str + reset,
        logging.INFO: blue + format_str + reset,
        logging.WARNING: yellow + format_str + reset,
        logging.ERROR: red + format_str + reset,
        logging.CRITICAL: bold_red + format_str + reset,
    }

    def format(self, record: logging.LogRecord) -> str:
        """Format log record with color based on log level."""
        log_fmt = self.FORMATS.get(record.levelno, self.format_str)
        formatter = logging.Formatter(log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)


class FileFormatter(logging.Formatter):
    """Formatter for file output without color codes."""

    def __init__(self) -> None:
        super().__init__(
            fmt="[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )


def setup_logger(
    name: str = "urdu_ocr",
    log_level: str = "INFO",
    log_file: str = "logs/app.log",
) -> logging.Logger:
    """
    Set up and configure a logger with console and file handlers.

    Args:
        name: Logger name
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Path to the log file

    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)

    # Avoid adding handlers multiple times
    if logger.handlers:
        return logger

    # Set log level
    level = getattr(logging, log_level.upper(), logging.INFO)
    logger.setLevel(level)

    # Console handler with custom formatter
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(CustomFormatter())
    logger.addHandler(console_handler)

    # File handler with rotating logs
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    file_handler = RotatingFileHandler(
        log_path,
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(FileFormatter())
    logger.addHandler(file_handler)

    return logger


# Create default logger instance
logger = setup_logger()


def get_logger(name: str | None = None) -> logging.Logger:
    """
    Get a logger instance.

    Args:
        name: Optional logger name. If None, returns the default logger.

    Returns:
        Logger instance
    """
    if name:
        return logging.getLogger(f"urdu_ocr.{name}")
    return logger
