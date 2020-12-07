from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import pickle
import statistics

df = pd.read_csv("finalEncoded.csv")
y = df['price']
X = df.drop(columns=['price'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)

reg = RandomForestRegressor(max_depth=80, random_state=0)
reg.fit(X_train, y_train)
filename = 'finalized_model_pickle.sav'
pickle.dump(reg, open(filename, 'wb'))

y_pred = reg.predict(X_test)

#calculate average loss
diff = abs(y_test - y_pred)
aloss = sum(diff)/len(diff)
#calculate median loss
mloss = statistics.median(diff)

print(aloss)
print(mloss)

plt.figure()
plt.axis([0,100000,0,100000])
plt.scatter(y_test[:1000] ,y_pred[:1000], alpha=0.4, c='red', label='Ground Truth vs Predicted')
plt.xlabel('Ground Truth')
plt.ylabel('Predictions')
plt.legend()
plt.title("Random Forest Model")
plt.savefig('RFR.png')