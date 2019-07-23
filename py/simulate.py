from py.portfolio import Portfolio
from py.variables import INTERVAL, COINS, PORTFOLIO_START_VALUE, TRANSACTIONS_FILE
import py.rebalance as rebalance
import pandas as pd
import numpy as np


portfolio = Portfolio(COINS, PORTFOLIO_START_VALUE)
for i in range(1, len(portfolio.hist_prices)):
    if i % INTERVAL == 0:
        portfolio.date = portfolio.dates[i]
        portfolio.prices = portfolio.hist_prices[i]
        rebalance.run(portfolio)


portfolio.transactions.transactions.to_json('src/assets/transactions.json', orient='records')
portfolio.summarize()





portfolio_lame = Portfolio(COINS, PORTFOLIO_START_VALUE)
np.multiply(portfolio_lame.units, portfolio_lame.hist_prices)

portfolio_lame.hist_prices[0].dot(portfolio_lame.units)


hr_totals = [PORTFOLIO_START_VALUE]
transactions.initialize(TRANSACTIONS_FILE, PORTFOLIO_START_VALUE, coins)
simulations = pd.DataFrame(columns=['timestamp', 'hodl', 'rebalanced'])

for index, row in prices.iterrows():
    if index % INTERVAL == 0:
        portfolio = rebalance.run(coins)

    # Append hodl total value

    # Append rebalanced total value
