import React, { Component } from 'react';
// import ReactDOM from 'react-dom';

import Coins from './components/Coins';
import Simulate from './components/Simulate';
import Transactions from './components/Transactions';
// import Graph from './components/Graph';


class App extends Component {
  render() {
    return (
      <div style={{ marginLeft: '10%', marginRight: '10%' , marginTop: '5%'}}>
        <div>
          <Coins />
          <Simulate />
        </div>
        <Transactions />
      </div>
    );
  }
}

export default App;
