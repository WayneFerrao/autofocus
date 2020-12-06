from sklearn.svm import LinearSVR
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("finalenc.csv")
y = df['price']
X = df.drop(columns=['price'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)

regr = make_pipeline(StandardScaler(), LinearSVR(random_state=0, tol=1e-03))
reg = LinearRegression().fit(X_train, y_train)

regr.fit(X_train,y_train)

y_pred = regr.predict(X_test)

plt.figure()
plt.plot(range(100000))
plt.scatter(y_test ,y_pred, alpha=0.4, c='red', label='Ground Truth vs Predicted')
plt.savefig('SVR.png')