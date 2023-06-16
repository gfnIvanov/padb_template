import sys
import csv
import json
from pathlib import Path
from data_types import MainData


def csv_to_json(raw_path: str, res_path: str):
    keys: list = None
    main = {'data': []}
    res_file = Path.joinpath(res_path, 'test.json')
    if Path(res_file).is_file():
        Path(res_file).unlink()
    with open(raw_path, newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=',', quotechar='|')
        for i, row in enumerate(rows):
            data: dict = None
            if i == 0:
                keys = row
            else:
                data = dict.fromkeys(keys)
                for ii, el in enumerate(row):
                    if el == 'NA':
                        data[keys[ii]] = None
                    else:
                        data[keys[ii]] = int(el) if el.isdigit() else el
                main['data'].append(data)
    validateData = MainData.parse_obj(main)
    with open(res_file, 'w+', encoding='utf-8') as new_JSON:
        json.dump(validateData.dict(), new_JSON, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    print(Path(__file__).resolve().parents[2])
    sys.path.append('src')
