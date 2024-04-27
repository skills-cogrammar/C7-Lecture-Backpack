import React from "react";

function Welcome (prop) {
    return (
        <div>
            <p> This is our lecture notes. There are {prop.number} students in this lecture.</p>
        </div>
    );
}

export default Welcome;