import React, {Component} from 'react';
import {Line} from 'react-chartjs-2';
import results from '../assets/sim_results.json';


export default class Chart extends Component {

  constructor(props) {
    super(props);
    this.state = {
      chartData: {
        labels: [],
        datasets: [{
          label: 'Rebalanced',
          data: results.rebalanced
        }]
      }
    }
  }

  render() {
    return (
      <div className='chart'>
        <Line
          data={this.state.chartData}
          options={{
            title: {
              display: true,
              text: 'Rebalanced vs. Non-Rebalanced',
              fontSize:25
            }
          }}
        />
      </div>
    );
  }
}
