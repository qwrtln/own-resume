import React from "react";
import "./App.css";
import ResumeContainer from "./resume/ResumeContainer";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Tu będzie piękne résumé</h1>
        <h4>Kiedyś</h4>
      </header>
      <div>
        <ResumeContainer />
      </div>
    </div>
  );
}

export default App;
