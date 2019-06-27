from py.variables import COLUMNS, TRANSACTIONS_FILE, FEE_RATE
import pandas as pd


class Transactions:

    ''' Create transactions.csv if it doesn't already exist '''
    def __init__(self, portfolio):
        try:
            self.transactions = pd.read_JSON(TRANSACTIONS_FILE)
        except:
            self.transactions = pd.DataFrame(columns=COLUMNS)

        for coin, units, price in zip(portfolio.coins, portfolio.units, portfolio.prices):
            if self.transactions.empty or coin not in self.transactions['coin']:
                self._add_coin(coin, units, price, portfolio.date)


    def _add_coin(self, coin, units, price, date):
        ''' Add initial purchase of coin to transactions table '''
        cost = units * price
        self.transactions = self.transactions.append({
            'id': len(self.transactions) + 1,
            'date': date,
            'coin': coin,
            'side': 'buy',
            'units': units,
            'prev_units': 0,
            'cum_units': units,
            'prev_cost': 0,
            'cost': cost,
            'cum_cost': cost,
            # 'cost_per_unit': price,
            # TODO: incorporate fees w/ less units purchased
            'fees': cost * FEE_RATE
            }, ignore_index=True
        )
        return


    def update(self, side, coin, cost, units, date):
        ''' Document transaction data to CSV '''

        coin_txs = self.transactions[self.transactions['coin'] == coin]
        prev_units = coin_txs['cum_units'].iloc[-1]
        prev_cost = coin_txs['cum_cost'].iloc[-1]

        if side == 'buy':
            cum_units = prev_units + units
            cum_cost = prev_cost + cost
        else:  # side == 'sell'
            cum_units = prev_units - units
            cum_cost = prev_cost - cost
            # cost_per_unit = prev_cost / prev_units

        self.transactions = self.transactions.append(
            {
                'id': len(self.transactions) + 1,
                'date': date,
                'coin': coin,
                'side': side,
                # 'price': price,
                'units': units,
                'cost': cost,
                'prev_units': prev_units,
                'cum_units': cum_units,
                'prev_cost': prev_cost,
                'cum_cost': cum_cost,
                'fees': cost * FEE_RATE
                # 'cost_per_unit': cost_per_unit,
                # 'pnl_realised_d_amt': ???,
                # 'pnl_realised_pct': ???,
                # 'pnl_unrealised_d_amt: ???'
            }, ignore_index=True
        )
        return cum_units
