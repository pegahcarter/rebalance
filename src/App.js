import React, { Component } from 'react';
// import ReactDOM from 'react-dom';

import Coins from './components/Coins';
import Transactions from './components/Transactions';
// import Graph from './components/Graph';

import { ButtonToolbar, Button } from "react-bootstrap";



class App extends Component {
  render() {
    return (
      <div style={{ marginLeft: '10%', marginRight: '10%' , marginTop: '5%'}}>
        <Coins />
        <div style={{ }}>
          <ButtonToolbar>
            <Button variant="outline-primary">BTC</Button>
            <Button variant="outline-primary">ETH</Button>
            <Button variant="outline-primary">XRP</Button>
            <Button variant="outline-primary">LTC</Button>
            <Button variant="outline-primary">XLM</Button>
            <Button variant="outline-primary">TRX</Button>
            <Button variant="outline-primary">ADA</Button>
            <Button variant="outline-primary">DASH</Button>
          </ButtonToolbar>
          <Button variant="outline-primary" size="lg" style={{ marginTop: 50}}>Simulate</Button>
        </div>
        <Transactions />
      </div>
    );
  }
}

export default App;
