import pandas as pd
import numpy as np 
import random
import csv

file = "dummy4.csv"

df = pd.read_csv(file)

#odometer has an "automatic" value that we need to remove
df['odometer'].fillna(0, inplace=True)
df['price'].fillna(0.0, inplace=True)
df['year'].fillna(0.0, inplace=True)

#removes all values from price, odometer, and year that are non convertible to float
for elem in range(len(df)):
    try:
        df['odometer'][elem].astype(float)
    except:
        df['odometer'][elem] = float(0)
    try:
        df['price'][elem].astype(float)
    except:
        df['price'][elem] = float(0)
    try:
        df['year'][elem].astype(float)
    except:
        df['year'][elem] = float(0)

#new dff using df without null price and year
dff = df[df.price.notnull()]
dff = dff[df.year.notnull()]
dff = dff.loc[dff['odometer'] != 0]

#run through each year and get number to represent average price of a car that year.
uniqueYears = set(dff['year'])
uniqueYears.remove(0)
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
newfile = "odometerTest.csv"
df.to_csv(newfile)
    
