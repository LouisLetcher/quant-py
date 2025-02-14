import pandas as pd

class DataLoader:
    def __init__(self, source):
        self.source = source
    
    def get_data(self, symbol, start, end):
        """Load market data for a given symbol."""
        df = pd.read_csv(f"data/{symbol}.csv", parse_dates=["Date"])
        df = df[(df["Date"] >= start) & (df["Date"] <= end)]
        return df.set_index("Date")
