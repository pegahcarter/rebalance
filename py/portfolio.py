import ccxt
import pandas as pd
from coin import Coin


hist_prices = pd.read_csv('../data/historical/prices.csv')
api = pd.read_csv('../api.csv')
binance = ccxt.binance({'options': {'adjustForTimeDifference': True},
			                        'apiKey': api['apiKey'][0],
			                        'secret': api['secret'][0]})


class Portfolio(object):

    def __init__(self, simulated=False, backtest=False, coins=None):
		self.hist_prices = hist_prices
        self.simulated = simulated
		self.backtest = backtest
		self.binance = binance
		self.balance = binance.fetchBalance()
        self.cost = 0
        self.market_val = 0
        self.pnl_unrealised_d_amt = 0
        self.pnl_unrealised_pct = 0
        self.pnl_realised_d_amt = 0
        self.fees = 0
		self.fee_rate = 0.0075
		self.slippage_rate = 0.02
		self.tx_count = 0

		self.coins = {}

        self._update_portfolio(coins)


	def _update_portfolio(self, coins):
		if not self.simulated:
			coins = [asset['asset']
					 for asset in self.balance['info']['balances']
					 if (float(asset['free']) > 0)]

		for coin in coins:
			self._add_coin(coin)

	# NOTE: this should add the initial purchase tx
    def _add_coin(self, coin):
		# NOTE: use num_transactions for tx id
		tx_count += 1
        self.coins[coin] = Coin(coin, tx_count, self.binance, self.simulated)


    def refresh(self):
        for coin in self.coins:
            # Update with current prices
            self.coin._update_market_val()


	def rebalance(self, coins_to_rebalance, d_amt):
		# a. market value should already be updated
		# b. we still need to determine units to trade
		pass


    def trade_coin(self, ticker, side, units, date=None):
        pass
