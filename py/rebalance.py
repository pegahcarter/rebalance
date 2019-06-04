import models
import transactions
import exchange


def run(coins=None):

	portfolio = models.Portfolio(coins)
	avg_weight = 1.0/len(portfolio.coins)
	# We'll take the coins with the highest and lowest dollar value to
	# test our threshold
	trade_weight = min([avg_weight - min(portfolio.usd_values)/sum(portfolio.usd_values),
						max(portfolio.usd_values)/sum(portfolio.usd_values) - avg_weight])

	trade_usd_value = trade_weight * sum(portfolio.usd_values)
	if trade_usd_value < 20:
		print('Trade value is less than $20.  Rebalance complete.')
		return

	min_index = portfolio.usd_values.argmin()
	max_index = portfolio.usd_values.argmax()
	print('\nValue of trade: ${0:.2f}'.format(trade_usd_value))
	print('Sell: {}'.format(portfolio.coins[max_index]))
	print('Buy: {}'.format(portfolio.coins[min_index]))
	# Sell side
	if portfolio.coins[max_index] != 'USDT':
		portfolio.binance.create_order(portfolio.coins[max_index] + '/USDT',
									   'market',
									   'sell',
									   trade_usd_value / portfolio.prices[max_index])

	# Buy side
	if portfolio.coins[min_index] != 'USDT':
		portfolio.binance.create_order(portfolio.coins[min_index] + '/USDT',
									   'market',
									   'buy',
									   trade_usd_value / portfolio.prices[min_index])

	return run(coins)



if __name__ == '__main__':

	transactions.initialize()
	run()
