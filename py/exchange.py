import ccxt
import pandas as pd

class Exchange(object):

	def __init__(self):
		api = pd.read_csv('../api.csv')
		self.binance = ccxt.binance({'options': {'adjustForTimeDifference': True},
					                        'apiKey': api['apiKey'][0],
					                        'secret': api['secret'][0]})

		balance = self.binance.fetchBalance()['free']
		self.coins_units = {coin: units
		   for coin, units
		   in balance.items()
		   if units > 0.01
		   and coin != 'ENJ'}



    def fetch_price(self):
        pass
