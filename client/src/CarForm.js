import styled from 'styled-components';

const FormContainer = styled.div`
    width: 800px;
    height: 500px;
    position:absolute;
    padding:7px;
    background: rgba(255, 255, 255, 0.55);
    margin-top: 3%;
    margin-left: 28%;

    border: 2px solid black;
    border-radius: 15px;

    
    z-index:900;
`;

export default function CarForm() {
    return (
        <FormContainer>

        </FormContainer>
    );
}