from portfolio import Portfolio
import transactions


def run(portfolio, i=None):

	avg_weight = 1.0/len(portfolio.coins)
	# We'll take the coins with the highest and lowest dollar value to
	# test our threshold
	market_val = sum(portfolio.market_vals)
	trade_weight = min([avg_weight - min(portfolio.market_vals)/market_val,
						max(portfolio.market_vals)/market_val - avg_weight])

	cost = trade_weight * market_val
	if cost < 20:
		print('Trade value is less than $20.  Rebalance complete.')
		return
	else:
		portfolio.trade(cost)
		return run(portfolio, i)



if __name__ == '__main__':

	# TODO: import variables
	portfolio = Portfolio(coins, PORTFOLIO_START_VALUE)
	run()
	# TODO: figure out where to save
