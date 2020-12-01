import logo from './logo.svg';
import {useState, useEffect} from 'react';
import './App.css';

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(()=>{
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    })
  },[]); 
  return (
    <div className="App">
      <header className="App-header">
          The current time is {currentTime}
      </header>
    </div>
  );
}

export default App;
