import coin

class Portfolio(object):

    def __init__(self, coins=None):
        self.cost = None
        self.market_val = None
        self.coins = {}
        self.pnl_unrealised_d_amt = None
        self.pnl_unrealised_pct = None
        self.pnl_realised_d_amt = None
        self.fees = None

        pass
