import React, { Component } from 'react';
import ReactTable from 'react-table';
import 'react-table/react-table.css';
import transactions from '../assets/transactions.json';


export default class Transactions extends Component {

  constructor(props) {
    super(props);
    this.state = {
      transactions: transactions
    }
  }

  render() {
    const { transactions } = this.state;
    return (
      <div style={{ marginTop: 100}}>
        <ReactTable
          data={transactions}
          className="-striped -highlight"
          columns={[{
              Header: 'Trade ID',
              accessor: 'id',
              width: 100
            },
            {
              Header: 'Date',
              accessor: 'date',
            },
            {
              Header: 'Coin',
              accessor: 'coin'
            },
            {
              Header: 'Side',
              accessor: 'side'
            },
            {
              Header: 'Units',
              accessor: 'units',
              Cell: props => props.value.toFixed(4)
            },
            {
              Header: 'Cost ($)',
              accessor: 'cost',
              Cell: props => props.value.toFixed(2)
            },
            {
              Header: 'Previous Units',
              accessor: 'prev_units',
              Cell: props => props.value.toFixed(4)
            },
            {
              Header: 'Cumulative Units',
              accessor: 'cum_units',
              Cell: props => props.value.toFixed(4)
            },
            {
              Header: 'Previous Cost ($)',
              accessor: 'prev_cost',
              Cell: props => props.value.toFixed(2)
            },
            {
              Header: 'Cumulative Cost ($)',
              accessor: 'cum_cost',
              Cell: props => props.value.toFixed(2)
            },
            {
              Header: 'Fees ($)',
              accessor: 'fees',
              Cell: props => props.value.toFixed(2)
          }]}
        />
      </div>
    );
  }
}
