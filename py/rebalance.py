from portfolio import Portfolio
from coin import Coin

simulated = False
backtest = False
coins = ['BTC', 'ETH', 'XRP', 'LTC']


def run(portfolio):

    portfolio.refresh() # TODO







if __name__ == "__main__":


    portfolio = Portfolio(simulated, backtest, coins)
    run(portfolio)
