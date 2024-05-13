import './App.css';
import CatPic from "./components/catPic.js";
import { useState } from "react";
import CatButton from "./components/newCatButton.js";


// Add functionality which allows image and button to work together

// Additional Tasks: 
// Add input field to specify type of cat 
// See if you could add a brief description of the cat in a paragraph
// Change the colour of the button everytime it's clicked

function App() {
  function getImage(){
    let number = Math.floor(Math.random()*10)+1;
    let imgPath = `frogs/${number}.png`;
    return imgPath;

    // let items = [];
    // fetch("https://api.thecatapi.com/v1/images/search")
    // .then((res) => res.json())
    // .then((result) => {
    //   items = result[0];
    //   console.log(items.url);
    //   return items.url;
    // });
  }

  let [url, setURL] = useState(getImage());

  function urlUpdate() {
    setURL(getImage());
  }

  return (
    <div> 
      <CatPic url={url}> </CatPic>
      <CatButton changeURL={urlUpdate}> </CatButton>
    </div>
  )
}

export default App;
