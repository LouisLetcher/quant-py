import pytest
from algorithms.stocks.mean_reversion import MeanReversionStrategy

def test_mean_reversion():
    strategy = MeanReversionStrategy(symbol="AAPL")
    assert strategy.capital > 0, "Initial capital should be greater than 0"
