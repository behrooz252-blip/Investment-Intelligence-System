"""
Market Snapshot Data Model.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class MarketSnapshot:

    timestamp: datetime

    index_value: float

    equal_weight_index: float

    total_value: float

    total_volume: float

    real_money_flow: float