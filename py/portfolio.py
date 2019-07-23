# from py.exchange import Exchange
from datetime import datetime
from py.variables import FEE_RATE, TRANSACTIONS_FILE, SUMMARY_FILE
import pandas as pd
import numpy as np
import itertools


class Portfolio:
	'''	Represents our account balance on Binance '''

	# exchange = Exchange()
	FEE_RATE = FEE_RATE

	def __init__(self, coins=None, PORTFOLIO_START_VALUE=None):
		self.PORTFOLIO_START_VALUE = PORTFOLIO_START_VALUE
		if PORTFOLIO_START_VALUE:
			hist_prices = pd.read_csv('src/assets/prices.csv', usecols=['date'] + coins)
			self.dates = hist_prices.pop('date')
			self.hist_prices = np.array(hist_prices)
			prices = self.hist_prices[0]
			amt_each = PORTFOLIO_START_VALUE / len(coins)
			units =  np.divide(amt_each, prices)
		# else: # This is not a simulation.  Rebalance our own portfolio.
			# TODO: figure out how to include/ignore USDT
			# date = datetime.now()
			# balance = self.exchange.fetch_balance()
			# coins = balance.keys()
			# prices = np.array([self.exchange.fetch_price(coin) for coin in coins])
			# units = balance.values()

		# self.date = date
		self.tx_count = 0
		self.coins = {coin: [] for coin in coins}
		self.avg_weight = 1.0/len(coins)
		self.start_units = units
		self.units = units
		for coin, coin_units, price in zip(coins, units, prices):
			self._add_coin(coin, coin_units, price)


	def _add_coin(self, coin, coin_units, price):
		self.tx_count += 1
		cost = coin_units * price
		self.coins[coin].append({
			'id': self.tx_count,
			'date': self.dates[0],
			'coin': coin,
			'side': 'BUY',
			'price': price,
			'units': coin_units,
			'cost': cost,
			'prev_units': 0,
			'cum_units': coin_units,
			'prev_cost': 0,
			'cum_cost': cost,
			# 'cost_per_unit': price
			'fees': cost * self.FEE_RATE
		})
		return


	def trade(self, side, coin_index, cost, i=None):
		self.tx_count += 1
		price = self.hist_prices[i, coin_index]
		units = cost/price
		coin = list(self.coins)[coin_index]
		prev_units = self.coins[coin][-1]['cum_units']
		prev_cost = self.coins[coin][-1]['cum_cost']

		if side == 'SELL':
			units *= -1.0
			cost *= -1.0

		self.coins[coin].append({
			'id': self.tx_count,
			'date': self.dates[i],
			'coin': coin,
			'side': side,
			'price': price,
			'units': units,
			'cost': cost,
			'prev_units': prev_units,
			'cum_units': prev_units + units,
			'prev_cost': prev_cost,
			'cum_cost': prev_cost + cost,
			'fees': abs(cost) * self.FEE_RATE
			# 'cost_per_unit': cost_per_unit,
			# 'pnl_realised_d_amt': ???,
			# 'pnl_realised_pct': ???,
			# 'pnl_unrealised_d_amt: ???'
		})
		self.units[coin_index] += units
		# if self.PORTFOLIO_START_VALUE is None:
		# 	exchange.create_order(coin, side, units)
		return self.units[coin_index]



	def summarize(self):
		''' Saves coin and transaction data '''

		transactions = list(itertools.chain(*self.coins.values()))
		transactions = pd.DataFrame(transactions).sort_values(by='id')
		transactions.to_json(TRANSACTIONS_FILE, orient='records')

		summary = []
		for i, coin in enumerate(self.coins):
			price = self.hist_prices[-1, i]
			units = self.coins[coin][-1]['cum_units']
			cost = self.coins[coin][-1]['cum_cost']
			summary.append({
				'coin': coin,
				'price': price,
				'units': units,
				'cost': cost,
				'market_val': price * units
				# 'unit_cost': ???,
				# 'pnl_unrealised_d_amt': ???,
				# 'pnl_unrealised_pct': ???,
				# 'pnl_realised_d_amt': ???,
				# 'gain_loss': ???,
			})
		summary = pd.DataFrame(summary)
		summary.to_json(SUMMARY_FILE, orient='records')
		return



# Old code from transactions.py.  Keeping for future reference
# try:
#     self.transactions = pd.read_JSON(TRANSACTIONS_FILE)
# except:
#     self.transactions = pd.DataFrame(columns=COLUMNS)
# for coin, units, price in zip(portfolio.coins, portfolio.units, portfolio.prices):
# 	if self.transactions.empty or coin not in self.transactions['coin']:
# 		self._add_coin(coin, units, price, portfolio.date)
