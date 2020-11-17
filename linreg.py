import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

np.set_printoptions(precision=3, suppress=True)


df = pd.read_csv('dividedsamples/training.csv') 
dfval = pd.read_csv('dividedsamples/testing.csv') 

train_features = df.copy()
test_features = dfval.copy()

train_labels = train_features.pop('price')
test_labels = test_features.pop('price')

regressor = LinearRegression()
regressor.fit(train_features, train_labels)
coeff_df = pd.DataFrame(regressor.coef_, train_features.columns, columns=['Coefficient'])
print(coeff_df)

y_pred = regressor.predict(test_features)
boi = pd.DataFrame({'Actual': test_labels, 'Predicted': y_pred})
print(boi)