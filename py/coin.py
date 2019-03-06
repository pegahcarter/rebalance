import pandas as pd


class Coin(object):

    def __init__(self, coin, binance, simulated=None):

        self.coin = coin
        self.simulated = simulated

        if simulated:
            self.hist_prices = pd.read_read_csv('../data/historical/prices.csv')[coin].tolist()

        self.binance = binance
        self.balance = self.binance.fetchBalance()
        self.init_price = self._fetch_price()
        self.init_units = self._fetch_units()
        self.init_cost = self.init_price * self.init_units
        self.market_val = self.init_cost

        # self.current_units = units
        # self.transactions = {}
        # self.pnl_unrealised_d_amt = None
        # self.pnl_unrealised_pct = None
        # self.pnl_realised_d_amt = None
        # self.cost = self.init_price * self.units
        # self.fees = None


    def _update_market_val(self):
        self.current_price = self._fetch_price()
        self.init_units = self._fetch_units()
        self.market_val = self.current_price * self.current_units


    def _fetch_price(self):
        if self.simulated:
            return self.hist_prices[0]
        else:
            return float(self.binance.fetch_ticker(coin + '/USDT')['info']['lastPrice'])


    def _fetch_units(self):
        if self.simulated:
            return 1000 / self.init_price
        else:
            return self.balance[self.coin]['total']


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
