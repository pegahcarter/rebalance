3/4/2019

--- Order of code execution ---

1. Initialize empty portfolio class w/ no coins

2. Are tx's already recorded?
  - If yes
    - There should already be a portfolio "summary" file
    - Set portfolio equal to portfolio "summary"
  - If no
    - Is this a simulation?
      - If "yes"
        - Simulate purchase of coins on day 0
        - If we're only simulating one portfolio, add to tx's
        - If we're backtesting 100's of portfolios, don't add to tx's
      - If "no"
        - document initial purchase of coins already owned

3. Now our portfolio/coins are up to date, fetch current prices.
  - If simulation, use historical data
  - If not simulation, fetch from exchange

4. Update coin prices/market values

5. Do we need to rebalance?
  - If "yes"
    - Calculate coin quantities to trade
    - Update tx's file if needed
    - refresh portfolio class
  - If "no"
    - continue


--- Psuedocode ---

portfolio = Portfolio()

if transactions.exists():
    for tx in transactions:
        portfolio.update(tx)
else:
  if simulation:
    coins = coins
  else:
    coins = fetch_coins(exchange)

  for coin in coins:
    portfolio.add_coin(coin, simulation=False, backtesting=False)

portfolio.refresh_prices()

while portfolio.price_differences > threshold:
  portfolio.rebalance()
