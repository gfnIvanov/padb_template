import os
import boto3
import yaml
from pathlib import Path

root_dir = Path(__file__).resolve().parents[2]

with open(Path.joinpath(root_dir, os.getenv('PARAMS_DIR'), 'process_model.yaml')) as f:
    params = yaml.safe_load(f)

bucket_name = 'padb-cv-3m'

session = boto3.session.Session()

s3 = session.client(
    service_name='s3',
    aws_access_key_id=os.getenv('aws_access_key_id'),
    aws_secret_access_key=os.getenv('aws_secret_access_key'),
    endpoint_url='https://storage.yandexcloud.net'
)


def upload_model():
    s3.upload_file(
        Path.joinpath(
            root_dir,
            params['process']['res'],
            'XGBmodel.dat'),
        bucket_name,
        'XGBModel.dat')


def download_model():
    resp_object = s3.get_object(Bucket=bucket_name, Key='XGBModel.dat')
    with open(Path.joinpath(root_dir, params['process']['res'], 'XGBmodel.dat'), 'wb') as f:
        f.write(resp_object['Body'].read())
