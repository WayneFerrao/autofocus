import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("finalEncoded.csv")
y = df['price']
X = df.drop(columns=['price'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)

reg = LinearRegression().fit(X_train, y_train)

y_pred = reg.predict(X_test)
diff = abs(y_pred - y_test)

print(sum(diff)/len(diff))
print(reg.score(X_train, y_train))

# Plot outputs
plt.figure(figsize=(10,7))
plt.scatter(y_test, y_pred)
plt.xlim(0,80000)
#plt.plot(X_test, fitted_svr_model.predict(X_test), color='red')
#plt.plot(X_test, fitted_svr_model.predict(X_test)+eps, color='black')
#plt.plot(X_test, fitted_svr_model.predict(X_test)-eps, color='black')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Linear Regression Prediction')
plt.show()