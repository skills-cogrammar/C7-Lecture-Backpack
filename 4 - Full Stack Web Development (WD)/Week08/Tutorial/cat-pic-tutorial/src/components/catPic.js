// Create an img component which displays a random image of a cat
import React from 'react';

function CatPic (prop) {
    return (
        <img alt = "Imagine a cat here" src = {prop.url} />
    )
}

export default CatPic;