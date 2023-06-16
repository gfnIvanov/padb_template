import os
import click
import logging
import yaml
import pickle
import pandas as pd
from pathlib import Path
import xgboost as xgb
from dotenv import load_dotenv
from sklearn.model_selection import train_test_split

root_dir = Path(__file__).resolve().parents[2]


@click.group()
def cli():
    pass


@click.command()
@click.option('--csv',
              type=click.Path(exists=True),
              help='Path to csv files')
@click.option('--res',
              type=click.Path(exists=True),
              help='Path to pre-trained model dir')
@click.option('--tsize',
              type=float,
              help='Test size')
@click.option('--estim',
              type=int,
              help='N_estimators')
@click.option('--depth',
              type=int,
              help='Max depth')
@click.option('--rate',
              type=float,
              help='Learning rate')
def process(
        csv: str,
        res: str,
        tsize: float,
        estim: int,
        depth: int,
        rate: float):
    try:
        logger = logging.getLogger(__name__)
        train_df = pd.read_csv(
            Path.joinpath(
                root_dir,
                csv,
                'train.csv'),
            index_col=[0])
        y = train_df['SalePrice']
        train_df.drop(columns=['SalePrice'], axis=1, inplace=True)
        X = train_df
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=tsize, random_state=0)
        model = xgb.XGBRegressor(
            n_estimators=estim,
            max_depth=depth,
            learning_rate=rate)
        model.fit(X_train, y_train)
        with open(Path.joinpath(root_dir, res, 'XGBmodel.dat'), 'wb') as f:
            pickle.dump(model, f)

        click.echo(
            click.style(
                f'Обучение модели завершено. Путь: {res}',
                fg='green'))
        click.echo(
            click.style(
                f'Качество обучения: {model.score(X_test, y_test)}',
                fg='green'))
    except Exception as e:
        click.echo(click.style(e, fg='red'))
        logger.error(e)


cli.add_command(process)

if __name__ == '__main__':
    load_dotenv()

    log_file = Path.joinpath(root_dir, os.getenv('LOG_FILE'))

    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    log_level = logging.INFO if os.getenv('MODE') == 'dev' else logging.ERROR
    logging.basicConfig(level=log_level, filename=log_file, format=log_fmt)

    with open(Path.joinpath(root_dir, os.getenv('PARAMS_DIR'), 'process_model.yaml')) as f:
        params = yaml.safe_load(f)

    cli(default_map=params)
