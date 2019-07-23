import React, { Component } from 'react';
import ReactTable, { ReactTableDefaults } from 'react-table';
import 'react-table/react-table.css';
import summary from '../assets/summary.json';


const columns = [
  {
    Header: 'Coin',
    accessor: 'coin',
    width: 100
  },
  {
    Header: 'Current Price',
    accessor: 'price',
    width: 200,
    Cell: props => '$' + props.value.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')
  },
  {
    Header: 'Units',
    accessor: 'units',
    width: 200,
    Cell: props => props.value.toFixed(4)
  },
  {
    Header: 'Cost',
    accessor: 'cost',
    width: 200,
    Cell: props => '$' + props.value.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')
  },
  {
    Header: 'Market Value',
    accessor: 'market_val',
    width: 200,
    Cell: props => '$' + props.value.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')
  }
]


export default class Coins extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div style={{width:950}}>
        <ReactTable
          columns={columns}
          data={summary}
          defaultPageSize={summary.length}
        >

        </ReactTable>
      </div>
    );
  }
}
