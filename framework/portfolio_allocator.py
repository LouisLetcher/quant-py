class PortfolioAllocator:
    def __init__(self, risk=0.02):
        self.risk = risk

    def allocate(self, capital, signal):
        """Determine position size based on risk."""
        if signal == 1:
            return capital * self.risk  # Buy
        elif signal == -1:
            return -capital * self.risk  # Sell
        return 0  # Hold
