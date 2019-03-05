import ccxt
import pandas as pd




class Coin(object):

    def __init__(self, coin, units, simulated=False):
        self.coin = coin
        self.simulated = simulated
        # self.init_units = units
        # self.current_units = units
        self.init_price = self._fetch_price()
        # self.transactions = {}
        self.pnl_unrealised_d_amt = None
        self.pnl_unrealised_pct = None
        self.pnl_realised_d_amt = None
        self.cost = self.init_price * self.units
        self.fees = None


    def _update_market_val(self):
        self.current_price = self._fetch_price()
        self.init_units = self._fetch_units()
        self.market_val = self.current_price * self.current_units


    def _fetch_price(self):
        if self.simulated:
            return pd.read_csv('../data/historical/prices.csv')[coin][0]
        else:
            return float(binance.fetch_ticker(coin + '/USDT')['info']['lastPrice'])


    def transact(self, side, units):
        d_amt = units * self.current_price
        if side == 'buy':
            self.current_units += units
            self.fees += d_amt * 0.00075
            self.cost = ???

        # side == 'sold'
        else:
            self.current_units -= units
            self.cost = ???
            self.tx_cost = ???
            self.tx_cost_per_unit = ???
