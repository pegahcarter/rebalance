import React from 'react';
import results from '../assets/sim_results.json';
import { VictoryChart, VictoryTheme, VictoryLine} from 'victory';

// var data = JSON.stringify(results);
// console.log(data);

const Graph = props => {
  return (
    <div>
      <VictoryChart
        theme={VictoryTheme.material}
      >
        data={{results}}
        x="date"
        y="hodl"
      </VictoryChart>
    </div>
  )
}

export default Graph;
