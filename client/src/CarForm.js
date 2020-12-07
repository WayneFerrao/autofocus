import  {Component} from 'react';
import axios from 'axios';
import styled from 'styled-components';
import { Select } from 'semantic-ui-react'
axios.defaults.baseURL = 'http://localhost:5000';
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
const MainAtt = styled.div`
`;

const SideAtt = styled.div`
`;
const AttDiv = styled.div`
    display:inline-block;
    flex-direction: column;
`;
const Dropdown = styled.select`
    height: 25px;
    width: 100px;
`;


const manufacturer = ['AC', 'Acura', 'Alfa Romeo', 'Alpina', 'Alpine', 'Aro', 
'Aston Martin', 'Audi', 'Austin', 'BMW', 'Bentley', 'Bristol', 'Buick', 'Cadillac', 
'ChangFeng', 'Chevrolet', 'Chrysler', 'Citroen', 'DS', 'Dacia', 'Dadi', 'Daewoo', 'Daihatsu', 
'Dallas', 'Derways', 'Dodge', 'DongFeng', 'Eagle', 'FAW', 'Ferrari', 'Fiat', 'Ford', 'GAZ', 
'GMC', 'Haval', 'Hindustan', 'Holden', 'Honda', 'Hummer', 'Hyundai', 'Infiniti', 'Innocenti', 
'Isdera', 'Isuzu', 'Jaguar', 'Jeep', 'Jiangling', 'Kia', 'Koenigsegg', 'Lamborghini', 'Land Rover', 
'Lexus', 'Lincoln', 'MCC', 'MG', 'Mahindra', 'Maruti', 'Maserati', 'Mazda', 'McLaren', 'Mega', 
'Mercedes-Benz', 'Mercury', 'Mini', 'Mitsubishi', 'Nissan', 'Oldsmobile', 'Peugeot', 'Pontiac', 
'Porsche', 'Renault', 'Rimac', 'Ronart', 'Saab', 'Saturn', 'Scion', 'SsangYong', 'Subaru', 'Suzuki', 
'TVR', 'Talbot', 'Tata', 'Toyota', 'Triumph', 'VAZ', 'VUHL', 'Venturi', 'Volkswagen', 'Volvo'];
const manMod = {
'AC': ['cobra'],
'Acura': ['cl', 'el', 'ilx', 'integra', 'mdx', 'rdx', 'rl', 'rlx', 'rsx', 'tl', 'tlx', 'tsx'],
'Alfa Romeo': ['145', '6', '90', 'giulia', 'gt', 'spider', 'stelvio'],
'Alpina': ['b9'],
'Alpine': ['v6'],
'Aro': ['10', '24'],
'Aston Martin': ['v8'],
'Audi': ['100', '200', '50', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'cabriolet', 'coupe', 'q3', 'q5', 'q7', 'quattro', 'r8', 's3', 's4', 's5', 's6', 's8', 'sq5', 'tt'],
'Austin': ['metro', 'montego'],
'BMW': ['m2', 'm3', 'm4', 'm5', 'm6', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'z3', 'z4'],
'Bentley': ['continental'],
'Bristol': ['speedster'],
'Buick': ['century', 'enclave', 'encore', 'lacrosse', 'lucerne', 'reatta', 'regal', 'rendezvous', 'riviera', 'roadmaster', 'sedan', 'skylark', 'terraza'],
'Cadillac': ['allante', 'ats', 'brougham', 'ct6', 'cts', 'dts', 'eldorado', 'escalade', 'fleetwood', 'seville', 'srx', 'sts', 'xlr', 'xt5', 'xts'],
'ChangFeng': ['suv'],
'Chevrolet': ['alero', 'astra', 'astro', 'avalanche', 'aveo', 'blazer', 'camaro', 'caprice', 'captiva', 'cavalier', 'classic', 'cobalt', 'colorado', 'corvette', 'cruze', 'equinox', 'hhr', 'impala', 'lumina', 'malibu', 'monza', 'prizm', 'silverado', 'spark', 'ssr', 'starcraft', 'suburban', 'tahoe', 'tracker', 'trailblazer', 'traverse', 'trax', 'uplander', 'van', 'venture', 'volt'],
'Chrysler': ['300', '300m', 'aspen', 'concorde', 'crossfire', 'intrepid', 'neon', 'pacifica', 'prowler', 'sebring', 'stratus', 'viper', 'voyager'],
'Citroen': ['c4', 'c5', 'cx', 'gs'],
'DS': ['3', '4', '5', '7'],
'Dacia': ['duster', 'nova'],
'Dadi': ['shuttle'],
'Daewoo': ['arcadia'],
'Daihatsu': ['delta', 'max'],
'Dallas': ['fun'],
'Derways': ['aurora'],
'Dodge': ['avenger', 'caliber', 'caravan', 'challenger', 'charger', 'dakota', 'dart', 'durango', 'journey', 'magnum', 'nitro', 'ram', 'stealth'],
'DongFeng': ['mpv'],
'Eagle': ['premier'],
'FAW': ['jetta'],
'Ferrari': ['328', '400', '430', 'california'],
'Fiat': ['124', '500', '600'],
'Ford': ['bronco', 'c-max', 'cougar', 'econoline', 'ecosport', 'edge', 'escape', 'escort', 'excursion', 'expedition', 'explorer', 'f-150', 'f-250', 'f-350', 'f-450', 'fiesta', 'flex', 'focus', 'freestar', 'freestyle', 'fusion', 'mustang', 'ranger', 'shelby', 'sierra', 'taurus', 'thunderbird', 'windstar'],
'GAZ': ['13', '14', '20'],
'GMC': ['acadia', 'canyon', 'envoy', 'jimmy', 'safari', 'savana', 'sonoma', 'terrain', 'yukon'],
'Haval': ['h2'],
'Hindustan': ['lancer'],
'Holden': ['rodeo'],
'Honda': ['accord', 'city', 'civic', 'cr-v', 'cr-z', 'element', 'fit', 'hr-v', 'insight', 'odyssey', 'passport', 'pilot', 'prelude', 'ridgeline', 's2000', 'today', 'z'],
'Hummer': ['h3'],
'Hyundai': ['accent', 'elantra', 'genesis', 'i30', 'ioniq', 'kona', 'matrix', 'santa', 'sonata', 'tiburon', 'tucson', 'veloster'],
'Infiniti': ['ex', 'fx', 'g20', 'g35', 'g37', 'i35', 'm35', 'q50', 'q60', 'q70', 'qx30', 'qx4', 'qx50', 'qx56', 'qx60', 'qx70', 'qx80'],
'Innocenti': ['mini', 'small'],
'Isdera': ['spyder'],
'Isuzu': ['trooper'],
'Jaguar': ['f-pace', 'f-type', 's-type', 'x-type', 'xe', 'xf', 'xj', 'xjs', 'xkr'],
'Jeep': ['cherokee', 'commander', 'compass', 'liberty', 'patriot', 'renegade', 'wrangler'],
'Jiangling': ['e-series'],
'Kia': ['cadenza', 'forte', 'niro', 'optima', 'rio', 'roadster', 'sedona', 'sorento', 'soul', 'spectra', 'sportage', 'stinger'],
'Koenigsegg': ['cc'],
'Lamborghini': ['huracan'],
'Land Rover': ['defender', 'discovery', 'hardtop'],
'Lexus': ['ct', 'es', 'gx', 'is', 'ls', 'lx', 'nx', 'rc', 'rx', 'sc'],
'Lincoln': ['aviator', 'mark', 'mkc', 'mks', 'mkt', 'mkx', 'mkz', 'navigator', 'zephyr'],
'MCC': ['smart'],
'MG': ['mgb', 'midget'],
'Mahindra': ['armada'],
'Maruti': ['1000', '800', 'versa'],
'Maserati': ['ghibli', 'granturismo', 'levante', 'quattroporte'],
'Mazda': ['2', '626', 'cx-5', 'cx-9', 'mx-5', 'protege', 'tribute'],
'McLaren': ['f1'],
'Mega': ['club'],
'Mercedes-Benz': ['220', '240', '250', 'c-class', 'cabrio', 'cla', 'clk', 'cls', 'e-class', 'g-class', 'gl', 'gla', 'glc', 'gle', 'glk', 'gls', 'ml', 's-class', 'sl', 'slk'],
'Mercury': ['mariner', 'milan', 'monterey', 'mountaineer', 'sable'],
'Mini': ['convertible'],
'Mitsubishi': ['delica', 'eclipse', 'endeavor', 'galant', 'gto', 'i', 'mirage', 'montero', 'outlander', 'raider'],
'Nissan': ['350z', '370z', 'altima', 'bluebird', 'cherry', 'crew', 'cube', 'datsun', 'frontier', 'juke', 'kicks', 'leaf', 'maxima', 'murano', 'nv200', 'pathfinder', 'quest', 'rogue', 'sentra', 'titan'],
'Oldsmobile': ['bravada', 'cutlass', 'intrigue', 'silhouette'],
'Peugeot': ['2008', 'ion'],
'Pontiac': ['bonneville', 'fiero', 'firebird', 'g6', 'lemans', 'montana', 'solstice', 'sunfire', 'torrent', 'vibe'],
'Porsche': ['911', '944', 'boxster', 'cayenne', 'cayman', 'macan', 'panamera'],
'Renault': ['11', '12', '15', '16', '17', '18', '19', '25', '30', '9', 'latitude'],
'Rimac': ['one'],
'Ronart': ['lightning'],
'Saab': ['03-Sep', '900', '95', '96', '99'],
'Saturn': ['aura', 'outlook', 'relay', 'sky', 'vue'],
'Scion': ['fr-s', 'ia', 'im', 'tc', 'xa', 'xb', 'xd'],
'SsangYong': ['family'],
'Subaru': ['ascent', 'baja', 'brz', 'forester', 'impreza', 'legacy', 'outback', 'tribeca', 'wrx', 'xv'],
'Suzuki': ['forenza', 'kizashi', 'samurai', 'sx4', 'vitara', 'xl7'],
'TVR': ['3000', '350', '450', 's'],
'Talbot': ['solara'],
'Tata': ['mint'],
'Toyota': ['4runner', 'avalon', 'c-hr', 'camry', 'celica', 'corolla', 'crown', 'echo', 'highlander', 'iq', 'prius', 'sequoia', 'sienna', 'sprinter', 'supra', 'tacoma', 'tundra', 'venza', 'yaris'],
'Triumph': ['1500', '2500'],
'VAZ': ['4x4'],
'VUHL': ['5'],
'Venturi': ['210'],
'Volkswagen': ['atlas', 'beetle', 'caddy', 'eos', 'golf', 'passat', 'tiguan', 'touareg'],
'Volvo': ['850', 'c30', 'c70', 's40', 's60', 's70', 's80', 's90', 'v50', 'v60', 'v70', 'xc60', 'xc70', 'xc90']
}
const colors = ['black', 'blue', 'brown', 'custom', 'green', 'grey', 'orange', 'purple', 'red', 'silver', 'white', 'yellow']
const manOptions = manufacturer.map((brand) =>
<option value={brand}>{brand}</option>
);
const colorOptions = colors.map((color) =>
<option value={color}>{color}</option>
);


export default class CarForm extends Component {
    constructor(){
        super();
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    async handleSubmit(event) {
        event.preventDefault();
        let data = new FormData(event.target);
        axios.post('/getData',data);
    }
    render(){
        return (
            <FormContainer>
                <form onSubmit={this.handleSubmit}>
                    <MainAtt>
                        <AttDiv>
                            <label for="cars">Manufacturer:</label>
                            <br/>
                            {/* <Select placeholder='Select your manufacturer' options={countryOptions} /> */}
                            <Dropdown name="manufacturer" id="cars">
                            {manOptions}
                            </Dropdown>
                        </AttDiv>
                        <AttDiv>
                            <label for="cars">Model:</label>
                            <br/>
                            <select name="model" id="cars">
                                <option value="volvo">Volvo</option>
                                <option value="saab">Saab</option>
                                <option value="opel">Opel</option>
                                <option value="audi">Audi</option>
                            </select>
                        </AttDiv>

                    <label for="cars">Please enter the approximate mileage:</label>
                    <input type="number" id="mileage" name="mileage"/>
                    <label for="cars">Please enter the model year:</label>
                    <input type="number" id="year" name="year"/>
                    </MainAtt>
                    <SideAtt>
                    <label for="cars">Transmission:</label>
                    <select name="transmission" id="transmission">
                        <option value="automatic">Automatic</option>
                        <option value="manual">Manual</option>
                        <option value="other">Other</option>
                    </select>
                    <label for="cars">Colour:</label>
                    <select name="color" id="color">
                        {colorOptions}
                    </select>
                    <label for="cars">Drive:</label>
                    <select name="drive" id="drive">
                        <option value="4wd">4WD</option>
                        <option value="rwd">RWD</option>
                        <option value="fwd">FWD</option>
                    </select>
                    <label for="cars">Number of cylinders:</label>
                    <select name="cylinders" id="cylinders">
                        <option value="1">1</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                        <option value="6">6</option>
                        <option value="8">8</option>
                    </select>
                    </SideAtt>
                <br/>
                <button>Submit</button> 
                </form>

            </FormContainer>
        );
    }
}