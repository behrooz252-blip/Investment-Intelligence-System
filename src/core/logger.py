import logging
from pathlib import Path

# ایجاد پوشه logs در صورت نبودن
Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/system.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("InvestmentIntelligence")
print("Logger module loaded")