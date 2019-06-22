# File used to create simulate code
from py.portfolio import Portfolio
from py.variables import INTERVAL, COINS, PORTFOLIO_START_VALUE, TRANSACTIONS_FILE

portfolio = Portfolio(COINS, PORTFOLIO_START_VALUE)
portfolio.transactions.transactions




# hr_totals = [PORTFOLIO_START_VALUE]
# transactions.initialize(TRANSACTIONS_FILE, PORTFOLIO_START_VALUE, coins)
# simulations = pd.DataFrame(columns=['timestamp', 'hodl', 'rebalanced'])
#
# for index, row in prices.iterrows():
#     if index % INTERVAL == 0:
#         portfolio = rebalance.run(coins)
#
#     # Append hodl total value
#
#     # Append rebalanced total value
