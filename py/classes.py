import pandas as pd

# NOTE: Is there a difference between `tx_cost`  and `tx_val`
class Transactions(object):
    def __init__(self):
        self.trade_id = trade_id
        self.coin = coin
        self.date = date
        self.side = side
        self.price = price
        self.fees = fees
        self.tx_val = tx_val
        self.tx_cost_per_unit = cost_per_unit

        self.units = units
        self.prev_units = prev_units
        self.cum_units = cum_units

        self.tx_cost = cost
        self.prev_cost = prev_cost
        self.cum_cost = cum_cost

        self.pnl_realised_d_amt = pnl_realised_d_amt
        self.pnl_realised_pct = pnl_realised_pct

    def fetch_market_val(self):
        pass


class Coin:
    hist_prices = pd.read_csv('../../data/historical/prices.csv')
    def __init__(self):
        self.cost = cost
        self.market_val = market_val
        self.pnl_unrealised_d_amt = pnl_unrealised_d_amt
        self.pnl_realised_d_amt = pnl_realised_d_amt
        self.pnl_unrealsed_pct = pnl_unrealsed_pct
        self.fees = fees

        self.hist_prices = hist_prices
        self.price = price
        self.units = units

    def _calculate_start_units(self, coin):
        if simulated:
            units = (d_amt_invested/num_coins) / coin['hist_prices'][0]
        else:
            units = balance[coin]

    def fetch_price(self):
        pass

    def calculate_units(self, d_amt):
        pass


class Exchange:
    def __init__(self, simulated, coins=None):
        self.exchange = ccxt.binance({'options': {'adjustForTimeDifference': True},
                                      'apiKey': api['apiKey'][0],
                                      'secret': api['secret'][0]})
        self.tickers = (set(ticker.split('/')) for ticker in self.exchange.fetchTickers())
        self.all_balances = exchange.fetchBalance()['free']
        if coins is None:
            if simulated:
                coins = random.sample(list(balance), 5) # TODO: need @param for num of coins
            else: # not simulated
                coins = [coin for coin, units in balance.items() if units > 0]

        self.coins = {}
        [self.coins[coin] = {'hist_prices': hist_prices[coin].tolist(),
                             'price': self.fetch_price(coin, simulated)} for coin in coins]

    def execute_trade(self):
        pass
