import React, { Component } from 'react';
import MaterialTable from 'material-table';

import summary from '../assets/summary.json';


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
      <div style={{width: '40%', display: 'inline-block'}}>
        <MaterialTable
          data={summary}
          title='Summary'
          showPagination={false}
          options={{
            search: false,
            paging: false
          }}
          columns={[
            {
              title: 'Coin',
              field: 'coin',
              'width': '20%'
            },
            {
              title: 'Price',
              field: 'price',
              width: '10%',
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
              width: '15%',
              type: 'currency'
            }
          ]}
        />
      </div>
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
