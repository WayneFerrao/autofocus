import pandas as pd 
import json as js
import csv
from multiprocessing import Process, Pipe
import os

#checking if a given model is present in the dictionary already
def add_model(model,car_data,manu):
    if model not in car_data:
        car_data[model] = manu

#Parses the car db file and returns a dict containing a mapping from Models -> Brand/Manufacturer
def parse_car_db():

    f = open('car_database.json','r',encoding="utf-8").readlines()
    cars = {}

    for line in f:
        parsed = js.loads(line)
        #add_model(parsed['Brand'] + ' ' + parsed['Model'],cars)
        add_model(parsed['Model'].lower(),cars,parsed['Brand'])
    return cars

def compareAndPrune(car_dict,pd_frame,i1,i2,conn):
    count = 0
    pid = os.getpid()
    new_df = pd.DataFrame()

    for i in range(i1,i2):
        conn.send([pid,str(count) + '/' + str((i2-i1)) ]) #send current progress to main process
        url = pd_frame.url[i].split('/')[5].split('-') #split the URL
        if len(url) > 3: #handles cases where the URL is not formatted correctly               
            url_data = check_parsed_url(url)
            date = url_data[0]
            mod = pd_frame.model[i]

            if type(mod) == str: #if the model isn't empty
                url_data.extend(mod.split(' ')) #add the words in the model string to the rest of the words we need to check

            for j in range(1,len(url_data)): #iterate over all words we need to check against the cars, start at index 1, since the first value in the url_data is the date
                item = url_data[j].lower() #make our guess lowercase
                if item in car_dict: #if the guess is in the car db, then add it to a temp dataframe, retaining all other data for the record,
                    temp = pd_frame.loc[i]
                    temp.model = item #set the model value to the correctly guessed model
                    temp.manufacturer = car_dict[item] #set the manufacturer value to the one in the car db (more accurate)
                    
                    cylinder = pd_frame.cylinders[i] #clean up the cylinder column
                    if type(cylinder) != float:
                        temp.cylinders = pd_frame.cylinders[i][0]
                    temp.date = date #set date value to the extracted value from the URL (more accurate)
                    new_df = new_df.append(temp)
                    count += 1 #add value to count
                    break
    return new_df

#helper function to reformat the url if the location has a hyphen
def check_parsed_url(url_list):
    try:
        int(url_list[1])
        return url_list[1:]
    except ValueError:
        return url_list[2:]

def main_process(car_stats,df,i1,i2,conn,filename='out.csv'):
    new_df = compareAndPrune(car_stats,df,i1,i2,conn)
    new_df = new_df.drop('url',axis=1) #drop url axis
    new_df.to_csv(filename,mode='a',index=True) #append results to main file

if __name__ == '__main__':
    car_stats = parse_car_db()
    matches = 0
    df = pd.read_csv('vehicles.csv')

    df = df.drop('lat',axis=1)
    df = df.drop('long',axis=1)
    df = df.drop('region_url',axis=1)
    df = df.drop('county',axis=1)
    df = df.drop('description',axis=1)
    df = df.drop('image_url',axis=1)
    df = df.drop('vin',axis=1)
    df = df.drop('type',axis=1)
    df = df.drop('size',axis=1)
    df = df.drop('fuel',axis=1)
    df = df.drop('state',axis=1)

    df1 = df.iloc[0:len(df.model)//2] #First third of dataframe
    df2 = df.iloc[len(df.model)//3:2*len(df.model)//3] #Second third of dataframe
    df3 = df.iloc[2*len(df.model)//3:] #Third third of dataframe

    parent_conn1, child_conn1 = Pipe()
    parent_conn2, child_conn2 = Pipe()
    parent_conn3, child_conn3 = Pipe()

    p1 = Process(target=main_process,args=(car_stats,df1,0,len(df.model)//3,child_conn1,0))
    p2 = Process(target=main_process,args=(car_stats,df2,len(df.model)//3,2 * (len(df.model))//3,child_conn2,1))
    p3 = Process(target=main_process,args=(car_stats,df3,2*(len(df.model))//3,len(df.model),child_conn3,2))

    p1.start()
    p2.start()
    p3.start()

    while True: #print the progress of each process
        print(parent_conn1.recv(),parent_conn2.recv(),parent_conn3.recv())

    #guessing colour
    #figure out the colour breakdown of the ford mustang
    #g = a['model'].unique() 
    #g = a.groupby(['model'])['model'].count()
    # g = g.sort_values(ascending=False)