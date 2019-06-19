import sys
import pandas as pd
import numpy as np
from exchange import Exchange

class Portfolio(object):
	'''	Represents our account balance on Binance '''

	hist_prices = pd.read_csv('data/historical/prices.csv')
	dates = hist_prices['timestamp'].tolist()
	exchange = Exchange()

	def __init__(self, coins=None, PORTFOLIO_START_VALUE=None):
		self.PORTFOLIO_START_VALUE = PORTFOLIO_START_VALUE
		if PORTFOLIO_START_VALUE:
			date = self.dates[0]
			self.hist_prices = np.array(self.hist_prices[coins])
			prices = self.hist_prices[0]
			amt_each = PORTFOLIO_START_VALUE / len(coins)
			units =  np.divide(amt_each, self.hist_prices[0])
		else: # This is not a simulation.  Rebalance our own portfolio.
			# TODO: figure out how to include/ignore USDT
			date = None
			balance = self.exchange.fetch_balance()
			coins = balance.keys()
			prices = np.array([self.exchange.fetch_price(coin) for coin in coins])
			units = balance.values()

		self.date = date
		self.coins = coins
		self.prices = prices
		self.units = units
		self.market_vals = prices * units


	def trade(self, cost):
		''' Executes a buy and sell '''

		sell_index = self.market_vals.argmax()
		buy_index = self.market_vals.argmin()
