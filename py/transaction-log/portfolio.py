import sys
import ccxt
import pandas as pd
import numpy as np
import exchange


class Portfolio(object):
	'''	Represents our account balance on Binance '''

	hist_prices = pd.read_csv('data/historical/prices.csv')
	dates = hist_prices['timestamp'].tolist()

	def __init__(self, coins=None, PORTFOLIO_START_VALUE=None):
		self.PORTFOLIO_START_VALUE = PORTFOLIO_START_VALUE
		if PORTFOLIO_START_VALUE:
			date = self.dates[0]
			self.hist_prices = np.array(self.hist_prices[coins])
			prices = prices[0]
			amt_each = PORTFOLIO_START_VALUE / len(coins)
			units =  np.divide(amt_each, self.hist_prices[0])
		else: # This is not a simulation.  Rebalance our own portfolio.
			date = None
			# prices = []
			coins = []
			units = []
			# TODO: add api reference
			api = pd.read_csv('...')
			self.binance = ccxt.binance({
				'options': {'adjustForTimeDifference': True},
			    'apiKey': api['apiKey'][0],
			    'secret': api['secret'][0]
			})

			all_coins_and_units = self.binance.fetchBalance()['free']
			for coin, coin_units in all_coins_and_units.items():
				# TODO: use BTC price on exchange instead of coin units
				# TODO: include/ignore USDT
					coins.append(coin)
					units.append(coin_units)
					prices.append(exchange.fetch_price(coin))

		self.date = date
		self.coins = coins
		self.units = units
		# self.prices = prices
		self.market_vals = np.multiply(units, prices)
