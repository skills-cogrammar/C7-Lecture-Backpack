import React from 'react';
import './styledButton.css';

function StyledButton (prop) {
   let styleSheet = {
        backgroundColor: "red",
        borderColor: "green",
        fontFamily: "Georgia",
        color: "white"
    };


    return (
        <button style = {styleSheet} onClick = {prop.func}> Button </button>
    )
}

export default StyledButton;