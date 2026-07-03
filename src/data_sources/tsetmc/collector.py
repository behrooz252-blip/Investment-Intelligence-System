from datetime import datetime

from data_sources.base import BaseDataSource
from models.market_snapshot import MarketSnapshot


class TSETMCCollector(BaseDataSource):

    def connect(self):
        print("Connecting to TSETMC...")

    def fetch(self):

        print("Fetching market data...")

        snapshot = MarketSnapshot(
            timestamp=datetime.now(),
            index_value=0,
            equal_weight_index=0,
            total_value=0,
            total_volume=0,
            real_money_flow=0
        )

        return snapshot

    def validate(self, data):
        print("Validating data...")

    def save(self, data):
        print("Saving data...")