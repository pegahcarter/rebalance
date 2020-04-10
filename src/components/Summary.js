import React, { Component } from 'react';
import summary from '../assets/summary.json';


// https://material-table.com/#/docs/features/remote-data
import MaterialTable from 'material-table';

export default class Summary extends Component {

  constructor(props) {
    super(props);
    this.state = {
      summary: summary
    }
  }

  render() {
    const { summary } = this.state;
    return (
      <MaterialTable
        title='Summary'
        columns={[
          {
            title: 'Coin',
            field: 'coin',
          },
          {
            title: 'Current Price',
            field: 'price',
            type: 'currency'
          },
          {
            title: 'Units',
            field: 'units',
            width: '5%',
          },
          {
            title: 'Market Value',
            field: 'market_val',
            width: '5%',
            type: 'currency'
          }
        ]}
        data={summary}
        showPagination={false}
        options={{
          search: false,
          paging: false
        }}
        style={{width: 600, display: 'inline-block'}}
      />
    )
  }
}




// NOTE: old version
// export default class Coins extends Component {
//
//   constructor(props) {
//     super(props);
//     this.state = {
//       summary: summary
//     }
//   }
//
//   render() {
//     const { summary } = this.state;
//     return (
//       <div style={{width:'40%', display: 'inline-block'}}>
//         <ReactTable
//           data={summary}
//           defaultPageSize={summary.length}
//           columns={[{
//             Header: 'Coin',
//             accessor: 'coin',
//             width: '5%'
//           },
//           {
//             Header: 'Current Price',
//             accessor: 'price',
//             width: '5%',
//             Cell: props => props.value.toFixed(2)
//           },
//           {
//             Header: 'Units',
//             accessor: 'units',
//             width: '5%',
//             Cell: props => props.value.toFixed(4)
//           },
//           {
//             Header: 'Market Value ($) ',
//             accessor: 'market_val',
//             width: '5%',
//             Cell: props => props.value.toFixed(2)
//           }]}
//         />
//       </div>
//     );
//   }
// }



// Sort of working code to color cells green
// Cell: props => (
//   <span style={{ backgroundColor: props.value > 0 ? '#90ee90' : '#f97976' }}>
//     { props.value.toFixed(2) }
//   </span>
// )
