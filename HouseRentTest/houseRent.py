import pandas as pd
import numpy as np
import sklearn

from sklearn import preprocessing, linear_model

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

# SPLIT DATA
x = np.array(data.drop(['rent amount'], 1))
y = np.array(data['rent amount'])

print('X', x.shape)
print('Y', y.shape)

xTrain, xTest, yTrain, yTest = sklearn.model_selection.train_test_split(x, y, test_size=0.2, random_state=10)

print('XTest', xTest.shape)
print('XTrain', xTrain.shape)

# TRAINING DATA
model = linear_model.LinearRegression()
model.fit(xTrain, yTrain)
accuracy = model.score(xTest, yTest)
print('Coefficients: ', model.coef_)
print('Intercept: ', model.intercept_)
print('Accuracy: %', round(accuracy*100, 3))

# Manuel Test
testVals = model.predict(xTest)
print(testVals.shape)
error = []
for i, testVal in enumerate(testVals):
    error.append(yTest[i] - testVal)
    print(f'Actual: {yTest[i]}, Prediction: {int(testVal)}, Error: {int(error[i])}')
