import React, { Component } from 'react';
// import ReactDOM from 'react-dom';
import Simulate from './components/Simulate';
import Summary from './components/Summary';
import Transactions from './components/Transactions';
import Chart from './components/Chart';
// import Ethereum from './components/Ethereum';


export default class App extends Component {
  constructor(props){
    super(props);
    this.state = {

    }
    this.submitSimulate = this.submitSimulate.bind(this);
  }

  render() {
    return (
      <React.Fragment>
        <div style={{marginLeft: 100, marginTop: 150}}>
          <Summary />
          <Chart />
        </div>
        <div style={{margin: 100}}>
          <Transactions />
        </div>
        <Simulate submit={this.submitSimulate}/>
      </React.Fragment>
    );
  }

  submitSimulate() {
    console.log('submit called');
  }

}
