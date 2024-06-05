import { useState } from "react";

function useInput(initialValue) {
    const [value, setValue] = useState(initialValue);

    const handleChange = (event) => {
        setValue(event.target.value);
    }

    return {value, handleChange}
}

export default useInput;