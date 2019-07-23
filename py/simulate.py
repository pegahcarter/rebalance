from py.portfolio import Portfolio
from py.variables import INTERVAL, COINS, PORTFOLIO_START_VALUE, TRANSACTIONS_FILE
import py.rebalance as rebalance
import itertools
import pandas as pd



portfolio = Portfolio(COINS, PORTFOLIO_START_VALUE)
df_rebalanced = [PORTFOLIO_START_VALUE]
df_hodl = [PORTFOLIO_START_VALUE]

for i in range(1, len(portfolio.hist_prices)):
    if i % INTERVAL == 0:
        rebalance.run(portfolio, i)
    # Append hodl total value
    df_rebalanced.append(portfolio.units.dot(portfolio.hist_prices[i]))
    # Append rebalanced total value
    df_hodl.append(portfolio.start_units.dot(portfolio.hist_prices[i]))


df = pd.DataFrame(zip(portfolio.dates, df_hodl, df_rebalanced), columns=['date', 'hodl', 'rebalanced'])
