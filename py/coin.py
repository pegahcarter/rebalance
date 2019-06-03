from py.transactions import Transaction

class Coin:

    def __init__(self, coin, trade_id, price, units, fee_rate):
        self.price = price
        self.units = units
        self.cost = price * units
        self.market_val = self.cost
        self.pnl_unrealised_d_amt = 0
        self.pnl_realised_d_amt = 0
        self.pnl_unrealsed_pct = 0
        self.fees = self.cost * fee_rate
