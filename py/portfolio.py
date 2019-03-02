import coin

test = {'a':1, 'b':2,'c':3}


class Portfolio(object):

    def __init__(self, coins=None, start_d_amt=None, transactions=None):
        self.cost = None
        self.market_val = None
        self.coins = {}
        self.pnl_unrealised_d_amt = None
        self.pnl_unrealised_pct = None
        self.pnl_realised_d_amt = None
        self.total_fees = None

    def _add_coin(self, ticker, units, price, date=None):
        if ticker not in self.coins:

            self.coins[coin] = Coin(*args)
            self._update_portfolio()

        pass

    def _update_portfolio(self):
        '''
        Updates the market value of all coins in our portfolio
        '''
        for coin in self.coins:
            # Update with current prices
            self.coin.update_market_val()

    def trade_coin(self, ticker, side, units)
