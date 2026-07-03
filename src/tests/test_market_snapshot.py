from datetime import datetime

from models.market_snapshot import MarketSnapshot


def test_market_snapshot():

    snapshot = MarketSnapshot(
        timestamp=datetime.now(),
        index_value=100,
        equal_weight_index=50,
        total_value=10,
        total_volume=20,
        real_money_flow=30
    )

    assert snapshot.index_value == 100