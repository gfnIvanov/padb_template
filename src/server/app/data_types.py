from typing import Union
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
    RoofMatl: StrValue
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
