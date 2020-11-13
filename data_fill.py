import pandas as pd
import numpy as np

#For filling values

def get_counts(df,obj): #where object is transmission,drive or whatever
    model_dict = {}
    models = df['model'].unique()
    for model in models:
        model_dict[model] = {}
    new_df = df.groupby(['model',obj]).size().reset_index()
    for i in range(0,len(new_df)):
        line = new_df.iloc[i]
        model,transmission = line['model'],line[obj]
        model_dict[model][transmission] = line[0]
    return model_dict

def make_ratios(dictionary,df):
    new_dict = {}
    models = df['model'].unique()
    for model in models:
        new_dict[model] = {}
    for i in dictionary:
        for obj in dictionary[i]:
            #print(dictionary[i][trans],sum(dictionary[i].values()))
            new_dict[i][obj] = dictionary[i][obj] / sum(dictionary[i].values())
    return new_dict

def make_counts(dictionary,obj): #turn the ratios into the number of values that need to be replaced
    new_dict = {}
    for m in dictionary:
        new_dict[m] = {}

    for model in dictionary:
        total =  len(df[df['model'] == model][obj] == np.nan)
        for trans in dictionary[model]:
            new_dict[model][trans] = round(dictionary[model][trans] * total)

        if dictionary[model] != {} and sum(new_dict[model].values()) != total:
            new_dict[model][trans] += abs(total - sum(new_dict[model].values()))
    
    return new_dict

def fill_values(dictionary,df,obj): #fill the values in the dataframe based
    final_df_l = []
    count = 0
    for model in dictionary:
        print(model,count,'/',len(dictionary))
        prev = 0
        model_df = df[df['model'] == model]
        for trans in dictionary[model]:
            num = dictionary[model][trans]
            rep_df = model_df[prev:prev+num]
            prev = num
            rep_df = rep_df.fillna({obj:trans})
            final_df_l.append(rep_df)
        count += 1
    output_df = pd.concat(final_df_l)
    return output_df
#df is shorthand for DataFrame
df = pd.read_csv('clean2.csv')

d1 = get_counts(df,'transmission')
d1 = make_ratios(d1,df)
d1 = make_counts(d1,'transmission')

df1 = fill_values(d1,df,'transmission')

d2 = get_counts(df,'cylinders')
d2 = make_ratios(d2,df)
d2 = make_counts(d2,'cylinders')

df2 = fill_values(d2,df1,'cylinders')


d3 = get_counts(df,'drive')
d3 = make_ratios(d3,df)
d3 = make_counts(d3,'drive')

df3 = fill_values(d2,df2,'drive')


df3.to_csv('test.csv')
#print(d)
#print(d)
'''
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
df = df.drop('state',axis=1)'''

# At this point, most of the useless columns are dropped. 
# Next steps

# Remove or update bad rows-> those with missing values for main columns like make, model etc
# Ensure each row has all columns filled/updated

#Write to a vehicles_final.csv
#print(df)
