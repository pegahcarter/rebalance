

class Coin:

    def __init__(self, coin, price, units, fee_rate):
        self.price = price
        self.units = units
        self.cost = price * units
        self.market_val = self.cost
