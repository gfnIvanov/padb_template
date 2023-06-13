from app import app
from flask import make_response
from .utils import get_json_rand


@app.get('/')
def index():
    return make_response('OK', 200)


@app.get('/get-random-data')
def get_random_data():
    data = get_json_rand()
    response = make_response(data, 200)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.get('/get-calc-price')
def get_calc_price():
    response = make_response({'price': 250000}, 200)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
