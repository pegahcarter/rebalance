# File used to create simulate code
from models import Portfolio
import pandas as pd
import transactions
import rebalance

FREQUENCY = 'daily'
INTERVAL = 24
coins = ['BTC','ETH','XRP','LTC','XLM'] # TODO: dynamic coins
PORTFOLIO_START_VALUE = 5000
hr_totals = [PORTFOLIO_START_VALUE]
TRANSACTIONS_FILE = '../data/simulations/transactions.csv'
hist_prices = pd.read_csv('../data/historical/prices.csv')[['timestamp'] + coins]


transactions.initialize(TRANSACTIONS_FILE, PORTFOLIO_START_VALUE, coins)

simulations = pd.DataFrame(columns=['timestamp', 'hodl', 'rebalanced'])



for index, row in prices.iterrows():
    if index % INTERVAL == 0:
        portfolio = rebalance.run(coins)

    # Append hodl total value

    # Append rebalanced total value
