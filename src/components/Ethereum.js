import React, { Component } from 'react';
import BigNumber from 'bignumber.js';
import web3 from "web3";
import YAML from 'yamljs';
import HDWalletProvider from '@truffle/hdwallet-provider';


// const file = fs.readFileSync('../assets/config.yaml', 'utf8')
const env = YAML.load('../assets/config.yaml');

const PUBLIC_KEY = env['addresses']['demo']['PUBLIC_KEY']
const PRIVATE_KEY = env['addresses']['demo']['PRIVATE_KEY']
const INFURA_URL = env['INFURA']['kovan']['HTTPS'] + env['INFURA']['ID']

let provider = new HDWalletProvider(PRIVATE_KEY, INFURA_URL);


export default class Ethereum extends Component {

  render() {
    return (
      <div>
        Hey there
      </div>
    )
  }
}
