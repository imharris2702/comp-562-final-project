import pandas as pd

def unpack_data(path: str):
    # Read data
    data = pd.read_csv(path)
    
    # Split catagorical parameters into booleam params
    data = pd.get_dummies(data)
    # Fill any remaining NaN with 0
    data = data.fillna(0)

    return data