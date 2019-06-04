import time
import pandas as pd
import exchange
import models

hist_prices = pd.read_csv('../data/historical/prices.csv')
START_DATE = int(hist_prices['timestamp'][0])
TRANSACTIONS_FILE = '../data/transactions/transactions.csv'

COLUMNS = ['date', 'coin', 'side', 'units', 'price_per_unit', 'fees', 'prev_units',
           'cum_units', 'tx_val', 'prev_cost', 'tx_cost',
           'tx_cost_per_unit', 'cum_cost', 'gain_loss', 'realised_pct']


def initialize(PORTFOLIO_START_VALUE=None, coins=None):
    ''' Create transactions.csv'''
    try:
        df = pd.read_csv(TRANSACTIONS_FILE)
    except:
        df = pd.DataFrame(columns=COLUMNS)
        df.to_csv(TRANSACTIONS_FILE, index=False)

    portfolio = models.Portfolio(coins, PORTFOLIO_START_VALUE)
    for coin, units in zip(portfolio.coins, portfolio.units):
        if df.empty or coin not in set(df['coin']):
            add_coin(coin, units, PORTFOLIO_START_VALUE)


def add_coin(coin, units, PORTFOLIO_START_VALUE=None):
    ''' Add initial purchase of coin to transactions table '''

    date = time.time()
    price = exchange.fetch_price(coin)
    # NOTE: if we were running a simulation, we'd want to define the variables different:
    #     date = START_DATE
    #     price = hist_prices[coin][0]
    df = pd.read_csv(TRANSACTIONS_FILE)
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

    df = df.append(row, ignore_index=True)
    df.to_csv(TRANSACTIONS_FILE, index=False)


def update(trade_coins, trade_sides, trade_units, trade_usd_value, date=None,
           current_price=None, tx_cost_per_unit=None, tx_cost=None, gain_loss=None,
           realised_pct=None, fees=None):
    ''' Document transaction data to CSV '''

    for coin, side, units in zip(trade_coins, trade_sides, trade_units):
        df = pd.read_csv(TRANSACTIONS_FILE)
        prev_units = df[df['coin'] == coin]['cum_units'].iloc[-1]
        prev_cost = df[df['coin'] == coin]['cum_cost'].iloc[-1]
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

        df = df.append({'date': date,
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
    df.to_csv(TRANSACTIONS_FILE, index=False)
