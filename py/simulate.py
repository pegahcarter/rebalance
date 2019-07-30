from py.portfolio import Portfolio
from py.variables import *
import py.rebalance as rebalance
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


df_rebalanced = [PORTFOLIO_START_VALUE]
df_hodl = [PORTFOLIO_START_VALUE]
portfolio = Portfolio(COINS, PORTFOLIO_START_VALUE)

for i in range(1, len(portfolio.hist_prices)):
    if i % INTERVAL == 0:
        portfolio = rebalance.run(portfolio, i)
    if i % 24 == 0:
        # Append hodl total value
        df_rebalanced.append(round(np.dot(portfolio.units, portfolio.hist_prices[i]), 2))
        # Append rebalanced total value
        df_hodl.append(round(np.dot(portfolio.start_units, portfolio.hist_prices[i]), 2))


sim_results = pd.DataFrame(zip(portfolio.dates, df_hodl, df_rebalanced), columns=['date', 'hodl', 'rebalanced'])

# sim_results['date_labels'] = None
# for i in range(0, len(portfolio.dates), len(portfolio.dates)//5):
#     sim_results.loc[i, 'date_labels'] = (datetime(year=2018,month=1,day=1) + timedelta(hours=i)).strftime('%b %Y')


sim_results.to_json(SIM_RESULTS_FILE)

portfolio.summarize()
