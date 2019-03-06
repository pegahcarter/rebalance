from portfolio import Portfolio
from coin import Coin

simulated = False
backtest = False
coins = ['BTC', 'ETH', 'XRP', 'LTC']


def run(portfolio):

    portfolio.refresh() # TODO
    avg_weight = 1.0/len(portfolio.coins)
    trade_weight = ???
    d_amt = trade_weight * portfolio.market_val
    if d_amt < 20:
        print('Trade value is less than $20.  Rebalance complete!')
        return
    else:
        # Execute trade

        # Run rebalancer again
        return run(portfolio)







if __name__ == "__main__":


    portfolio = Portfolio(simulated, backtest, coins)
    run(portfolio)
