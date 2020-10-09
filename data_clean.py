import pandas as pd
import numpy as np

#df is shorthand for DataFrame
df = pd.read_csv('test.csv')

df = df.drop('lat',axis=1)
df = df.drop('long',axis=1)
df = df.drop('url',axis=1)
df = df.drop('region_url',axis=1)
df = df.drop('county',axis=1)
df = df.drop('description',axis=1)
df = df.drop('image_url',axis=1)
df = df.drop('vin',axis=1)
df = df.drop('type',axis=1)
df = df.drop('size',axis=1)
df = df.drop('fuel',axis=1)
df = df.drop('state',axis=1)

# At this point, most of the useless columns are dropped. 
# Next steps

# Remove or update bad rows-> those with missing values for main columns like make, model etc
# Ensure each row has all columns filled/updated

#Write to a vehicles_final.csv
print(df)
