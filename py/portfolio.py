from coin import Coin
import ccxt

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

        # self._update_portfolio()


    def _add_coin(self, coin, units):

        self.coins[coin] = Coin(coin, units, simulated)
        self._update_portfolio()


    def _fetch_units(self):
        if self.simulated:
            return 1000 / self.init_price
        else:
            return balance[self.coin]['total']


    def refresh(self):
        '''
        Updates the market value of all coins in our portfolio
        '''
        for coin in self.coins:
            # Update with current prices
            self.coin._update_market_val()



    def trade_coin(self, ticker, side, units, date=None):
        pass
