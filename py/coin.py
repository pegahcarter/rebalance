import ccxt

api = ccxt.binance()


class Coin(object):

    def __init__(self, ticker, units, date=None):
        self.ticker = ticker
        self.init_price = None
        self.init_units = units
        self.current_units = units
        self.current_price = self._fetch_price()
        self.transactions = {}
        self.pnl_unrealised_d_amt = None
        self.pnl_unrealised_pct = None
        self.pnl_realised_d_amt = None
        self.cost = None
        self.fees = None


    def update_market_val(self):
        self.current_price = self._fetch_price()
        self.market_val = self.current_price * self.current_units


    def _fetch_price(self):
        if self.date:
            # TODO: add param to get price based on date
            # NOTE: Can I put the date critera into fetch_ticker?
        else:
            btc_price = float(api.fetch_ticker('BTC/USDT')['info']['lastPrice']
            if self.ticker == 'BTC':
                return btc_price
            else:
                btc_ratio = float(api.fetch_ticker(coin + '/BTC')['info']['lastPrice'])
                return btc_ratio


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
