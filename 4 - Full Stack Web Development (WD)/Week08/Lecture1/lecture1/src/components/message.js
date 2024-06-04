import React from 'react';
import { useUserName } from './userContext.js';

function Message () {
    let name = useUserName();
    return (
        <div>
            <p> Welcome to the Counter App, {name}. <br></br>
            Please let us know if you have any questions.</p>
        </div>
    )
}

export default Message;