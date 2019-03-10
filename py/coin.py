

class Coin(object):

    def __init__(self, coin, tx_count, simulated=False, hist_prices=None):
        self.ticker = coin
        self.hist_prices = hist_prices
        self.current_price = None
        self.market_val = 0

        self.pnl_unrealised_d_amt = 0
        self.pnl_unrealised_pct = 0
        self.pnl_realised_d_amt = 0
        self.fees = 0

        self.transactions = []




    def _update_market_val(self):
        self.current_price = self._fetch_price()
        self.init_units = self._fetch_units()
        self.market_val = self.current_price * self.current_units


    def _fetch_price(self):
        if self.hist_prices is not None:
            return self.hist_prices[0]
        else:
            # NOTE: what about tether??
            return float(self.binance.fetch_ticker(coin + '/USDT')['info']['lastPrice'])


    def _fetch_units(self):
        if self.simulated:
            return 1000 / self.hist_prices[0]
        else:
            # NOTE: should balance be passed into this function as a @param?
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
