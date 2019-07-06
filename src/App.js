import React, { Component } from 'react';
import ReactDOM from 'react-dom';

import Coins from './components/Coins';
import Transactions from './components/Transactions';
import Graph from './components/Graph';


class App extends Component {
  render() {
    return (
      <Transactions />
    );
  }
}

export default App;
