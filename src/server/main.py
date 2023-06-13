import os
import yaml
from app import app
from pathlib import Path
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()

    root_dir = Path(__file__).resolve().parents[2]

    debug = os.getenv('MODE') == 'dev'

    with open(Path.joinpath(root_dir, os.getenv('PARAMS_DIR'), 'server.yaml')) as f:
        params = yaml.safe_load(f)

    app.run(port=params['port'], debug=debug)
