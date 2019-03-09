import ccxt
import pandas as pd

class Exchange(object):

	def __init__(self):
		api = pd.read_csv('../api.csv')
		self.binance = ccxt.binance({'options': {'adjustForTimeDifference': True},
					                        'apiKey': api['apiKey'][0],
					                        'secret': api['secret'][0]})

    def fetch_price(self):
        pass
