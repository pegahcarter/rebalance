import React, {Component} from 'react';
import {VictoryChart, VictoryLine, VictoryVoronoiContainer, VictoryTooltip, VictoryLegend} from 'victory';
import results from '../assets/sim_results.json';


export default class Chart extends Component {

  render() {

    var hodl = []
    var rebalanced = []
    for (var i in results.hodl) {
      let current_date = new Date(results.date[i]);
      hodl.push({
        y: results.hodl[i]
      });
      rebalanced.push({
        y: results.rebalanced[i]
      });
    }

    return (
      <div style={{ display: 'inline-block', width: '35%', float: 'right' }}>
        <VictoryChart
          height={250}
          animate={{ duration: 1000 }}
          minDomain={{ y: 0}}
          containerComponent={
            <VictoryVoronoiContainer
              voronoiDimension='x'
              labels={(d) => `$${d.y}`}
              labelComponent={
                <VictoryTooltip
                  cornerRadius={0}
                  flyoutStyle={{ fill: 'white' }}
                />
              }
            />
          }
        >
          <VictoryLegend x={75}
            orientation='horizontal'
            gutter={20}
            style={{ border: { stroke: 'black' }}}
            data={[
              { name: 'HODL', symbol: { fill: 'red' } },
              { name: 'Rebalanced', symbol: { fill: 'blue' } }
            ]}
          />
          <VictoryLine
            data={hodl}
            style={{
              data: {
                stroke: 'red'
              },
              labels: { fill: 'red' }
            }}
          />
          <VictoryLine
            data={rebalanced}
            style={{
              data: {
                stroke: 'blue'
              },
              labels: { fill: 'blue' }
            }}
          />
        </VictoryChart>
      </div>
    );
  }
}
