import car from './car.jpg'
import {useState, useEffect} from 'react';
import styled from "styled-components";
import {BrowserRouter as Router, Route} from 'react-router-dom';
import Search from './Search';
import NavBar from './NavBar';

const BGContainer = styled.div`
  width: 100vw;
  height: 100vh;
  background-image: url(${car});
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  overflow-y: auto;
`;

const Title = styled.div`
  font-family: 'Carme';
  font-weight: 400;
  color: #2d262a;
  font-size: 6.5em;
  text-align: center;
  padding-top: 2%;
  @media (min-width: 1024px) {
    padding-top:3%;
  }
  margin-bottom: 0;
  padding-bottom: 0;
`;

const Motto  = styled.h3`
  font-family: 'Source Sans Pro';
  font-weight: 300;
  font-style: italic;
  font-size: 1.6em;
  text-align: center;
  margin-top: 0.5%;
`;
const TransitionText = styled.h1`
  text-align: center;
  overflow: hidden;
  flex-direction: column;
`;
function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(()=>{
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    })
  },[]); 

 
  const Home = () => (
    <body>
      <BGContainer>
        <NavBar/>
        <Title>Autofocus</Title>
        <Motto>The true price of a car.</Motto>
        </BGContainer>
          <TransitionText class="subTitle"> Let's find out the real price </TransitionText>

      <Search/>
    </body>
  );
  
  return (
    <Router>
      <Route exact path='/' component={Home}/>
      <Route path='/search' component={Search}/>
      
    </Router>
  );
}

export default App;
