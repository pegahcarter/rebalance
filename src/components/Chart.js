import React, {Component} from 'react';
import {VictoryChart, VictoryLine} from 'victory';
import results from '../assets/sim_results.json';

// data={[
//   { x: 1, y: 2 },
//   { x: 2, y: 4},
//   { x: 3, y: 8}
// ]}

var data = []
for (var i in results.hodl) {
  data.push({
    y: results.hodl[i]
  });
}

console.log(data);



export default class Chart extends Component {

  render() {
    return (
      <div>
        <VictoryChart>
          <VictoryLine
            data={data}
          />
        </VictoryChart>
      </div>
    );
  }
}
