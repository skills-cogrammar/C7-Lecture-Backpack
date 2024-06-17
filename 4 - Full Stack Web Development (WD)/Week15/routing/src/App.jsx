import { useEffect, useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import Navbar from "./components/NavBar";
import { Link, Outlet, useLoaderData } from "react-router-dom";

function App() {
  const { results } = useLoaderData();

  console.log(results);

  return (
    <>
      <Navbar />
      <div className="flex w-full justify-between px-8">
        <div className="">
          {results.map((character) => {
            return (
              <div key={character.id}>
                <Link to={`contacts/${character.id}`} state={character}>Character {character.id}</Link>
              </div>
            );
          })}
        </div>

        <Outlet />
      </div>
    </>
  );
}

export const fetchCharacters = async () => {
  const response = await fetch("https://rickandmortyapi.com/api/character");
  const data = await response.json();
  const results = data.results;
  return { results };
};

export default App;
