import pandas as pd
import numpy as np
from numpy import argmax
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

out_path = "dummy.csv"

df = pd.read_csv(out_path)

#use dff to do basic charts to show trends
dff = df.dropna(axis=0)

#set all categorical types to 'categorical'

#This stuff was for data analysis
#sns.lineplot(x=dff['year'], y=dff['price'])
#sns.scatterplot(x=dff['odometer'], y=dff['price'])

# color one hot encoder
colors = set(dff['paint_color'])
color_df = pd.DataFrame(colors, columns=['paint_color'])
# generate binary values using get_dummies
dum_df = pd.get_dummies(color_df, columns=["paint_color"], prefix=["Color_is"])
# merge with main df bridge_df on key values
color_df = color_df.join(dum_df)
print(color_df)

#model one hot encoder
models = set(dff['model'])
model_df = pd.DataFrame(models, columns=['model'])
# generate binary values using get_dummies
dum_df = pd.get_dummies(model_df, columns=["model"], prefix=["Model_is"])
# merge with main df bridge_df on key values
model_df = model_df.join(dum_df)
print(model_df)

#manufacturer
manufacturers = set(dff['manufacturer'])
manufacturer_df = pd.DataFrame(manufacturers, columns=['manufacturer'])
# generate binary values using get_dummies
dum_df = pd.get_dummies(manufacturer_df, columns=["manufacturer"], prefix=["Manufacturer_is"])
# merge with main df bridge_df on key values
manufacturer_df = manufacturer_df.join(dum_df)
print(manufacturer_df)

#drive
drives = set(dff['drive'])
drive_df = pd.DataFrame(drives, columns=['drive'])
# generate binary values using get_dummies
dum_df = pd.get_dummies(drive_df, columns=["drive"], prefix=["Drive_is"])
# merge with main df bridge_df on key values
drive_df = drive_df.join(dum_df)
print(drive_df)

#transmission
transmissions = set(dff['transmission'])
transmission_df = pd.DataFrame(transmissions, columns=['transmission'])
# generate binary values using get_dummies
dum_df = pd.get_dummies(transmission_df, columns=["transmission"], prefix=["Transmission_is"])
# merge with main df bridge_df on key values
transmission_df = transmission_df.join(dum_df)
print(transmission_df)

#condition
conditions = set(dff['condition'])
condition_df = pd.DataFrame(transmissions, columns=['condition'])
# generate binary values using get_dummies
dum_df = pd.get_dummies(condition_df, columns=["condition"], prefix=["Condition_is"])
# merge with main df bridge_df on key values
condition_df = condition_df.join(dum_df)
print(condition_df)





