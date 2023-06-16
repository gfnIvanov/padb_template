import os
import yaml
import json
import pickle
import random
import pandas as pd
import numpy as np
from pathlib import Path
from .data_types import CSVData

root_dir = Path(__file__).resolve().parents[3]


def get_json_rand() -> CSVData:
    global params
    with open(Path.joinpath(root_dir, os.getenv('PARAMS_DIR'), 'process_data.yaml')) as f:
        params = yaml.safe_load(f)

    json_file = Path.joinpath(root_dir, params['process']['res'], 'test.json')

    with open(json_file) as f:
        json_data = json.load(f)

    rand = random.randint(0, len(json_data['data']))

    return json_data['data'][rand]


def format_reduction(data: CSVData) -> float:
    results = []
    json_file = Path.joinpath(root_dir, params['process']['res'], 'test.csv')
    df = pd.read_csv(json_file, index_col=[0])
    for col in df.columns:
        split_res = col.split('_')
        col_name = split_res[0]
        col_value = split_res[1] if len(split_res) > 1 else None
        if col_value is None:
            median = df[col].median()
            results.append(median if data[col] is None else data[col])
        else:
            cur_value = 'UNKNOWN' if data[col_name] is None else data[col_name]
            res = 1 if cur_value == col_value else 0
            results.append(res)
    df_for_predict = pd.DataFrame([results], columns=df.columns)
    return df_for_predict


def predict_model(data: pd.DataFrame) -> int:
    with open(Path.joinpath(root_dir, os.getenv('PARAMS_DIR'), 'process_model.yaml')) as f:
        params = yaml.safe_load(f)
    with open(Path.joinpath(root_dir, params['process']['res'], 'XGBmodel.dat'), 'rb') as f:
        model = pickle.load(f)

    return np.expm1(model.predict(data))[0]
