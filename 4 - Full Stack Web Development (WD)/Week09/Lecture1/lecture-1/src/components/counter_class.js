import React, { Component } from "react"; 
  
class Counter extends Component { 
    constructor() { 
        super(); 
        this.state = { 
            count: 0 
        }; 
        this.inc = this.inc.bind(this); 
        this.dec = this.dec.bind(this); 
    } 
  
    inc () {
        this.setState({ count: this.state.count + 1 });
        console.log(this.state.count);
    }

    dec () {
        this.setState({ count: this.state.count - 1 });
        console.log(this.state.count);
    }
  
    render() { 
        return (
            <div>
                <p>Count: {this.state.count}</p>
                <button onClick={this.inc} >Increment</button>
                <button onClick={this.dec} >Decrement</button>
            </div>
        ) 
    } 
} 
  
export default Counter; 