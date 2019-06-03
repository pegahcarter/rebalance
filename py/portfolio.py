import ccxt
import pandas as pd
from py.coin import Coin
from exchange import Exchange


class Portfolio(Exchange):

    def __init__(self, **kwargs):
        self.transactions = []
        coins = kwargs.pop(coins)
        for key, val in kwargs.items():
            setattr(self, key, val)

        self.coins = {}
        for coin in coins:
            price = self.prices[coin].at[0]
            self.coins[coin] = Coin(
                coin=coin,
                trade_id=len(self.transactions) + 1,
                price=price,
                units=self.start_amt/price,
                fee_rate = self.fee_rate
            )

        # self.cost = 0
        # self.market_val = 0
        # self.pnl_unrealised_d_amt = 0
        # self.pnl_unrealised_pct = 0
        # self.pnl_realised_d_amt = 0
        # self.fees = 0
		# self.fee_rate = 0.0075
		# self.slippage_rate = 0.02
		# self.tx_count = 0
        #
		# self.coins = {}
        #
        # self._update_portfolio(coins)
        # def _update_portfolio(self, coins):
        #     if not self.simulated:
        #         coins = self.exchange.balance.keys()
        #
        #         for coin in coins:
        #             self._add_coin(coin)



	# NOTE: this should add the initial purchase tx
    def _add_coin(self, coin):
		# NOTE: use num_transactions for tx id
		tx_count += 1
        self.coins[coin] = Coin(coin, tx_count)


    def refresh(self):
        for coin in self.coins:
            # Update with current prices
            self.coin._update_market_val()


	def rebalance(self, coins_to_rebalance, d_amt):
		# a. market value should already be updated
		# b. we still need to determine units to trade
		pass
