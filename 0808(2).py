import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Binarizer
from sklearn.linear_model import LinearRegression
header = ['preg', 'plas', 'pres', 'skin',
          'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv',
                   names=header)

array = data.values
x = array[:, 0:8]
y = array[:, 8]
print(x.shape, y.shape)
scaler = StandardScaler()
rescaled_X = scaler.fit_transform(x)
print(rescaled_X)
model = LinearRegression()
model.fit(x, y)

predicted_Y = model.predict(x)
y = (predicted_Y > 0.5).astype(int)
print(y)


# scaler = Binarizer(threshold=0.5)
# rescaled_X = scaler.fit_transform(x)
# print(rescaled_X)


# scaler = MinMaxScaler(feature_range=(0, 1))
# rescaled_X = scaler.fit_transform(x)
# print(rescaled_X)



