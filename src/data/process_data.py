import os
import click
import logging
import yaml
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from classes.Dataset import Dataset
from csv_to_json import csv_to_json

root_dir = Path(__file__).resolve().parents[2]


@click.group()
def cli():
    pass


@click.command()
@click.option('--raw',
              type=click.Path(exists=True),
              help='Path to raw datasets')
@click.option('--res',
              type=click.Path(),
              help='Path to processed datasets')
@click.option('--key',
              type=str,
              help='Key field (case sensitive)')
@click.option('--type',
              type=click.Choice(['csv', 'txt', 'excel']),
              help='Raw files extension')
@click.option('--percent',
              type=int,
              help='Allowed gap percentage in a column')
@click.option('--log',
              is_flag=True,
              help='Whether or not to log the key variable')
@click.option('--dummy',
              is_flag=True,
              help='Process or not categorical features')
@click.option('--json',
              is_flag=True,
              help='Whether or not to convert test data to json')
@click.option('--rename',
              type=list[str],
              help='Array of fields to rename')
@click.option('--eject',
              type=list[dict],
              help='Array of fields to clear ejection')
def process(
        raw: str,
        res: str,
        key: str,
        type: str,
        percent: int,
        log: bool,
        dummy: bool,
        json: bool,
        rename: list[str],
        eject: list[dict]):
    try:
        logger = logging.getLogger(__name__)
        if type == 'csv':
            train_df = pd.read_csv(Path.joinpath(root_dir, raw, 'train.csv'))
            raw_test_path = Path.joinpath(root_dir, raw, 'test.csv')
            test_df = pd.read_csv(raw_test_path)
            click.echo(
                click.style(
                    f'Размер тренировочного набора {train_df.shape}',
                    fg='green'))
            click.echo(
                click.style(
                    f'Размер тестового набора {test_df.shape}\n',
                    fg='green'))
        else:
            raise Warning(
                'Флаги --type=txt и --type=excel пока не поддерживаются, используйте csv')
        if len(rename) > 0:
            for name in rename:
                new_name = ''.join(list(name)[1:]) + str(list(name)[0])
                train_df.rename(columns={name: new_name}, inplace=True)
                test_df.rename(columns={name: new_name}, inplace=True)
        dataset = Dataset(train_df, test_df, key, percent, log, dummy, eject)
        click.echo(dataset.info())
        dataset.process()
        all_data = dataset.df
        train_df = all_data.iloc[:train_df.shape[0], :]
        test_df = all_data.iloc[test_df.shape[0]:, :]
        test_df.drop(columns=['SalePrice'], axis=1, inplace=True)
        train_df.to_csv(Path.joinpath(root_dir, res, 'train.csv'))
        test_df.to_csv(Path.joinpath(root_dir, res, 'test.csv'))
        if json:
            csv_to_json(raw_test_path, Path.joinpath(root_dir, res))
        click.echo(
            click.style(
                f'Обработка датасетов завершена. Путь: {res}',
                fg='green'))
    except Warning as w:
        click.echo(click.style(w, fg='yellow'))
        logger.warning(w)
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

    with open(Path.joinpath(root_dir, os.getenv('PARAMS_DIR'), 'process_data.yaml')) as f:
        params = yaml.safe_load(f)

    cli(default_map=params)
