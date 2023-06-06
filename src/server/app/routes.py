from app import app
from flask import make_response
from .utils import get_json_rand

@app.get('/')
def index():
    return make_response('OK', 200)

@app.get('/get-random-data')
def get_random_data():
    data = get_json_rand()
    return make_response(data, 200)
