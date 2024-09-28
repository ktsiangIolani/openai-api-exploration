import "./App.css";
import React, { useState } from "react";

function App() {
  //------------------------------- STATES ------------------------------------

  const [message, setMessage] = useState(null);
  const [word, setWord] = useState("");

  //------------------------------- API CALLS ------------------------------------

  // returns a synonym from the server
  const getSynonym = () => {
    fetch("http://localhost:5000/api/thesaurus", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ word: word }),
    })
      .then((response) => response.json())
      .then((data) => setMessage(data.message))
      .catch((error) => console.error(error));
  };

  //------------------------------- COMPONENTS ------------------------------------

  const GetSynonymButton = () => {
    return (
      <button type="button" onClick={getSynonym}>
        Find a better word
      </button>
    );
  };

  return (
    <div className="App">
      <div className="App-header">
        <h1>AI Thesaurus</h1>
        <form onSubmit={getSynonym}>
          <input
            type="text"
            placeholder="Give me a word"
            value={word}
            onChange={(event) => setWord(event.target.value)}
          />
        </form>
        <GetSynonymButton />
        {message && (
          <p>
            A better alternative is: <p id="synonym">{message}</p>
          </p>
        )}
      </div>
    </div>
  );
}

export default App;
