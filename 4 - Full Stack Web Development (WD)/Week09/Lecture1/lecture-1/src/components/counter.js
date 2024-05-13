import React, { useState } from 'react';

function Counter () {
    let [count, setCount] = useState(0);

    function inc () {
        setCount(count + 1);
    }

    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={inc} >Increment</button>
        </div>
    )
}

export default Counter;


