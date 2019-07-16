import React, { Component } from 'react';
import ReactTable from 'react-table';
import 'react-table/react-table.css';
import transactions from '../assets/transactions.json';

const columns = [
  {
    Header: 'Trade ID',
    accessor: 'id',
    width: 100
  },
  {
    Header: 'Date',
    accessor: 'date'
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
    accessor: 'units'
  },
  {
    Header: 'Cost',
    accessor: 'cost'
  },
  {
    Header: 'Previous Units',
    accessor: 'prev_units'
  },
  {
    Header: 'Cumulative Units',
    accessor: 'cum_units'
  },
  {
    Header: 'Previous Cost',
    accessor: 'prev_cost'
  },
  {
    Header: 'Cumulative Cost',
    accessor: 'cum_cost'
  },
  {
    Header: 'Fees',
    accessor: 'fees'
  }
]


export default class Transactions extends Component {

  render() {
    return (
      <div style={{ marginTop: '10%'}}>
        <ReactTable
          columns={columns}
          data={transactions}
        >
        </ReactTable>
      </div>
    );
  }
}
