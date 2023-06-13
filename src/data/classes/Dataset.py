import click
import numpy as np
import pandas as pd
from dataclasses import dataclass


@dataclass
class Dataset:
    train_df: pd.DataFrame
    test_df: pd.DataFrame
    key_var: str
    percent: int
    log: bool
    dummy: bool
    eject: list[dict]

    @property
    def df(self) -> pd.DataFrame:
        if self.all_data is None:
            raise Warning(
                'Нет доступа к свойству до выполнения метода process()')
        return self.all_data

    def info(self):
        click.echo(click.style('Параметры инстанса:', fg='green'))
        click.echo(click.style(f' - key_var: {self.key_var}', fg='green'))
        click.echo(click.style(f' - percent: {self.percent}', fg='green'))
        click.echo(click.style(f' - log: {self.log}', fg='green'))
        click.echo(click.style(f' - dummy: {self.dummy}\n', fg='green'))

    def process(self):
        if self.key_var not in self.train_df.columns:
            raise Warning(
                f'Ключевая переменная {self.key_var} отсутствует в тренировочном датасете')
        if self.log:
            self.train_df[self.key_var] = np.log1p(self.train_df[self.key_var])
        self.all_data = pd.concat([self.train_df, self.test_df], axis=0)
        self.all_data.drop(columns=['Id'], axis=1, inplace=True)
        self.__clearEmpty()
        if len(self.eject) > 0:
            for x in self.eject:
                self.__clearEjection(x['column'], x['index'])
        if self.dummy:
            self.__getDummies()

    def __clearEmpty(self):
        nullsValues = self.all_data.isnull().sum().sort_values(ascending=False)
        click.echo(
            click.style(
                'Обработка пропущенных значений в датасете...',
                fg='green'))
        click.echo(click.style('Всего значений пропущено:', fg='green'))
        for col in nullsValues.head(10).index:
            isNull = self.all_data[col].isnull().sum()
            null_from_total = str(
                round((isNull / self.all_data.shape[0]) * 100, 2))
            click.echo(
                click.style(
                    f'{col} {isNull} ({null_from_total})%\n',
                    fg='green'))

        for col in nullsValues.index:
            isNull = self.all_data[col].isnull().sum()
            nullsPercent = round((isNull / self.all_data.shape[0]) * 100, 2)
            if nullsPercent >= self.percent:
                self.all_data = self.all_data.drop(columns=[col], axis=1)
            else:
                if self.all_data[col].dtype == 'object':
                    self.all_data[col].fillna(value='UNKNOWN', inplace=True)
                else:
                    self.all_data[col].fillna(
                        value=self.all_data[col].median(), inplace=True)

    def __clearEjection(self, column, index):
        self.all_data = self.all_data.drop(
            self.all_data[self.all_data[column] > index].index)

    def __getDummies(self):
        click.echo(
            click.style(
                'Обработка категориальных признаков...',
                fg='green'))
        self.all_data = pd.get_dummies(self.all_data,
                                       columns=self.__getCategorical(),
                                       drop_first=False)
        click.echo(
            click.style(
                f'Новый размер датасета {self.all_data.shape}\n',
                fg='green'))

    def __getCategorical(self):
        return self.all_data.dtypes[self.all_data.dtypes == 'object'].index
