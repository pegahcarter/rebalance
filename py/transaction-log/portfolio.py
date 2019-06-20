import pandas as pd
import numpy as np
from transactions import Transactions
from exchange import Exchange
from datetime import  datetime

class Portfolio:
	'''	Represents our account balance on Binance '''

	hist_prices = pd.read_csv('data/historical/prices.csv')
	dates = hist_prices['timestamp'].tolist()
	exchange = Exchange()

	def __init__(self, COINS=None, PORTFOLIO_START_VALUE=None):
		self.PORTFOLIO_START_VALUE = PORTFOLIO_START_VALUE
		if PORTFOLIO_START_VALUE:
			date = self.dates[0]
			self.hist_prices = np.array(self.hist_prices[COINS])
			prices = self.hist_prices[0]
			amt_each = PORTFOLIO_START_VALUE / len(COINS)
			units =  np.divide(amt_each, self.hist_prices[0])
		else: # This is not a simulation.  Rebalance our own portfolio.
			# TODO: figure out how to include/ignore USDT
			date = datetime.now()
			balance = self.exchange.fetch_balance()
			coins = balance.keys()
			prices = np.array([self.exchange.fetch_price(coin) for coin in coins])
			units = balance.values()

		self.date = date
		self.coins = coins
		self.prices = prices
		self.units = units
		self.market_vals = prices * units
		self.transactions = Transactions(self)


	def trade(self, cost):
		''' Executes a buy and sell order '''

		sell_index = self.market_vals.argmax()
		buy_index = self.market_vals.argmin()
		data = {'sell': sell_index, 'buy': buy_index}

		for side, index in data.items():
			coin = self.coins[index]
			# TODO: make sure self.prices is current in backtest
			price = self.prices[index]
			units = cost/price
			self.units[index] = self.transactions.update(side, coin, cost, units, self.date)
			if self.PORTFOLIO_START_VALUE is None:
				exchange.create_order(coin, side, units)
