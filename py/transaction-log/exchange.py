import ccxt
import pandas as pd
import transactions
from variables import token

class Exchange:

	def __init__(self, coins=None):
		# TODO: add correct api reference
		api = pd.read_csv('...')
		self.binance = ccxt.binance({'options': {'adjustForTimeDifference': True}, token})


	def fetch_balance(self):
		''' Return the coins and units we have on the exchange '''

		balance = self.binance.fetchBalance()['free']
		return {coin:units for coin, units in balance.items() if units > 0}


	def fetch_price(self, coin, i=None):
		''' Return the current dollar price of the coin in question '''

		if i is not None:
			return self.hist_prices[i, self.coins.index(coin)]
		if coin == 'USDT':
			return 1.0
		else:
			return float(self.binance.fetch_ticker(coin + '/USDT')['info']['lastPrice'])

	def create_order(coin, side, units):
		return self.binance.create_order(coin + '/USDT', 'market', side, units)
