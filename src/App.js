import React, { Component } from 'react';
// import ReactDOM from 'react-dom';

import Summary from './components/Summary';
import Simulate from './components/Simulate';
import Transactions from './components/Transactions';
import Chart from './components/Chart';

// <div>
//   <Summary />
//   <Simulate submit={this.submitSimulate} />
// </div>
// <Transactions />

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
        <Chart />
      </div>
    );
  }

  submitSimulate() {
    console.log('submit called');
  }

}
