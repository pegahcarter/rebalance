import React, { Component } from 'react';
import './App.css';
import ReactTable from 'react-table';
import 'react-table/react-table.css';
import Coins from './components/Coins';
import Transactions from './components/Transactions';
import Graph from './components/Graph';


class App extends Component {
  render() {
    return (
      <div>
        <Coins />
        <Transactions />
      </div>
    );
  }
}

export default App;
