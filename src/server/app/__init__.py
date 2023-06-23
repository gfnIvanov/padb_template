import os
import click
import logging
from flask import Flask
from flask_cors import CORS
from flask import make_response
from flask import request
from pathlib import Path
from .utils import get_json_rand, format_reduction, predict_model

root_dir = Path(__file__).resolve().parents[3]

logger = logging.getLogger(__name__)

app = Flask(__name__)


CORS(app)


@app.get('/')
def index():
    return make_response('OK', 200)


@app.get('/get-random-data')
def get_random_data():
    try:
        data = get_json_rand()
        response = make_response(data, 200)
        return response
    except Exception as e:
        click.echo(click.style(e, fg='red'))
        logger.error(e)


@app.post('/calc-price')
def calc_price():
    try:
        processed_data = format_reduction(request.get_json())
        prediction = str(round(predict_model(processed_data), 2))
        return make_response(prediction, 200)
    except Exception as e:
        click.echo(click.style(e, fg='red'))
        logger.error(e)


if __name__ == '__main__':
    log_file = Path.joinpath(root_dir, os.getenv('LOG_FILE'))
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    log_level = logging.INFO if os.getenv('MODE') == 'dev' else logging.ERROR
    logging.basicConfig(level=log_level, filename=log_file, format=log_fmt)
