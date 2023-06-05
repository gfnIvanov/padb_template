import csv
import json
from typing import Union
from pathlib import Path
from pydantic import BaseModel

IntValue = Union[int, None]
StrValue = Union[str, None]

class CSVData(BaseModel):
    Id: int
    MSSubClass: IntValue
    MSZoning: StrValue
    LotFrontage: IntValue
    LotArea: IntValue
    Street: StrValue
    Alley: StrValue
    LotShape: StrValue
    LandContour: StrValue
    Utilities: StrValue
    LotConfig: StrValue
    LandSlope: StrValue
    Neighborhood: StrValue
    Condition1: StrValue
    Condition2: StrValue
    BldgType: StrValue
    HouseStyle: StrValue
    OverallQual: IntValue
    OverallCond: IntValue
    YearBuilt: IntValue
    YearRemodAdd: IntValue
    RoofStyle: StrValue
    RoofMatl:StrValue
    Exterior1st: StrValue
    Exterior2nd: StrValue
    MasVnrType: StrValue
    MasVnrArea: IntValue
    ExterQual: StrValue
    ExterCond: StrValue
    Foundation: StrValue
    BsmtQual: StrValue
    BsmtCond: StrValue
    BsmtExposure: StrValue
    BsmtFinType1: StrValue
    BsmtFinSF1: IntValue
    BsmtFinType2: StrValue
    BsmtFinSF2: IntValue
    BsmtUnfSF: IntValue
    TotalBsmtSF: IntValue
    Heating: StrValue
    HeatingQC: StrValue
    CentralAir: StrValue
    Electrical: StrValue
    stFlrSF1: IntValue
    ndFlrSF2: IntValue
    LowQualFinSF: IntValue
    GrLivArea: IntValue
    BsmtFullBath: IntValue
    BsmtHalfBath: IntValue
    FullBath: IntValue
    HalfBath: IntValue
    BedroomAbvGr: IntValue
    KitchenAbvGr: IntValue
    KitchenQual: StrValue
    TotRmsAbvGrd: IntValue
    Functional: StrValue
    Fireplaces: IntValue
    FireplaceQu: StrValue
    GarageType: StrValue
    GarageYrBlt: IntValue
    GarageFinish: StrValue
    GarageCars: IntValue
    GarageArea: IntValue
    GarageQual: StrValue
    GarageCond: StrValue
    PavedDrive: StrValue
    WoodDeckSF: IntValue
    OpenPorchSF: IntValue
    EnclosedPorch: IntValue
    SsnPorch3: IntValue
    ScreenPorch: IntValue
    PoolArea: IntValue
    PoolQC: StrValue
    Fence: StrValue
    MiscFeature: StrValue
    MiscVal: IntValue
    MoSold: IntValue
    YrSold: IntValue
    SaleType: StrValue
    SaleCondition: StrValue

class MainData(BaseModel):
    data: list[CSVData]

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
        
