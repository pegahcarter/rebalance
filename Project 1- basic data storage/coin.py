import pandas as pd


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
