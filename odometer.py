import pandas as pd
import numpy as np 
import random
import csv

df = pd.read_csv("dummy2.csv")
df['odometer'].astype(float)
df['price'].astype(float)
df['year'].astype(float)
df['odometer'].fillna(0.0, inplace=True)
dff = df[df.odometer.notnull()]
dff = dff.loc[dff['odometer'] != 0]
# =============================================================================
# df = df[df.year.notnull()]
# df = df[df.price.notnull()]
# select_color = df.loc[df['price'] >= 200]
# select_color.to_csv("dummy2.csv")
# =============================================================================
#print(df['odometer'].isnull().sum())


#run through each year and get number to represent average price of a car that year.
uniqueYears = set(dff['year'])
ratios = {}
for year in uniqueYears:
    dfYear = dff.loc[dff['year'] == year]
    #add column of price / odometer
    dfYear['rate'] = dfYear['price'] / dfYear['odometer']
    #find average of price / odometer
    average = dfYear['rate'].sum()/len(dfYear['rate'])
    ratios[year] = average
print(ratios)
#at this point, each average is matched with the index of that average + 1900
#with empty odometers, take the average of the year and do price/average = odometer
for row in range(len(df)):
    if df['odometer'][row] == 0 and df['year'][row] in ratios:
        #get new odometer value, then set df['odometer'][row]
        year = df['year'][row]
        average = ratios[year]
        odometer = df['price'][row] / average
        df['odometer'][row] = odometer
df.to_csv("dummy3.csv")
    
