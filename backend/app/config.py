"""
Configuration Settings

Application configuration using Pydantic Settings.
Supports environment variables and .env files.
"""

import os
from functools import lru_cache
from pathlib import Path
from typing import List, Tuple

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings with environment variable support."""

    # Application settings
    APP_NAME: str = "Urdu Character Recognition API"
    VERSION: str = "1.0.0"
    DEBUG: bool = False
    ENVIRONMENT: str = "development"

    # Model settings
    MODEL_PATH: str = "saved_models/urdu_cnn_model.h5"
    CLASS_LABELS_PATH: str = "saved_models/class_labels.json"

    # File upload settings
    MAX_FILE_SIZE: int = 5 * 1024 * 1024  # 5MB
    ALLOWED_EXTENSIONS: List[str] = [".png", ".jpg", ".jpeg", ".bmp"]

    # Image processing settings
    IMAGE_SIZE: Tuple[int, int] = (64, 64)

    # Logging settings
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/app.log"

    # CORS settings
    CORS_ORIGINS: List[str] = ["http://localhost:5173", "http://localhost:3000"]

    # Server settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Model configuration
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    @property
    def model_path_resolved(self) -> Path:
        """Get the resolved model path."""
        return Path(__file__).parent.parent / self.MODEL_PATH

    @property
    def class_labels_path_resolved(self) -> Path:
        """Get the resolved class labels path."""
        return Path(__file__).parent.parent / self.CLASS_LABELS_PATH

    @property
    def log_file_resolved(self) -> Path:
        """Get the resolved log file path."""
        return Path(__file__).parent.parent / self.LOG_FILE


@lru_cache
def get_settings() -> Settings:
    """
    Get cached settings instance.

    Returns:
        Settings instance
    """
    return Settings()


# Urdu character class mappings
URDU_CHARACTERS = {
    0: "ا",  # Alif
    1: "ب",  # Bay
    2: "پ",  # Pay
    3: "ت",  # Tay
    4: "ٹ",  # Ttay
    5: "ث",  # Say
    6: "ج",  # Jeem
    7: "چ",  # Chay
    8: "ح",  # Hay
    9: "خ",  # Khay
    10: "د",  # Daal
    11: "ڈ",  # Ddaal
    12: "ذ",  # Zaal
    13: "ر",  # Ray
    14: "ڑ",  # Rray
    15: "ز",  # Zay
    16: "ژ",  # Zhay
    17: "س",  # Seen
    18: "ش",  # Sheen
    19: "ص",  # Swad
    20: "ض",  # Dwad
    21: "ط",  # Tway
    22: "ظ",  # Zway
    23: "ع",  # Ain
    24: "غ",  # Ghain
    25: "ف",  # Fay
    26: "ق",  # Qaaf
    27: "ک",  # Kaaf
    28: "گ",  # Gaaf
    29: "ل",  # Laam
    30: "م",  # Meem
    31: "ن",  # Noon
    32: "و",  # Wao
    33: "ہ",  # Hay Gol
    34: "ی",  # Choti Yay
    35: "ے",  # Bari Yay
    36: "۰",  # Zero
    37: "۱",  # One
    38: "۲",  # Two
    39: "۳",  # Three
    40: "۴",  # Four
    41: "۵",  # Five
    42: "۶",  # Six
    43: "۷",  # Seven
    44: "۸",  # Eight
    45: "۹",  # Nine
}

URDU_CHARACTER_NAMES = {
    "ا": "Alif",
    "ب": "Bay",
    "پ": "Pay",
    "ت": "Tay",
    "ٹ": "Ttay",
    "ث": "Say",
    "ج": "Jeem",
    "چ": "Chay",
    "ح": "Hay",
    "خ": "Khay",
    "د": "Daal",
    "ڈ": "Ddaal",
    "ذ": "Zaal",
    "ر": "Ray",
    "ڑ": "Rray",
    "ز": "Zay",
    "ژ": "Zhay",
    "س": "Seen",
    "ش": "Sheen",
    "ص": "Swad",
    "ض": "Dwad",
    "ط": "Tway",
    "ظ": "Zway",
    "ع": "Ain",
    "غ": "Ghain",
    "ف": "Fay",
    "ق": "Qaaf",
    "ک": "Kaaf",
    "گ": "Gaaf",
    "ل": "Laam",
    "م": "Meem",
    "ن": "Noon",
    "و": "Wao",
    "ہ": "Hay Gol",
    "ی": "Choti Yay",
    "ے": "Bari Yay",
    "۰": "Zero",
    "۱": "One",
    "۲": "Two",
    "۳": "Three",
    "۴": "Four",
    "۵": "Five",
    "۶": "Six",
    "۷": "Seven",
    "۸": "Eight",
    "۹": "Nine",
}
