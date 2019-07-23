
def run(portfolio, i):

	market_vals = portfolio.hist_prices[i] * portfolio.units
	market_val_sum = sum(market_vals)

	# We'll take the coins with the highest and lowest dollar value to
	# test our threshold
	trade_weight = min([portfolio.avg_weight - min(market_vals)/market_val_sum,
						max(market_vals)/market_val_sum - portfolio.avg_weight])

	cost = trade_weight * market_val_sum
	if cost > 20:
		portfolio.trade(side='SELL', coin_index=market_vals.argmax(), cost=cost, i=i)
		portfolio.trade(side='BUY', coin_index=market_vals.argmin(), cost=cost, i=i)
		return run(portfolio, i)
