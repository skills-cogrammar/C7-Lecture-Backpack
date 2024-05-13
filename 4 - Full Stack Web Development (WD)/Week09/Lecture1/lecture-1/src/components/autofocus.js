import { useRef, useEffect } from 'react';

function AutoFocusInput () {
 
    let ref = useRef();

    useEffect( () => {
        ref.current.focus();
    }, [])


    return (
        <input type='text' ref = {ref}></input>
    )
}

export default AutoFocusInput;