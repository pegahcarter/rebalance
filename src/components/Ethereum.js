import React, { Component } from 'react';
import BigNumber from 'bignumber.js';
import web3 from "web3";
import YAML from 'yaml';
import fs from 'fs';
import HDWalletProvider from '@truffle/hdwallet-provider';



export default class Ethereum extends Component {

  render() {
    return (
      <div>
        Welcome to Ethereum
      </div>
    )
  }
}
