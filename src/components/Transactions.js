import React, { Component } from 'react';
import MaterialTable from 'material-table';

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
        <MaterialTable
          data={transactions}
          title='Transactions'
          showPagination={false}
          options={{
            pageSize: 10,
          }}
          columns={[
            {
              title: 'Trade ID',
              field: 'id',
              width: 100
            },
            {
              title: 'Date',
              field: 'date',
              type: 'date'
            },
            {
              title: 'Coin',
              field: 'coin'
            },
            {
              title: 'Side',
              field: 'side'
            },
            {
              title: 'Units',
              field: 'units',
            },
            {
              title: 'Cost',
              field: 'cost',
              type: 'currency'
            },
            {
              title: 'Previous Units',
              field: 'prev_units',
            },
            {
              title: 'Cumulative Units',
              field: 'cum_units',
            },
            {
              title: 'Fees',
              field: 'fees',
              type: 'currency'
          }]}
        />
    );
  }
}
