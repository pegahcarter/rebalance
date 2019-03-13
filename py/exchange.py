import random
import pandas as pd
import ccxt

# TODO: generic way to use multiple exchanges?
# TODO: decide which  properties to inherit from portfolio


class Exchange(object):

	hist_prices = pd.read_csv('../data/historical/prices.csv')

	def __init__(self, simulation=False, coins=None):

		self.tickers = list(ccxt.binance().fetch_tickers())
		self.simulation = simulation

		if simulation:
			if coins is None:
				# Pick random coins to backtest portfolio
				coins = random.sample(coins, 5) # TODO: should I add dynamic # of coins simulated?

			# TODO: Calculate units on day 0- where should this function be? When should it update?


		else:
			api = pd.read_csv('../api.csv')
			self.binance = ccxt.binance({'options': {'adjustForTimeDifference': True},
										 'apiKey': api['apiKey'][0],
										 'secret': api['secret'][0]})
			balance = self.binance.fetchBalance()['free']
			if coins is None:
				coins = [coin for coin, units in balance.items() if units > 0.01] # TODO: standardize units

			# NOTE: Where should coin units be stored?


		self.balance = {coin: fetch_units(coin) for coin in coins}


	def fetch_units(self, coin, date=None):
		# Do something



   def fetch_ticker(self, coin1, coin2):
	   if coin1 + '/' + coin2 in self.tickers:
		   return coin1 + '/' + coin2
	   elif coin2 + '/' + coin1 in self.tickers:
		   return coin2 + '/' + coin1


    def fetch_price(self, coin, date=None):
		if 'USD' or 'DAI' in coin:
			return 1.0

		if not self.simulated:
			btc_price = float(self.binance.fetch_ticker('BTC/USDT')['info']['lastPrice'])
			if coin == 'BTC':
				return btc_price
			else:
				btc_ratio = float(self.binance.fetch_ticker(coin + '/BTC')['info']['lastPrice'])
				return btc_ratio * btc_price
		else:
			pass # TODO


	def fetch_trade_units(self, ticker, d_amt):
		numerator, denominator = ticker.split('/')
		coin_ratio = fetch_price(numerator, date)/fetch_price(denominator)
		return d_amt * coin_ratio



	def ticker_exists(self, coin1, coin2):
		if coin1 + '/' + coin2 in self.tickers:
			return True
		elif coin2 + '/' + coin1 in self.tickers:
			return True
		else:
			return False


	def execute_trade(self, ticker, units):
		pass
