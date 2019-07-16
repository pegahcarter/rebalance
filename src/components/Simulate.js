import React, { Component } from 'react';
import { ButtonToolbar, Button } from "react-bootstrap";


export default class Simulate extends Component {

  render() {
    return (
      <div>
        <ButtonToolbar>
          <Button variant="outline-primary">BTC</Button>
          <Button variant="outline-primary">ETH</Button>
          <Button variant="outline-primary">XRP</Button>
          <Button variant="outline-primary">LTC</Button>
          <Button variant="outline-primary">XLM</Button>
          <Button variant="outline-primary">TRX</Button>
          <Button variant="outline-primary">ADA</Button>
          <Button variant="outline-primary">DASH</Button>
        </ButtonToolbar>
        <Button variant="outline-primary" size="lg" style={{ marginTop: 50}}>Simulate</Button>
      </div>
    );
  }
}
