import pandas as pd
# import ccxt
import json

class Portfolio:

    # api = ccxt.binance()
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

        self.prices = self.prices[['timestamp'] + coins]
        for coin in coins:
            # if coin not in map(lambda tx: tx['coin'], transactions):
            if coin not in self.coins:
                self.coins[coin] = {}
                self._add_coin(coin=coin)

    def _add_coin(self, coin):
        price = self.get_price(coin)
        cost = 1000
        fees = cost * self.fee_rate
        units = (cost - fees)/price
        date = self.prices['timestamp'][0]
        self._add_transaction(coin, 'BUY', units, cost, price, date)

    def _add_transaction(self, coin, side, units, cost, price, date):
        tx = {
            'id': len(self.transactions) + 1,
            'date': date,
            'coin': coin,
            'side': side,
            'units': units * (1 - self.slippage_rate),
            'cost': cost,
            'price': price,
            'fees': cost * self.fee_rate
        }
        try:
            coin_txs = self.get_coin_txs(coin)
            tx['prev_cost'] = coin_txs['prev_cost'][-1]
            tx['prev_units'] = coin_txs['cum_units'][-1]
        except:  # There are no prior transactions with the coin
            tx['prev_cost'] = 0
            tx['prev_units'] = 0
        if side == 'BUY':
            tx['cum_cost'] = tx['prev_cost'] + cost
            tx['cum_units'] = tx['prev_units'] + units
        else:  # side == 'SELL'
            tx['cum_cost'] = tx['prev_units'] - cost  # THIS
            tx['cum_units'] = tx['prev_units'] - units  # THIS
            tx['cost_per_unit'] = tx['prev_cost'] / tx['prev_units']  # THIS
            tx['tx_cost'] = units / tx['prev_units'] * tx['prev_cost']
            tx['pnl_realised_d_amt'] = cost - tx['tx_cost']
            tx['pnl_realised_pct'] = tx['pnl_realised_d_amt'] / tx['tx_cost']
        self.transactions.append(tx)

    def get_price(self, coin, i=0):
        if self.simulated:
            return self.prices[coin][i]
        btc_price = self.api.fetch_ticker('BTC/USDT')['info']['lastPrice']
        if coin == 'BTC':
            return btc_price
        else:
            return btc_price * self.api.fetch_ticker(coin + '/BTC')['info']['lastPrice']

    def get_coin_txs(self, coin):
        tx_df = pd.DataFrame(self.transactions)
        return tx_df.loc[tx_df['coin'] == coin].reset_index(drop=True)

    def update_coins(self, i=0):
        for coin in self.coins:
            Coin = {}
            Coin['price'] = self.get_price(coin, i)
            coin_txs = self.get_coin_txs(coin)
            Coin['cost'] = coin_txs['cum_cost'][len(coin_txs)-1]
            Coin['units'] = coin_txs['cum_units'][len(coin_txs)-1]
            Coin['cost_per_unit'] = Coin['cost']/Coin['units']
            Coin['market_val'] = Coin['units'] * Coin['price']
            Coin['pnl_unrealised_d_amt'] = (Coin['price'] - Coin['cost_per_unit']) * Coin['units']
            try:
                Coin['pnl_realised_d_amt'] = coin_txs['pnl_realised_d_amt']
            except:  # Coin has not yet been sold in a tx
                Coin['pnl_realised_d_amt'] = 0
            # pnl_unrealised_pct =
            Coin['fees'] = coin_txs['fees'].sum()
            self.coins[coin] = Coin
