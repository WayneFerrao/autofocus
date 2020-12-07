from flask import Flask
from flask import request
import datetime 
import json
# from RFR import reg
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

with open('encode.json') as json_file:
    data = json.load(json_file)
@app.route('/getData', methods=['GET', 'POST'])
def get_data():
    # print(request.form)
    # print(data)
    manufacturer = data['manufacturer'][request.form.get('manufacturer')]

    # model = data['model'][request.form.get('model')]
    model = 1
    odometer = request.form.get('mileage')
    transmission = data['transmission'][request.form.get('transmission')]
    color = data['color'][request.form.get('color')]
    drive = data['drive'][request.form.get('drive')]
    cylinders = request.form.get('cylinders')
    year = request.form.get('year')

    queryPoint = [[cylinders, drive, manufacturer, model, odometer, color, transmission, year]]
    print(queryPoint)
    print('//////////')
    reg = pickle.load(open('finalized_model_pickle.sav', 'rb'))
    prediction = reg.predict(queryPoint)
    print(prediction[0])
    return ("BOI")

