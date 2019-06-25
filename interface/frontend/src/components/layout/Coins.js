import React from 'react';
import ReactTable from 'react-table';
import 'react-table/react-table.css';

const columns = []

export default class Coins extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      coin: 'BTC'
    };
  }

  render() {
    return (
      <div>Coins</div>
    );
  }
}
