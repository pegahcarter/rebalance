from py.portfolio import Portfolio

simulated = True
coins = ['BTC', 'ETH', 'XRP', 'LTC']
fee_rate = 0.00075
slippage_rate = 0.01

portfolio = Portfolio(
    simulated=simulated,
    coins=coins,
    fee_rate=fee_rate,
    slippage_rate=slippage_rate
)

portfolio.coins
portfolio.update_coins()
portfolio.coins['BTC']
portfolio.transactions
