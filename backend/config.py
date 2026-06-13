from __future__ import annotations

import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
GENERATED_DIR = Path(os.getenv("GENERATED_DIR", BASE_DIR / "generated"))
DATA_DIR = Path(os.getenv("DATA_DIR", BASE_DIR / "data"))
HISTORY_FILE = Path(os.getenv("HISTORY_FILE", DATA_DIR / "history.json"))
MAX_CONTENT_LENGTH = 8 * 1024


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret-in-production")
    JSON_SORT_KEYS = False
    MAX_CONTENT_LENGTH = MAX_CONTENT_LENGTH
