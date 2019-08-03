import React, { Component, useState } from 'react';
// import { ToggleButtonGroup, ButtonToolbar, ToggleButton, Button } from "react-bootstrap";
import { Modal, Button } from 'react-bootstrap';


export default class Simulate extends Component {
  constructor(){
    super()
    this.state = {
      showModal: false
    }
    this.toggleModal = this.toggleModal.bind(this);
  }

  render() {
    return (
      <div>
        <Button onClick={this.toggleModal}>Simulate</Button>
        <Modal show={this.state.showModal} onHide={this.toggleModal}>
          <Modal.Header closeButton>
            <Modal.Title>Select coins to simulate</Modal.Title>
          </Modal.Header>
          <Modal.Body></Modal.Body>
          <Modal.Footer>
            <Button variant='secondary' onClick={this.toggleModal}>
              Cancel
            </Button>
            <Button variant='primary' onClick={this.toggleModal}>
              Run
            </Button>
          </Modal.Footer>
        </Modal>
      </div>
    );
  }

  toggleModal() {
    this.state.showModal === true ? this.setState({showModal: false}) : this.setState({showModal: true});
  }

}


// this.showModal === true ? this.setState({showModal: true}) : this.setState({showModal: false});
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
