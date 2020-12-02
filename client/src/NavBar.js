import styled from 'styled-components'
import car from './car.jpg'
import {Link } from 'react-router-dom';

const RowDiv = styled.div`
  text-align: center;
  padding-top: 2%;
`;

const Item = styled.p`
  display: inline-block;
  font-family: 'Source Sans Pro';
  font-weight: 400;
  font-size: 1.2em;
  color: #333;
  text-align: center;
  margin-left: 2%;
  margin-right: 2%;
  cursor: pointer;
  &:hover {
    transform: scale(1.25);
  }
`;



export default function NavBar() {
    return (
        <RowDiv>
            <Item>Search</Item>
            <Item><a href = {car} style={{textDecoration: "none", color: "#222"}} target = "_blank">Report</a></Item>
        </RowDiv>
    );
}