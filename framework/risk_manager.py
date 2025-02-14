class RiskManager:
    def __init__(self, max_drawdown=0.1):
        self.max_drawdown = max_drawdown

    def evaluate_risk(self, portfolio_value, peak_value):
        """Check if max drawdown is exceeded."""
        drawdown = (peak_value - portfolio_value) / peak_value
        return drawdown < self.max_drawdown
