from py.portfolio import Portfolio
import numpy as np

simulated = True
coins = ['BTC', 'ETH', 'XRP', 'LTC']
fee_rate = 0.00075
slippage_rate = 0.005

portfolio = Portfolio(
    simulated=simulated,
    coins=coins,
    fee_rate=fee_rate,
    slippage_rate=slippage_rate
)

avg_weight = 1.0/len(portfolio.coins)

for i in range(len(portfolio.prices)):
    portfolio.update_coins(i)
    market_vals = np.array(list(map(lambda x: x['market_val'], portfolio.coins)))
    print(market_vals)
    trade_weight = min([
        avg_weight - min(market_vals)/sum(market_vals),
        max(market_vals)/sum(market_vals) - avg_weight
    ])

    d_val = trade_weight * sum(market_vals)
    if d_val < 20:
        continue

    coin_to_sell = portfolio.coins[market_vals.argmax()]
    coin_to_buy = portfolio.coins[market_vals.argmin()]

    portfolio.trade(d_val=d_val, i=i, sell=coin_to_sell, buy=coin_to_buy)
