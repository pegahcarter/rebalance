import sys
import ccxt
import pandas as pd
import numpy as np
import exchange


class Portfolio(object):
	'''	Represents our account balance on Binance '''

	def __init__(self, coins=None, PORTFOLIO_START_VALUE=None):
		if PORTFOLIO_START_VALUE:
			pass
			# hist_prices = pd.read_csv()[['timestamp'] + coins_in_portfolio]
			# amt_each = PORTFOLIO_START_VALUE / len(coins_in_portfolio)
			# units =  np.divide(amt_each, prices)
			# prices = hist_prices[coins_in_portfolio].iloc[0]
			# date = hist_prices[0]
		else: # This is not a simulation.  Rebalance our own portfolio.
			coins = []
			units = []
			prices = []
			hist_prices = None
			date = None
			try:
				api = pd.read_csv('../../api.csv')
			except:
				api = pd.read_csv('../api.csv')
			self.binance = ccxt.binance({'options': {'adjustForTimeDifference': True},
			                        'apiKey': api['apiKey'][0],
			                        'secret': api['secret'][0]})

			all_coins_and_units = self.binance.fetchBalance()['free']
			for coin, coin_units in all_coins_and_units.items():
				# TODO: use BTC price on exchange instead of coin units
				if coin == 'USDT' and coin_units > 200 \
				or coin not in ['TFUEL', 'USDT'] and coin_units > 0.001:
					coins.append(coin)
					units.append(coin_units)
					prices.append(exchange.fetch_price(coin))

		self.coins = coins
		self.hist_prices = hist_prices
		self.units = units
		self.prices = prices
		self.date = date
		self.usd_values = np.multiply(units, prices)
