from flask import Flask
from flask_cors import CORS
from flask import make_response
from flask import request
from .utils import get_json_rand, format_reduction, predict_model

app = Flask(__name__)


CORS(app)


@app.get('/')
def index():
    return make_response('OK', 200)


@app.get('/get-random-data')
def get_random_data():
    data = get_json_rand()
    response = make_response(data, 200)
    return response


@app.post('/calc-price')
def calc_price():
    processed_data = format_reduction(request.get_json())
    prediction = str(round(predict_model(processed_data), 2))
    return make_response(prediction, 200)
