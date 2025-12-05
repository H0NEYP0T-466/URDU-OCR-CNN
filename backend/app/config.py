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
    
    # Digit model settings
    DIGIT_MODEL_PATH: str = "saved_models/urdu_digit_cnn_model.h5"
    DIGIT_CLASS_LABELS_PATH: str = "saved_models/digit_class_labels.json"

    # File upload settings
    MAX_FILE_SIZE: int = 5 * 1024 * 1024  # 5MB
    ALLOWED_EXTENSIONS: List[str] = [".png", ".jpg", ".jpeg", ".bmp"]

    # Image processing settings
    IMAGE_SIZE: Tuple[int, int] = (64, 64)

    # Logging settings
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/app.log"

    # CORS settings
    CORS_ORIGINS: List[str] = ["*"]

    # Server settings
    HOST: str = "0.0.0.0"
    PORT: int = 3000

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
    def digit_model_path_resolved(self) -> Path:
        """Get the resolved digit model path."""
        return Path(__file__).parent.parent / self.DIGIT_MODEL_PATH

    @property
    def digit_class_labels_path_resolved(self) -> Path:
        """Get the resolved digit class labels path."""
        return Path(__file__).parent.parent / self.DIGIT_CLASS_LABELS_PATH

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

# Mapping from folder names to Urdu characters
# Based on the dataset structure: characters_train_set/{folder_name}/
FOLDER_TO_CHARACTER = {
    "alif": "ا",
    "alif mad aa": "آ",  # Alif with madda
    "ayn": "ع",
    "baa": "ب",
    "bari yaa": "ے",
    "cheey": "چ",
    "choti yaa": "ی",
    "daal": "د",
    "dhaal": "ڈ",
    "faa": "ف",
    "gaaf": "گ",
    "ghain": "غ",
    "haa1": "ح",  # Hay (gol)
    "haa2": "ہ",  # Hay (choti)
    "haa3": "ھ",  # Do chashmi hay
    "hamza": "ء",
    "jeem": "ج",
    "kaaf": "ک",
    "khaa": "خ",
    "laam": "ل",
    "meem": "م",
    "noon": "ن",
    "noonghunna": "ں",  # Noon ghunna
    "paa": "پ",
    "qaaf": "ق",
    "raa": "ر",
    "rhraa": "ڑ",  # Rray
    "seen": "س",
    "seey": "ث",  # Say/Seey
    "sheen": "ش",
    "swaad": "ص",
    "taa": "ت",
    "ttaa": "ٹ",
    "twa": "ط",  # Toay
    "waw": "و",
    "zaaa": "ز",  # Zay
    "zaal": "ذ",
    "zhaa": "ژ",
    "zwaa": "ظ",  # Zoay
    "zwaad": "ض",  # Dwad/Zwad
}

# Mapping from folder names to Urdu digit characters
# Based on the dataset structure: digits_train_set/{folder_name}/
FOLDER_TO_DIGIT = {
    "0": "۰",
    "1": "۱",
    "2": "۲",
    "3": "۳",
    "4": "۴",
    "5": "۵",
    "6": "۶",
    "7": "۷",
    "8": "۸",
    "9": "۹",
}


def get_urdu_character_from_folder(folder_name: str) -> str:
    """
    Get the Urdu character corresponding to a folder name.

    Args:
        folder_name: Name of the folder (e.g., 'alif', 'baa', '0', '1')

    Returns:
        The corresponding Urdu character, or the folder name if not found
    """
    # Check characters first
    if folder_name in FOLDER_TO_CHARACTER:
        return FOLDER_TO_CHARACTER[folder_name]
    # Then check digits
    if folder_name in FOLDER_TO_DIGIT:
        return FOLDER_TO_DIGIT[folder_name]
    # Return the folder name as-is if no mapping found
    return folder_name
