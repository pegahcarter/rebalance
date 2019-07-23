from py.transactions import Transactions
from py.exchange import Exchange
from py.variables import FEE_RATE
from datetime import  datetime
import pandas as pd
import numpy as np

class Portfolio:
	'''	Represents our account balance on Binance '''

	# exchange = Exchange()
	FEE_RATE = FEE_RATE

	def __init__(self, COINS=None, PORTFOLIO_START_VALUE=None):
		self.PORTFOLIO_START_VALUE = PORTFOLIO_START_VALUE
		if PORTFOLIO_START_VALUE:
			hist_prices = pd.read_csv('src/assets/prices.csv', usecols=['date'] + COINS)
			self.dates = hist_prices.pop('date')
			self.hist_prices = np.array(hist_prices)
			# date = self.dates[0]
			# prices = self.hist_prices[0]
			amt_each = PORTFOLIO_START_VALUE / len(COINS)
			units =  np.divide(amt_each, self.hist_prices[0, :])
		# else: # This is not a simulation.  Rebalance our own portfolio.
			# TODO: figure out how to include/ignore USDT
			# date = datetime.now()
			# balance = self.exchange.fetch_balance()
			# coins = balance.keys()
			# prices = np.array([self.exchange.fetch_price(coin) for coin in coins])
			# units = balance.values()

		# self.date = date
		self.tx_count = 0
		self.coins = {coin: [] for coin in COINS}
		self.avg_weight = 1.0/len(self.coins)
		self.start_units = units
		self.units = units
		for coin, coin_units, price in zip(COINS, units, self.hist_prices[0]):
			_add_coin(coin, coin_units, price)


	def _add_coin(self, coin, coin_units, price):
		cost = coin_units * price
		self.tx_count += 1
		self.coins[coin].append({
			'id': tx_count,
			'date': self.dates[0],
			'coin': coin,
			'side': 'BUY',
			'units': coin_units,
			'prev_units': 0,
			'cum_units': coin_units,
			'prev_cost': 0,
			'cost': cost,
			'cum_cost': cost,
			# 'cost_per_unit': price
			'fees': cost * self.FEE_RATE
		})
		return



	def trade(self, cost, data):
		''' Executes a buy and sell order '''

		for side, index in data:
			coin = self.coins[index]
			price = self.prices[index]
			units = cost/price
			self.units[index] = self.transactions.update(side, coin, cost, units, self.date)
			# if self.PORTFOLIO_START_VALUE is None:
			# 	exchange.create_order(coin, side, units)


	def summarize(self):
		''' Saves grouped coin data to coins.json '''

		summary = []
		for i, coin in enumerate(self.coins):
			tx = self.transactions.transactions.copy()
			coin_df = tx[tx['coin'] == coin]
			summary.append({
				'coin': coin,
				'price': self.prices[i],
				'units': self.units[i],
				'cost': coin_df.iloc[-1]['cum_cost'],
				# 'unit_cost': ???,
				# 'pnl_unrealised_d_amt': ???,
				# 'pnl_unrealised_pct': ???,
				# 'pnl_realised_d_amt': ???,
				# 'gain_loss': ???,
				'market_val': self.prices[i] * self.units[i]
			})
		summary = pd.DataFrame(summary)
		summary.to_json('src/assets/coins.json', orient='records')
