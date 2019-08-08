var nj = require('numjs');
import prices from '../assets/prices.json';

class Portfolio {
  constructor(coins) {
    this.tx_count = 0;
    this.FEE_RATE = 0.00075;
    this.PORTFOLIO_START_VALUE = 5000;
    this.avg_weight = 1.0/coins.length;

  }
}
