import { useRef } from 'react';

function PetCat () {

    let pet = useRef(0);

    function handleClick() {
        pet.current = pet.current + 1;
        alert('You clicked ' + pet.current + ' times!');
      }

  return (
    <div>
        <p> Pet Counter: {pet.current}</p>
        <button onClick={handleClick}> Pet the virtual cat! </button>
    </div>
  )
}

export default PetCat;

