#!/usr/bin/env bash

python ./src/data/process_data.py process
python ./src/models/process_model.py process
python src/server/main.py