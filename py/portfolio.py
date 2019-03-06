import ccxt
import pandas as pd
from coin import Coin

api = pd.read_csv('../api.csv')
binance = ccxt.binance({'options': {'adjustForTimeDifference': True},
			                        'apiKey': api['apiKey'][0],
			                        'secret': api['secret'][0]})


class Portfolio(object):

    def __init__(self, simulated=None, backtest=None, coins=None):
        self.simulated = simulated
        self.backtest = backtest
        self.cost = None
        self.market_val = None
        self.coins = {}
        self.pnl_unrealised_d_amt = None
        self.pnl_unrealised_pct = None
        self.pnl_realised_d_amt = None
        self.fees = None
		self.binance = binance

        self._update_portfolio(coins)


	def _update_portfolio(self, coins):
		if not self.simulated:
			coins = [asset['asset']
					 for asset in balance['info']['balances']
					 if (float(asset['free']) > 0)]

		for coin in coins:
			self._add_coin(coin)


    def _add_coin(self, coin):
        self.coins[coin] = Coin(coin, self.binance, self.simulated)


    def refresh(self):
        for coin in self.coins:
            # Update with current prices
            self.coin._update_market_val()


	def rebalance(self, coins_to_rebalance, d_amt):
		# a. market value should already be updated
		# b. we need to still determine units to trade
		pass


    def trade_coin(self, ticker, side, units, date=None):
        pass
