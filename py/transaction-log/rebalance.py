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

	portfolio.trade(cost)


	# # Sell side
	# if portfolio.coins[max_index] != 'USDT':
	# 	portfolio.binance.create_order(portfolio.coins[max_index] + '/USDT',
	# 								   'market',
	# 								   'sell',
	# 								   cost / portfolio.prices[max_index])
	#
	# # Buy side
	# if portfolio.coins[min_index] != 'USDT':
	# 	portfolio.binance.create_order(portfolio.coins[min_index] + '/USDT',
	# 								   'market',
	# 								   'buy',
	# 								   cost / portfolio.prices[min_index])
	#

	return run(portfolio, i)



if __name__ == '__main__':

	# TODO: import variables
	portfolio = Portfolio(coins, PORTFOLIO_START_VALUE)
	transactions.initialize(portfolio)
	run()
