from transactions import Transactions
import pandas as pd
import ccxt
import json

class Portfolio:

    fee_rate = fee_rate
    slippage_rate = slippage_rate
    api = ccxt.binance()
    prices = pd.read_csv('data/historical/prices.csv')

    def __init__(self, simulated=False, coins=None):
        self.simulated = simulated
        self.prices = self.prices[['timestamp'] + coins]
        try:
            with open('transactions.json', 'r') as f:
                self.transactions = json.load(f)
        except:
            self.transactions = []

        for coin in coins:
            if coin not in map(lambda tx: tx['coin'], transactions):
                self._add_coin(coin=coin)

    def _add_coin(self, coin):
        price = self.get_price(coin)
        units = 1000/price
        date = self.prices['timestamp'][0]
        self.transactions.append({
            'date': date,
            'coin': coin,
            'side': 'BUY',
            'units': units,
            'prev_units': 0,
            'cum_units': units
        })

    def get_price(self, coin, i=0):
        if self.simulated:
            return self.prices[coin][i]
        else:
            return query_price(coin)

    def query_price(self, coin):
        btc_price = self.api.fetch_ticker('BTC/USDT')['info']['lastPrice']
        if coin == 'BTC':
            return btc_price
        else:
            return btc_price * self.api.fetch_ticker(coin + '/BTC')['info']['lastPrice']

    def summarize(self):
        # Add summary
        self.summary = {}
