import ccxt
import pandas as pd
from coin import Coin

class Portfolio:

    def __init__(self, **kwargs):
        self.transactions = []
        coins = kwargs.pop('coins')
        for key, val in kwargs.items():
            setattr(self, key, val)

        self.coins = {}
        for coin in coins:
            self._add_coin(coin)
            self.transactions.append({
                'id': len(self.transactions) + 1,
                'date': self.prices['timestamp'].at[0],
                'buy_or_sell': 'buy',
                'price': self.coins[coin]['price'],
                'units': self.coins[coin]['units']
            })

    # This adds the initial purchase of coin
    def _add_coin(self, coin):
        price = self.prices[coin].at[0]
        units = self.start_amt/price
        self.coins[coin] = {
            'price': price,
            'units': units,
            'market_val': price * units
        }
