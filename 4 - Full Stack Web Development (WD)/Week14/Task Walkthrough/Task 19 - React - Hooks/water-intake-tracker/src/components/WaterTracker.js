import { useState, useRef, useEffect } from 'react';

function WaterTracker() {
  const [intake, setIntake] = useState(0);
  const inputRef = useRef();

  useEffect(() => {
    inputRef.current.focus();
  }, []);

  const handleAddIntake = () => {
    const addedIntake = parseInt(inputRef.current.value, 10);
    setIntake(intake + addedIntake);
    inputRef.current.value = '';
  };

  const handleReset = () => {
    setIntake(0);
  };

  return (
    <div>
      <input ref={inputRef} type="number" placeholder="Enter water in ml" />
      <button onClick={handleAddIntake}>Add</button>
      <button onClick={handleReset}>Reset</button>
      <h1>Total Water Intake: {intake} ml</h1>
    </div>
  );
}

export default WaterTracker;
