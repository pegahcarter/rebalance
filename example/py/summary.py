

class Summary:

    fee_rate = 0.0075
    slippage_rate = 0.01

    def __init__(self):
        self.cost = cost
        self.market_val = market_val
        self.pnl_unrealised_d_amt = pnl_unrealised_d_amt
        self.pnl_realised_d_amt = pnl_realised_d_amt
        self.pnl_unrealsed_pct = pnl_unrealsed_pct
        self.fees = fees

        self.tx_count = tx_count
        self.coins = coins # NOTE: only as list


    def fetch_price(self, coin, date):
        return hist_prices[coin][date] # TODO
