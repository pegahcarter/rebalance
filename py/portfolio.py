import pandas as pd
import ccxt
import json

class Portfolio:

    slippage_rate = slippage_rate
    api = ccxt.binance()
    prices = pd.read_csv('data/historical/prices.csv')

    def __init__(self, simulated=False, coins=None, fee_rate=None, slippage_rate=None):
        try:
            with open('portfolio.json', 'r') as f:
                portfolio = json.load(f)
                for key, val in portfolio.items():
                    setattr(self, key, val)
        except:
            self.transactions = []
            self.coins = {}
            self.simulated = simulated
            self.fee_rate = fee_rate
            self.slippage_rate = slippage_rate
            self.cost = 0
            self.market_val = 0
            self.pnl_unrealised_d_amt = 0
            self.pnl_realised_d_amt = 0
            self.pnl_unrealsed_pct = 0
            self.fees = 0

        self.transactions = pd.Dataframe(self.transactions)
        self.prices = self.prices[['timestamp'] + coins]
        for coin in coins:
            # if coin not in map(lambda tx: tx['coin'], transactions):
            if coin not in self.coins:
                self._add_coin(coin=coin)

    def _add_coin(self, coin):
        price = self.get_price(coin)
        cost = 1000
        fees = cost * self.fee_rate
        units = (cost - fees)/price
        date = self.prices['timestamp'][0]
        self._add_transaction(coin, 'BUY', units, cost, price, date)

    def _add_transaction(coin, side, units, cost, price, date):
        coin_txs = get_coin_txs(coin)
        tx = {
            'date': date,
            'side': side,
            'units': units,
            'cost': cost,
            'price': price,
            'date': date
        }

        tx['prev_cost'] = coin_txs['prev_cost'][-1]
        tx['prev_units'] = coin_txs['cum_units'][-1]
        # TODO: figure out where to place fees
        if side == 'BUY':
            tx['cum_cost'] = prev_cost + cost
            tx['cum_units'] = prev_units + units
        else:  # side == 'SELL'
            tx['cum_cost'] = prev_units - cost
            tx['cum_units'] = prev_units - units
            tx['tx_cost_per_unit'] = prev_cost / prev_units
            tx['tx_cost'] = units / prev_units * prev_cost
            tx['pnl_realised_d_amt'] = cost - tx_cost
            tx['pnl_realised_pct'] = pnl_realised_d_amt / tx_cost
        self.transactions.append(tx, ignore_index=True)

    def get_price(self, coin, i=0):
        if self.simulated:
            return self.prices[coin][i]
        btc_price = self.api.fetch_ticker('BTC/USDT')['info']['lastPrice']
        if coin == 'BTC':
            return btc_price
        else:
            return btc_price * self.api.fetch_ticker(coin + '/BTC')['info']['lastPrice']

    def get_coin_txs(self, coin):
        return self.tranasactions.loc[self.transactions['coin'] == coin]

    def update_coins(self, i=0):
        for coin in self.coins:
            coin_txs = get_coin_txs(coin)
            data = {}
            data['price'] = self.get_price(coin, i)
            data['cost'] = coin_txs['cum_cost'][-1]
            data['units'] = coin_txs['cum_units'][-1]
            data['cost_per_unit'] = data['cost']/data['units']
            data['market_val'] = data['units'] * data['price']
            data['pnl_unrealised_d_amt'] = (data['price'] - data['cost_per_unit']) * data['units']
            data['pnl_realised_d_amt'] = coin_txs['pnl_realised_d_amt']
            # pnl_unrealised_pct =
            data['fees'] = coin_txs['fees'].sum()
            self.coins[coin] = data
