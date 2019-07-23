from py.portfolio import Portfolio
from py.variables import INTERVAL, COINS, PORTFOLIO_START_VALUE, TRANSACTIONS_FILE
import py.rebalance as rebalance


portfolio = Portfolio(COINS, PORTFOLIO_START_VALUE)
for i in range(1, len(portfolio.hist_prices)):
    if i % INTERVAL == 0:
        rebalance.run(portfolio, i)


portfolio.transactions.transactions.to_json('src/assets/transactions.json', orient='records')
portfolio.summarize()


# Code to create simulated non-rebalanced portfolio
import pandas as pd
portfolio_lame = Portfolio(COINS, PORTFOLIO_START_VALUE)

test = pd.read_csv('src/assets/prices.csv', usecols=['date'] + COINS)
a = test.pop('date')


portfolio_lame.units



hr_totals = [PORTFOLIO_START_VALUE]
transactions.initialize(TRANSACTIONS_FILE, PORTFOLIO_START_VALUE, coins)
simulations = pd.DataFrame(columns=['timestamp', 'hodl', 'rebalanced'])

for index, row in prices.iterrows():
    if index % INTERVAL == 0:
        portfolio = rebalance.run(coins)

    # Append hodl total value

    # Append rebalanced total value
