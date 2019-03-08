This repository merges two similar repositories:
* __[crypto-simulations](https://github.com/cartercarlson/crypto-simulations)__
  * Simulates rebalancing a randomly selected basket of 5 coins 250 times and records the total value of the portfolio
    over the course of the simulation.
  * Compares overall hodl performance to rebalanced performance.
* __[transaction-log](https://github.com/cartercarlson/transaction-log)__
  * Rebalances a specific basket of coins and captures details of the transactions
  * Can be simulated or used for personal rebalancing

While the two repositories have similar purposes, they were made separately and have different code structures:
* __crypto-simulations__
  * _Code structure_: many separate lists and zips the lists together  
  * _Pros_: optimizes simulation speed for hundreds of backtests
  * _Cons_: Hard to understand code, not suitable for adding transaction documentation.
* __transaction-log__
  * _Code structure_: portfolio object, methods for portfolio class are outside the class in functions
  * _Pros_: accurate documentation of transactions, code is easier to follow
  * _Cons_: cannot scale to multiple backtests, calculations still needed for summary, outside functions for the portfolio should be a method inside the portfolio class

Once completed, the new code structure will have:
* A portfolio object summarizing performance, including a list of coin objects
* Coin objects for each coin in the portfolio, including coin performance and transactions
* A transaction object inside each coin, containing all relevant coin transactions
