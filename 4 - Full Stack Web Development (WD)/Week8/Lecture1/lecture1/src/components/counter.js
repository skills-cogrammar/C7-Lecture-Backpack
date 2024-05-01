import React from 'react';
import { useState } from 'react';
import Message from "./message"


function Counter () {
    let [count, setCount] = useState(0);

    function inc () {
        setCount(count + 1);
        console.log(count);
    }

    function dec () {
        setCount(count - 1);
        console.log(count);
    }

    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={inc} >Increment</button>
            <button onClick={dec} >Decrement</button>
            <Message></Message>
        </div>
    )
}

export default Counter;