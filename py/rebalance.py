import numpy as np

def run(portfolio):

	market_vals = portfolio.prices * portfolio.units
	market_val_sum = sum(market_vals)

	# We'll take the coins with the highest and lowest dollar value to
	# test our threshold
	trade_weight = min([portfolio.avg_weight - min(market_vals)/market_val_sum,
						max(market_vals)/market_val_sum - portfolio.avg_weight])

	cost = trade_weight * market_val_sum
	if cost > 20:
		data = [['sell', market_vals.argmax()], ['buy', market_vals.argmin()]]
		portfolio.trade(cost, data)
		return run(portfolio)
