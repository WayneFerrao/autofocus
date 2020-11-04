import pandas as pd
import numpy as np 
import random
import csv


def isNan(string):
    return string != string

def occurences(model):
    """returns percentage of each color in each model as a color: percent dictionary"""
    nulls = 0
    notnulls = 0
    occurence = {}
    #finds occurence of each color
    for i in range(len(df)):
        #find df model that matches and get colors that arent null
        if isNan(df['paint_color'][i]) == False and df['model'][i] == model:
            #update occurence of model
            if df['paint_color'][i] in occurence:
                occurence[df['paint_color'][i]] += 1
            else:
                occurence[df['paint_color'][i]] = 1
            notnulls += 1
        #nan for model
        elif df['model'][i] == model:
            nulls += 1
    
    for key in occurence:
        occurence[key] = round((occurence[key] / notnulls) * nulls)
        
    return occurence
    
def fillNan(dictionary):
    """takes dictionary of percentages and returns list of colors
    of size nulls"""
    nullList = []
    sumValues = sum(dictionary.values())
    for i in range(sumValues):
        while True:
            key = random.choice(list(dictionary))
            if dictionary[key] > 0:
                nullList.append(key)
                dictionary[key] -= 1
                break
    
    return nullList

def listOfModelColours(model):
    """return list of colours in order of appearance of model in csv"""
    modelOccurenceDict = occurences(model) 
    #NOTE: NUMBER OF VALUES IN DICT MAY BE HIGHER OR LOWER BY A NUMBER OR SO.
    newNullList = fillNan(modelOccurenceDict)
    return newNullList


df = pd.read_csv("out.csv", dtype={"numbers":"string", "condition": "string", "id": "string", "odometer":"string", "price":"string","year":"string"})

models = list(set(df['model']))
modelDict = {}
for model in models:
    """fill in every value for model if there is at least one of these models with
    a colour to base off of. Find ratio of color, then create list of size nan model colors"""
    modelDict[model] = listOfModelColours(model)
  
filledInList = []
#iterate through and append each corresponding list        
for i in range(len(df)):
    #i is model and color index
    #check if color is null
    if isNan(df['paint_color'][i]):
        #check if the modelDict has color values to append with
        if len(modelDict[df['model'][i]]) > 0:
            #take modelDict value list and append
            filledInList.append([df['model'][i], modelDict[df['model'][i]].pop()])
        else:
            #take df model and value and append
            filledInList.append([df['model'][i], df['paint_color'][i]])
    else:
        #take df model and value and append
        filledInList.append([df['model'][i], df['paint_color'][i]])
        
#filledInList contains [model, color]
df = pd.DataFrame(filledInList)
df.to_csv("dummy.csv")

    
