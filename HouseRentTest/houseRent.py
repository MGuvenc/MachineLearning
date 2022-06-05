import pandas as pd

data = pd.read_csv('houses_to_rent.csv')

data = data [['city', 'rooms', 'bathroom', 'parking spaces', 'fire insurance', 'furniture', 'rent amount']]
print(data.head())

data['rent amount'] = data['rent amount'].map(lambda i: int(i[2:].replace(',', '')))
data['fire insurance'] = data['fire insurance'].map(lambda i: int(i[2:]))
print(data.head())