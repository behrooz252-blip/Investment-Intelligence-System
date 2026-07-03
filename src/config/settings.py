"""
Global configuration for Investment Intelligence System.
"""

from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
CACHE_DIR = DATA_DIR / "cache"

LOG_DIR = PROJECT_ROOT / "logs"

# Application
APP_NAME = "Investment Intelligence System"
VERSION = "1.0.0"

DEBUG = True