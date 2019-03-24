import ccxt
import pandas as pd
import random

api = pd.read_csv('../../../api.csv')


class Exchange:


    def __init__(self, simulated, coins=None):

        self.exchange = ccxt.binance({'options': {'adjustForTimeDifference': True},
                                      'apiKey': api['apiKey'][0],
                                      'secret': api['secret'][0]})
        self.tickers = (set(ticker.split('/')) for ticker in self.exchange.fetchTickers())
        self.all_balances = exchange.fetchBalance()['free']


        if coins is None:
            if simulated:
                coins = random.sample(list(balance), 5) # TODO: need @param for num of coins
            else: # not simulated
                coins = [coin for coin, units in balance.items() if units > 0]

        self.coins = {}
        [self.coins[coin] = {'hist_prices': hist_prices[coin].tolist()
                             'price': self.fetch_price(coin, simulated)} for coin in coins]


    def execute_trade(self):
        pass
