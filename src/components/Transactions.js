import React from 'react';
import ReactTable from 'react-table';
import 'react-table/react-table.css';

const columns = []

export default class Transactions extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      tx_count: 1
    };
  }

  render() {
    return (
      <div>Transactions</div>
    )
  }
}
