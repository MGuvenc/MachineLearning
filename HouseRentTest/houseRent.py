import pandas as pd

data = pd.read_csv('houses_to_rent.csv')
print(data.head())

data = data [['city', 'rooms', 'bathroom', 'parking spaces',
     'floor', 'animal', 'furniture', 'hoa', 'rent amount',
     'property tax', 'fire insurance', 'total']]
