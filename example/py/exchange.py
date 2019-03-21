import ccxt
import pandas as pd
import random

exchange = ccxt.binance({'options': {'adjustForTimeDifference': True},
                             'apiKey': api['apiKey'][0],
                             'secret': api['secret'][0]})

balance = exchange.fetchBalance()['free']
balance.keys()

random.sample(list(balance),3)


class Exchange:

    api = pd.read_csv('../../../api.csv')

    def __init__(self):

        self.exchange = ccxt.binance({'options': {'adjustForTimeDifference': True},
                                     'apiKey': api['apiKey'][0],
                                     'secret': api['secret'][0]})
        self.balance = self.exchange.fetchBalance()['free']
        self.tickers = (set(ticker.split('/')) for ticker in self.exchange.fetchTickers())




    def fetch_price(self, coin, date=None):

        if date is not None:
            pass
        else:
            pass



    def calculate_units(self):
        pass


    def execute_trade(self):
        pass
