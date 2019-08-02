import React, { Component } from 'react';
// import ReactDOM from 'react-dom';

import Summary from './components/Summary';
import Simulate from './components/Simulate';
import Transactions from './components/Transactions';
import Chart from './components/Chart';



export default class App extends Component {
  constructor(props){
    super(props);
    this.state = {

    }
    this.submitSimulate = this.submitSimulate.bind(this);
  }

  render() {
    return (
      <div style={{ marginLeft: '5%', marginRight: '5%' , marginTop: '3%', fontSize: 14}}>
        <Simulate />
      </div>
    );
  }

  submitSimulate() {
    console.log('submit called');
  }

}

// <div style={{display: 'inline-block', width: '100%'}}>
//   <Summary />
//   <Chart />
// </div>
// <Transactions />
// <Simulate submit={this.submitSimulate} />
