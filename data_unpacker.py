import pandas as pd
from sklearn.preprocessing import normalize

def unpack_data(path: str, preprocess: bool = False):
    '''Take data from house prices csv. Setting preprocess to true normalizes numerical data'''
    # Read data
    data = pd.read_csv(path)
    
    # Split catagorical parameters into booleam params
    data = pd.get_dummies(data)
    # Fill any remaining NaN with 0
    data = data.fillna(0)

    if preprocess:
        # Normalize numerical data, not including numerical categories or years
        categories = ["LotFrontage", 
                    "LotArea", 
                    "MasVnrArea", 
                    "BsmtFinSF1", 
                    "BsmtFinSF2",
                    "BsmtUnfSF",
                    "TotalBsmtSF",
                    "1stFlrSF",
                    "2ndFlrSF",
                    "LowQualFinSF",
                    "GrLivArea",
                    "BsmtFullBath",
                    "BsmtHalfBath",
                    "FullBath",
                    "HalfBath",
                    "TotRmsAbvGrd",
                    "Fireplaces",
                    "GarageCars",
                    "GarageArea",
                    "WoodDeckSF",
                    "OpenPorchSF",
                    "EnclosedPorch",
                    "3SsnPorch",
                    "ScreenPorch",
                    "PoolArea",
                    "MiscVal",
                    "SalePrice"]
        data[categories] = normalize(data[categories])

    return data