from py.portfolio import Portfolio
from py.variables import *
import py.rebalance as rebalance
import pandas as pd
import numpy as np


df_rebalanced = [PORTFOLIO_START_VALUE]
df_hodl = [PORTFOLIO_START_VALUE]
portfolio = Portfolio(COINS, PORTFOLIO_START_VALUE)

for i in range(1, len(portfolio.hist_prices)):
    if i % INTERVAL == 0:
        portfolio = rebalance.run(portfolio, i)
    # Append hodl total value
    df_rebalanced.append(np.dot(portfolio.units, portfolio.hist_prices[i]))
    # Append rebalanced total value
    df_hodl.append(np.dot(portfolio.start_units, portfolio.hist_prices[i]))


sim_results = pd.DataFrame(zip(portfolio.dates, df_hodl, df_rebalanced), columns=['date', 'hodl', 'rebalanced'])
sim_results.to_json(SIM_RESULTS_FILE, orient='records')


portfolio.summarize()
