import keras as keras
import keras
import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

#use dot graph
'''
#get X and y
dftrain = pd.read_csv("training.csv")
dftest = pd.read_csv("testing.csv")
#get ys
ytrain = dftrain['price']
ytest = dftest['price']
#get Xs
Xtrain = dftrain.drop(columns='price')
Xtest = dftest.drop(columns='price')
'''
df = pd.read_csv("finalenc.csv")
y = df['price']
X = df.drop(columns=['price'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

tf.keras.backend.clear_session()
tf.random.set_seed(60)
model=keras.models.Sequential([
    #input layer
    keras.layers.Dense(X_train.shape[1], input_dim = X_train.shape[1], activation='relu'), 
    keras.layers.BatchNormalization(),
    keras.layers.Dropout(0.3),

    keras.layers.Dense(units=30,activation='relu'), 
    keras.layers.BatchNormalization(),
    keras.layers.Dropout(0.2),

    #output layer
    keras.layers.Dense(units=1, activation="linear"),
],name="Batchnorm",)

optimizer = keras.optimizers.Adam()
model.compile(optimizer=optimizer, 
            loss='mean_absolute_error')
history = model.fit(X_train, y_train,
                    epochs=100, batch_size=2000,
                    validation_data=(X_test, y_test), 
                    verbose=1)

