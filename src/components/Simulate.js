import React, { Component, useState } from 'react';
import { ToggleButtonGroup, ButtonToolbar, ToggleButton } from "react-bootstrap";
import { Modal, Form, Button } from 'react-bootstrap';


export default class Simulate extends Component {
  constructor(){
    super()
    this.state = {
      showModal: false,
      coins: {
        BTC: false,
        ETH: false
      }
    }
    this.toggleModal = this.toggleModal.bind(this);
    this.submitButton = this.submitButton.bind(this);
    this.changeColor = this.changeColor.bind(this);
    this.updateCoinState = this.updateCoinState.bind(this);
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
            <button id='BTC' className='btn btn-outline-primary' onClick={this.changeColor}>BTC</button>
            <button id='ETH' className='btn btn-outline-primary' onClick={this.changeColor}>ETH</button>
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
  }

  submitButton(props) {
    this.toggleModal();
    // TODO: update each coin state to false
  }

  changeColor(props) {
    let coin = props.target.id;
    this.state.coins[coin] ? props.target.className = 'btn btn-outline-primary' : props.target.className = 'btn btn-primary';
    this.updateCoinState(coin);
  }

  updateCoinState(coin) {
    const isSelected = {...this.state.coins};
    isSelected[coin] = !isSelected[coin];
    this.setState({ coins: isSelected })
  }

}


// <div className="d-flex justify-content-end">
//   <ButtonToolbar>
//     <ToggleButtonGroup type="checkbox" defaultValue={[1,2,3,4]}>
//       <ToggleButton variant="outline-dark" style={{width:100, margin:10}} value={1}>BTC</ToggleButton>
//       <ToggleButton variant="outline-dark" style={{width:100, margin:10}} value={2}>ETH</ToggleButton>
//       <ToggleButton variant="outline-dark" style={{width:100, margin:10}} value={3}>XRP</ToggleButton>
//       <ToggleButton variant="outline-dark" style={{width:100, margin:10}} value={4}>LTC</ToggleButton>
//     </ToggleButtonGroup>
//   </ButtonToolbar>
// </div>
// <div className="d-flex justify-content-end">
//   <ButtonToolbar>
//     <ToggleButtonGroup type="checkbox" defaultValue={5}>
//       <ToggleButton variant="outline-dark" style={{width:100, margin:10}} value={5}>XLM</ToggleButton>
//       <ToggleButton variant="outline-dark" style={{width:100, margin:10}} value={6}>TRX</ToggleButton>
//       <ToggleButton variant="outline-dark" style={{width:100, margin:10}} value={7}>ADA</ToggleButton>
//       <ToggleButton variant="outline-dark" style={{width:100, margin:10}} value={8}>DASH</ToggleButton>
//     </ToggleButtonGroup>
//   </ButtonToolbar>
// </div>
// <div className="d-flex justify-content-end">
//   <Button variant="primary" type="submit" style={{ marginTop: 50, width: 200}} onClick={() => {this.props.submit()}}>Simulate</Button>
// </div>
