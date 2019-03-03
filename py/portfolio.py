from coin import Coin


class Portfolio(object):

    def __init__(self, coins=None, start_d_amt=None, transactions=None):
        self.cost = None
        self.market_val = None
        self.coins = {}
        self.pnl_unrealised_d_amt = None
        self.pnl_unrealised_pct = None
        self.pnl_realised_d_amt = None
        self.fees = None

        self._update_portfolio()


    def _add_coin(self, ticker, units, price=None, date=None):
        if ticker not in self.coins:

            self.coins[coin] = Coin(ticker, price, date)
            self._update_portfolio()

        pass


    def _update_portfolio(self):
        '''
        Updates the market value of all coins in our portfolio
        '''
        for coin in self.coins:
            # Update with current prices
            self.coin._update_market_val()



    def trade_coin(self, ticker, side, units, date=None):
        pass
