import styled from 'styled-components'
import car from './car.jpg'
import Party from './Particles';
import CarForm from './CarForm';

const SharpBlur = styled.div`
  overflow: hidden;
  flex-direction: column;
  width:100vw;
`;

const SearchPageParallax = styled.div`
  position: absolute;
  margin-left:12%;
  margin-top: 4%;
  display: flex;
  z-index: 999;
`;
const SearchPageBG = styled.div`
  height: 102vh;
  width: 100vw;

  background-image:  url(${car});
  -webkit-filter: blur(10px);
  -moz-filter: blur(10px);
  -o-filter: blur(10px);
  -ms-filter: blur(10px);
  filter: blur(10px);
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  overflow-y: auto;
  margin: -5px -10px -10px;
  z-index: 1;
`;
const ParticleContainer = styled.div`
position:absolute;
  width: 100vw;
  text-align:center
  height: 100%;
  z-index: 50;
`;

export default function Search() {
    return (
        <SharpBlur>
        <SearchPageParallax>

        </SearchPageParallax>
        <ParticleContainer>
          <CarForm/>

          <Party/>
        </ParticleContainer>
        <SearchPageBG>
        <CarForm/>
     
        </SearchPageBG>
       
      </SharpBlur>
    );
}