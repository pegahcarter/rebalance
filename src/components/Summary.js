import React, { Component } from 'react';
import ReactTable, { ReactTableDefaults } from 'react-table';
import 'react-table/react-table.css';
import summary from '../assets/summary.json';


export default class Coins extends Component {

  constructor(props) {
    super(props);
    this.state = {
      summary: summary
    }
  }

  render() {
    const { summary } = this.state;
    return (
      <div style={{width:950}}>
        <ReactTable
          data={summary}
          defaultPageSize={summary.length}
          columns={[{
            Header: 'Coin',
            accessor: 'coin',
            width: 100
          },
          {
            Header: 'Current Price',
            accessor: 'price',
            width: 200,
            Cell: props => props.value.toFixed(2)
          },
          {
            Header: 'Units',
            accessor: 'units',
            width: 200,
            Cell: props => props.value.toFixed(4)
          },
          {
            Header: 'Cost ($)',
            accessor: 'cost',
            width: 200,
            Cell: props => props.value.toFixed(2)
          },
          {
            Header: 'Market Value ($) ',
            accessor: 'market_val',
            width: 200,
            Cell: props => (
              <span style={{ backgroundColor: props.value > 0 ? '#90ee90' : '#f97976' }}>
                { props.value.toFixed(2) }
              </span>
            )
          }]}
        />
      </div>
    );
  }
}
