import ccxt
import pandas as pd


class Exchange:

    api = pd.read_csv('../../../api.csv')
    hist_prices = pd.read_csv('../../data/historical/prices.csv')

    def __init__(self, simulated, backtest):
        self.simulated = simulated
        self.backtest = backtest
        self.exchange = ccxt.binance({'options': {'adjustForTimeDifference': True},
                                     'apiKey': api['apiKey'][0],
                                     'secret': api['secret'][0]})
        self.balance = self.exchange.fetchBalance()['free']
        self.tickers = (set(ticker.split('/')) for ticker in self.exchange.fetchTickers())

        self.hist_prices = hist_prices



    def fetch_price(self, coin, date=None):

        if date is not None:
            pass
        else:
            pass



    def calculate_units(self):
        pass


    def execute_trade(self):
        pass
