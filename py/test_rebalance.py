from py.portfolio import Portfolio
import numpy as np
import json

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

avg_weight = 1.0/len(coins)
portfolio.coins

# portfolio.update_coins(50)
# market_vals = np.array(list(map(lambda x: x['market_val'], portfolio.coins.values())))
# trade_weight = min([
#     avg_weight - min(market_vals)/sum(market_vals),
#     max(market_vals)/sum(market_vals) - avg_weight
# ])
# trade_weight * sum(market_vals)
#
# sell_coin = coins[market_vals.argmax()]
# buy_coin = coins[market_vals.argmin()]
# cost = trade_weight * market_vals.sum()
# portfolio.trade(cost=cost, i=50, sell=sell_coin, buy=buy_coin)
# portfolio.transactions

for i in range(len(portfolio.prices)):
    portfolio.update_coins(i)
    market_vals = np.array(list(map(lambda x: x['market_val'], portfolio.coins.values())))
    trade_weight = min([
        avg_weight - min(market_vals)/sum(market_vals),
        max(market_vals)/sum(market_vals) - avg_weight
    ])

    cost = trade_weight * sum(market_vals)
    if cost < 20:
        continue

    coin_to_sell = coins[market_vals.argmax()]
    coin_to_buy = coins[market_vals.argmin()]

    portfolio.trade(cost=cost, i=i, sell=coin_to_sell, buy=coin_to_buy)

import pandas as pd
test = pd.Series(portfolio.transactions)
test.to_json('transactions.json', orient='records')
