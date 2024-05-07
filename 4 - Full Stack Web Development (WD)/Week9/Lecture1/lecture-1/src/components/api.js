import React, { useState, useEffect } from 'react';

function API() {
  let [funFact, setFunFact] = useState(null);
  let [change, setChange] = useState(0);

  useEffect(() => {
    async function fetchData() {
      let response = await fetch("https://catfact.ninja/fact/");
      let data = await response.json();
      console.log(data.fact)
      setFunFact(data.fact);
    }
    fetchData();
  }, [change])


  function handleClick () {
    setChange(change + 1);
  }

  return (
    <div>
      <h1>{funFact}</h1>
      <button onClick = {handleClick}> New Fact </button>
    </div>
  )
}
export default API;



