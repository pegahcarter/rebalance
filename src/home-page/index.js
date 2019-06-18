import React from 'react';
import Coins from './Coins';
import Transactions from './Transactions';

const Homepage = () => {
  return (
    <div>
      <div id="overview">
        <Coins />
        <Graph />
      </div>
      <Transactions />
    </div>
  )
}

export default Homepage;
