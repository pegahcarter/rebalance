from portfolio import Portfolio
from coin import Coin

simulated = False
backtest = False
coins = ['BTC', 'ETH', 'XRP', 'LTC']


def run(portfolio):

    # TODO: what do we need to update?
    portfolio.refresh()

    avg_weight = 1.0/len(portfolio.coins)

    # TODO: should there be other functions to figure out trade weight?
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
