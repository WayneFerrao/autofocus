#1 Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
import pandas as pd
from sklearn.svm import LinearSVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error 
from sklearn.linear_model import SGDRegressor


#Importing the dataset

df = pd.read_csv("finalEncoded.csv")
y = df['price']
X = df.drop(columns=['price'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)

svr = LinearSVR(epsilon=0.01, C=0.01, fit_intercept=True)

svr.fit(X_train, y_train)


def svr_results(y_test, X_test, fitted_svr_model):
    
    print("C: {}".format(fitted_svr_model.C))
    print("Epsilon: {}".format(fitted_svr_model.epsilon))
    
    print("Intercept: {:,.3f}".format(fitted_svr_model.intercept_[0]))
    print("Coefficient: {:,.3f}".format(fitted_svr_model.coef_[0]))
    
    mae = mean_absolute_error(y_test, fitted_svr_model.predict(X_test))
    print("MAE = ${:,.2f}".format(1000*mae))
    
    perc_within_eps = 100*np.sum(y_test - fitted_svr_model.predict(X_test) < 5) / len(y_test)
    print("Percentage within Epsilon = {:,.2f}%".format(perc_within_eps))
    
    # Plot outputs
    plt.figure(figsize=(10,7))
    plt.scatter(y_test, fitted_svr_model.predict(X_test))
    #plt.plot(X_test, fitted_svr_model.predict(X_test), color='red')
    #plt.plot(X_test, fitted_svr_model.predict(X_test)+eps, color='black')
    #plt.plot(X_test, fitted_svr_model.predict(X_test)-eps, color='black')
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.title('SVR Prediction')
    plt.show()

print(y_test.shape)
print(X_test.shape)
svr_results(y_test, X_test, svr)