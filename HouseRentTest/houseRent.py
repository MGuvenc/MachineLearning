import pandas as pd
import numpy as np
from sklearn import preprocessing

# IMPORT DATA
data = pd.read_csv('houses_to_rent.csv')
data = data[['city', 'rooms', 'bathroom', 'parking spaces', 'fire insurance', 'furniture', 'rent amount']]

print(data.head())

# MAP DATA
data['rent amount'] = data['rent amount'].map(lambda i: int(i[2:].replace(',', '')))
data['fire insurance'] = data['fire insurance'].map(lambda i: int(i[2:]))

le = preprocessing.LabelEncoder()
data['furniture'] = le.fit_transform(data['furniture'])

print(data.head())

# CHECKING NULL DATA
print(data.isnull().sum())
# data = data.dropna() If data is null

# SPLIT DATA#
x = np.array(data.drop(['rent amount'], 1))
y = np.array(data['rent amount'])

print('X', x.shape)
print('Y', y.shape)
