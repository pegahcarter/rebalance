import pandas as pd
# from rebalance import Rebalance
from portfolio import Portfolio

coins = ['BTC', 'ETH', 'XRP', 'LTC']
prices = pd.read_csv('data/historical/prices.csv')

param = {
    'simulated': True,
    'coins': coins,
    'fee_rate': 0.00075,
    'slippage_rate': 0.005,
    'start_amt': 1000,
    'prices': prices.loc[:, ['timestamp'] + coins]
}

if __name__ == '__main__':
    portfolio = Portfolio(**param)
    # Rebalance(portfolio)
    # portfolio.save()
