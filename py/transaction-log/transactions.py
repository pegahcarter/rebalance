from variables import COLUMNS, TRANSACTIONS_FILE
import pandas as pd


class Transactions:

    ''' Create transactions.csv if it doesn't already exist '''
    def __init__(self, portfolio):
        try:
            transactions = pd.read_csv(TRANSACTIONS_FILE)
        except:
            transactions = pd.DataFrame(columns=COLUMNS)

        for coin, units, price in zip(portfolio.coins, portfolio.units, portfolio.prices):
            if transactions.empty or coin not in transactions['coin']:
                add_coin(coin, units, price, portfolio.date)
        self.transactions = transactions


def add_coin(coin, units, price, date):
    ''' Add initial purchase of coin to transactions table '''

    row = {'date': date,
           'coin': coin,
           'side': 'buy',
           'units': units,
           'price_per_unit': price,
           'fees': price * units * 0.00075,
           'prev_units': 0,
           'cum_units': units,
           'tx_val': price * units,
           'prev_cost': 0,
           'cum_cost': price * units,
           'gain_loss': 0}

    transactions = transactions.append(row, ignore_index=True)


def update(trade_coins, trade_sides, trade_units, trade_usd_value, date=None,
           current_price=None, tx_cost_per_unit=None, tx_cost=None, gain_loss=None,
           realised_pct=None, fees=None):
    ''' Document transaction data to CSV '''

    for coin, side, units in zip(trade_coins, trade_sides, trade_units):
        transactions = pd.read_csv(TRANSACTIONS_FILE)
        prev_units = transactions[transactions['coin'] == coin]['cum_units'].iloc[-1]
        prev_cost = transactions[transactions['coin'] == coin]['cum_cost'].iloc[-1]
        if date is None:
            date = time.time()
            current_price = exchange.fetch_price(coin)

        if side == 'buy':
            fees = trade_usd_value * 0.00075
            cum_units = prev_units + units
            cum_cost = prev_cost + trade_usd_value
        else:
            cum_units = prev_units - units
            tx_cost_per_unit = prev_cost / prev_units
            tx_cost = units / prev_units * prev_cost
            cum_cost = prev_cost - trade_usd_value
            gain_loss = trade_usd_value - tx_cost
            realised_pct = gain_loss / tx_cost

        transactions = transactions.append({'date': date,
                        'coin': coin,
                        'side': side,
                        'units': units,
                        'price_per_unit': current_price,
                        'fees': fees,
                        'prev_units': prev_units,
                        'cum_units': cum_units,
                        'tx_val': current_price * units,
                        'prev_cost': prev_cost,
                        'tx_cost':  tx_cost,
                        'tx_cost_per_unit': tx_cost_per_unit,
                        'cum_cost': cum_cost,
                        'gain_loss': gain_loss,
                        'realised_pct': realised_pct}, ignore_index=True)

    # Save updated dataframe to CSV
    transactions.to_csv(TRANSACTIONS_FILE, index=False)
