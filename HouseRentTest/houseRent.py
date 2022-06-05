import pandas as pd

data = pd.read_csv('houses_to_rent.csv')

data = data [['city', 'rooms', 'bathroom', 'parking spaces', 'fire insurance', 'furniture', 'rent amount']]
print(data.head())
