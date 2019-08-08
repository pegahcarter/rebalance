import React, { Component } from 'react';
import { Modal, Button } from 'react-bootstrap';
import { PythonShell } from 'python-shell';
import prices from '../assets/prices.json';
delete prices.date;


export default class Simulate extends Component {
  constructor(){
    super()
    let coinDict = {}
    Object.keys(prices).forEach((coin) => {
      coinDict[coin] = false;
    })
    this.state = {
      showModal: false,
      simCoins: [],
      coins: coinDict,
    }
    this.toggleModal = this.toggleModal.bind(this);
    this.submitButton = this.submitButton.bind(this);
    this.updateCoinState = this.updateCoinState.bind(this);
    this.resetCoinState = this.resetCoinState.bind(this);
  }

  render() {

    return (
      <div>
        <Button onClick={this.toggleModal}>Simulate</Button>
        <Modal show={this.state.showModal} onHide={this.toggleModal}>
          <Modal.Header closeButton>
            <Modal.Title>Select coins to simulate</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <div style={{display: 'inline-block'}}>
              {
                Object.keys(this.state.coins).map((coin) => {
                  return (
                    <Button
                      key={coin}
                      variant='outline-primary'
                      id={coin}
                      onClick={this.updateCoinState}
                      style={{margin: '5%', width: '15%'}}
                    >
                      {coin}
                    </Button>
                  );
                })
              }
            </div>
          </Modal.Body>
          <Modal.Footer>
            <Button variant='secondary' onClick={this.toggleModal}>
              Cancel
            </Button>
            <Button variant='primary' onClick={this.submitButton}>
              Run
            </Button>
          </Modal.Footer>
        </Modal>
      </div>
    );
  }

  toggleModal() {
    this.state.showModal ? this.setState({showModal: false}) : this.setState({showModal: true});
    this.resetCoinState();
  }

  submitButton() {
    this.toggleModal();
    let simCoins = []
    Object.keys(this.state.coins).forEach((coin) => {
      if (this.state.coins[coin] === true) { simCoins.push(coin) }
    });
    let options: {
      pythonPath: 'C:/Users/carter/AppData/Local/Programs/Python/Python37-32',
      scriptPath: 'C:/Users/carter/AppData/Local/Programs/Python/Python37-32/Lib/site-packages',
      args: [simCoins]
    }
    PythonShell.run('C:/Users/carter/Documents/crypto/rebalance/py/simulate.py', options, function(err, results) {
      if (err) throw err;
    });
  }

  updateCoinState(props) {
    let coin = props.target.id;
    this.state.coins[coin] ? props.target.className = 'btn btn-outline-primary' : props.target.className = 'btn btn-primary';
    const isSelected = {...this.state.coins};
    isSelected[coin] = !isSelected[coin];
    this.setState({ coins: isSelected });
  }

  resetCoinState() {
    const isSelected = {...this.state.coins};
    Object.keys(isSelected).forEach((coin) => {
      isSelected[coin] = false;
      this.setState({ coins: isSelected });
    });
  }

}
