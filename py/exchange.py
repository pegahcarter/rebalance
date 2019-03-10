import ccxt
import pandas as pd

# TODO: generic way to use multiple exchanges?
class Exchange(object):

	def __init__(self, simulated=False, coins=None):
		self.simulated = simulated
		api = pd.read_csv('../api.csv')
		self.binance = ccxt.binance({'options': {'adjustForTimeDifference': True},
					                        'apiKey': api['apiKey'][0],
					                        'secret': api['secret'][0]})
		self.tickers = binance.fetch_tickers().keys()
		balance = self.binance.fetchBalance()['free']
		# 1. Ignore "coin dust", i.e. the small fraction of coin that sometimes
		# 		remains if we aren't able to perfectly sell/transfer 100% of the coin
		# 2. This is based on units of coin owned: if we're rebalancing a coin
		# 		priced at $1 million/coin, units will be less than 0.01
		self.balance = {coin: units
				   for coin, units
				   in balance.items()
				   if units > 0.01}



   def fetch_ticker(self, coin1, coin2):
	   if coin1 + '/' + coin2 in self.tickers:
		   return coin1 + '/' + coin2
	   elif coin2 + '/' + coin1 in self.tickers:
		   return coin2 + '/' + coin1


    def fetch_price(self, coin):
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


	def fetch_units(self, ticker, d_amt):
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
