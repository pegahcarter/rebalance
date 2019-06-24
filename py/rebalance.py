

def run(portfolio, i=None):

	if i:
		portfolio.date = portfolio.dates[i]
		portfolio.prices = portfolio.hist_prices[i]
		portfolio.market_vals = portfolio.prices * portfolio.units

	avg_weight = 1.0/len(portfolio.coins)
	# We'll take the coins with the highest and lowest dollar value to
	# test our threshold
	market_val = sum(portfolio.market_vals)
	trade_weight = min([avg_weight - min(portfolio.market_vals)/market_val,
						max(portfolio.market_vals)/market_val - avg_weight])

	cost = trade_weight * market_val
	if cost > 20:
		portfolio.trade(cost)
		return run(portfolio, i)
