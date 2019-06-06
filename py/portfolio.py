from transactions import Transactions


class Portfolio:

    fee_rate = fee_rate
    slippage_rate = slippage_rate
    
    def __init__(self, simulated=False, coins=None):
        self.simulated = simulated
        self.transactions = Transactions(simulated, coins)

    def summarize(self):
        # Add summary
        self.summary = {}
