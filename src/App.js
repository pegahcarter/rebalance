import React, { Component } from 'react';
// import ReactDOM from 'react-dom';

import Coins from './components/Coins';
import Simulate from './components/Simulate';
import Transactions from './components/Transactions';
import Graph from './components/Graph';


export default class App extends Component {
  constructor(props){
    super(props);
    this.state = {

    }
    this.submitSimulate = this.submitSimulate.bind(this);
  }

  render() {
    return (
      <div style={{ marginLeft: '10%', marginRight: '10%' , marginTop: 100}}>
        <div>
          <Coins />
          <Graph />
          <Simulate submit={this.submitSimulate} />
        </div>
        <Transactions />
      </div>
    );
  }

  submitSimulate() {
    console.log('submit called');
  }

}
