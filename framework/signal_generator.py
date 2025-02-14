import pandas as pd

class SignalGenerator:
    def __init__(self, strategy="mean_reversion"):
        self.strategy = strategy

    def generate_signals(self, data):
        """Generate signals based on the strategy."""
        if self.strategy == "mean_reversion":
            data["signal"] = (data["Close"] < data["Close"].rolling(20).mean()).astype(int)
        elif self.strategy == "momentum":
            data["signal"] = (data["Close"].diff() > 0).astype(int)
        return data
