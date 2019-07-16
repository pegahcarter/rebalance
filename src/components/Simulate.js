import React, { Component } from 'react';
import { ToggleButtonGroup, ButtonToolbar, ToggleButton, Button } from "react-bootstrap";


export default class Simulate extends Component {

  render() {
    return (
      <div>
        <div class="d-flex justify-content-end">
          <ButtonToolbar>
            <ToggleButtonGroup type="checkbox" defaultValue={[1,2,3,4]}>
              <ToggleButton variant="outline-dark" style={{width:100, margin:10}} value={1}>BTC</ToggleButton>
              <ToggleButton variant="outline-dark" style={{width:100, margin:10}} value={2}>ETH</ToggleButton>
              <ToggleButton variant="outline-dark" style={{width:100, margin:10}} value={3}>XRP</ToggleButton>
              <ToggleButton variant="outline-dark" style={{width:100, margin:10}} value={4}>LTC</ToggleButton>
            </ToggleButtonGroup>
          </ButtonToolbar>
        </div>
        <div class="d-flex justify-content-end">
          <ButtonToolbar>
            <ToggleButtonGroup type="checkbox" defaultValue={5}>
              <ToggleButton variant="outline-dark" style={{width:100, margin:10}} value={5}>XLM</ToggleButton>
              <ToggleButton variant="outline-dark" style={{width:100, margin:10}} value={6}>TRX</ToggleButton>
              <ToggleButton variant="outline-dark" style={{width:100, margin:10}} value={7}>ADA</ToggleButton>
              <ToggleButton variant="outline-dark" style={{width:100, margin:10}} value={8}>DASH</ToggleButton>
            </ToggleButtonGroup>
          </ButtonToolbar>
        </div>
        <div class="d-flex justify-content-end">
          <Button variant="primary" type="submit" style={{ marginTop: 50, width: 200}}>Simulate</Button>
        </div>
      </div>
    );
  }
}
