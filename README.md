This repository merges two similar repositories into one:
* __[crypto-simulations](https://github.com/cartercarlson/crypto-simulations)__
  * Simulates a randomly selected basket of 5 coins 250 times and records the total value of the portfolio
    over the course of the simulation.
  * Compares overall hodl performance to rebalanced performance.
* __[transaction-log](https://github.com/cartercarlson/transaction-log)__
  * Rebalances a specific basket of coins and captures details of every transaction
  * Can be simulated or used for personal rebalancing
    
While the two repositories have similar purposes, they were made separately and have different code structures.
* __crypto-simulations__ 
  * _Code_: Uses many separate lists and zips the lists together.  
  * _Pros_: Optimizes simulation speed for hundreds of backtests
  * _Cons_: Hard to understand code and is not suitable for adding transaction documentation.
* __transaction-log__
  * _C
