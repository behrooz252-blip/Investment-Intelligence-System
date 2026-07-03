"""
File storage for raw market data.
"""

import json
from pathlib import Path
from datetime import datetime

from config.settings import RAW_DATA_DIR


class FileStorage:

    def __init__(self):
        RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    def save_json(self, data: dict, prefix: str):

        filename = f"{prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        filepath = RAW_DATA_DIR / filename

        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        return filepath