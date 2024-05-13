// Create a button which displays a new random image of a cat

import React from 'react';

function CatButton (prop) {
    return <button onClick = {prop.changeURL} > Generate new cat! </button>
}

export default CatButton;