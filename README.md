### padb_template
==============================

A training project for preparing data and a linear regression model, which is needed to organize a server that takes a data set as input and calculates the cost of a house based on the received data using a pre-trained model

[Web-interface](https://github.com/gfnIvanov/padb_web)

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── pre-commit-config.yaml
    ├── docker-compose.yml
    ├── Dockerfile
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models
    │
    ├── notebooks          <- Jupyter notebooks.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── process_data.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── process_model.py <- train and save model
    │   │
    │   ├── server         <- Flask-server (sends test data and calculates price)
    │   │   ├── manage.py
    │   │   └── app 
    │   │       ├── __init__.py 
    │   │       └── utils 
    │   │           └── __init__.py 
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

### Data processing

Usage ```src/data/process_data.py process```

```
Options:
  --raw PATH              Path to raw datasets
  --res PATH              Path to processed datasets
  --key TEXT              Key field (case sensitive)
  --type [csv|txt|excel]  Raw files extension
  --percent INTEGER       Allowed gap percentage in a column
  --log                   Whether or not to log the key variable
  --dummy                 Process or not categorical features
  --help                  Show this message and exit.
```

### Model processing

Usage ```src/models/process_model.py process```

```
Options:
  --csv PATH       Path to csv files
  --res PATH       Path to pre-trained model dir
  --tsize FLOAT    Test size
  --estim INTEGER  N_estimators
  --depth INTEGER  Max depth
  --rate FLOAT     Learning rate
  --help           Show this message and exit.
```

### Pre-commit check all
```
pre-commit run --all-files
```

### Run with Docker-compose
```
docker-compose build

docker-compose up -d
```

### Watch logs
```
docker-compose logs -f
```

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
