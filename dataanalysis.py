import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

datafile = "clean3.csv"

df = pd.read_csv(datafile)

# =============================================================================
# for elem in range(len(df)):
#     try:
#         float(df['cylinders'][elem])
#     except:
#         df['cylinders'][elem] = float(0)
#     try:
#         float(df['drive'][elem])
#         df['drive'][elem] = float(0)
#     except:
#         pass
#         
# df = df.loc[df['cylinders'] != 0]
# df = df.loc[df['drive'] != 0]
# 
# df.to_csv("clean2.csv")
# =============================================================================

#df.groupby(['year']).mean().to_csv("year.csv")
byYear = df.sort_values(by=['year'])
data1 = byYear.loc[byYear['year'] <= 2002] #1900-2002
data2 = byYear.loc[byYear['year'] > 2002] #203-2021

# =============================================================================
# #YEAR VS PRICE
# # Add title
# plt.title("Price of Car Based on Year")
# 
# # Bar chart showing average arrival delay for Spirit Airlines flights by month
# sns.lineplot(x=data1['year'], y=data1['price'])
# 
# # Add label for vertical axis
# plt.ylabel("Price")
# =============================================================================

#DRIVE VS PRICE
# =============================================================================
# #Add title
# plt.title("Price of Car Based on Drive")
# 
# # Bar chart showing average arrival delay for Spirit Airlines flights by month
# sns.barplot(x=data2['drive'], y=data2['price'])
# 
# # Add label for vertical axis
# plt.ylabel("Price")
# =============================================================================

#CYLINDER VS PRICE
# =============================================================================
# #Add title
# plt.title("Price of Car Based on Cylinders")
# 
# # Bar chart showing average arrival delay for Spirit Airlines flights by month
# sns.barplot(x=data2['cylinders'], y=data2['price'])
# 
# # Add label for vertical axis
# plt.ylabel("Price")
# =============================================================================

#ODOMETER VS PRICE
# =============================================================================
# # Add title
# plt.title("Price of Car Based on Odometer")
# 
# # Bar chart showing average arrival delay for Spirit Airlines flights by month
# sns.lineplot(x=data1['odometer'], y=data1['price'])
# 
# # Add label for vertical axis
# plt.ylabel("Price")
# =============================================================================

# =============================================================================
# #COLOR VS PRICE
# # Add title
# plt.title("Average Price of Car Based on Colour")
# 
# # Bar chart showing average arrival delay for Spirit Airlines flights by month
# sns.barplot(x=data2['paint_color'], y=data2['price'])
# 
# # Add label for vertical axis
# plt.ylabel("Price")
# =============================================================================

# =============================================================================
# #TRANSMISSION VS PRICE
# # Add title
# plt.title("Average Price of Car Based on Transmission")
# 
# # Bar chart showing average arrival delay for Spirit Airlines flights by month
# sns.barplot(x=data2['transmission'], y=data2['price'])
# 
# # Add label for vertical axis
# plt.ylabel("Price")
# =============================================================================

# =============================================================================
# #ODOMETER VS YEAR
# #Add title
# plt.title("ODOMETER VS YEAR")
# 
# # Bar chart showing average arrival delay for Spirit Airlines flights by month
# sns.lineplot(x=data2['year'], y=data2['odometer'])
# 
# # Add label for vertical axis
# plt.ylabel("Odometer")
# =============================================================================


# =============================================================================
# #DISTRIBUTION OF COLOR
# colors = data2.pivot_table(index=['paint_color'], aggfunc='size')
# print(colors)
# for i in range(len(colors)):
#     print(colors[i])
#     print(len(data1))
#     colors[i] = (colors[i]/len(data2['paint_color'])) * 100
#     
# print(colors)
# =============================================================================


# =============================================================================
# #DISTRIBUTION OF TRANSMISSION
# transmissions = data2.pivot_table(index=['transmission'], aggfunc='size')
# print(transmissions)
# for i in range(len(transmissions)):
#     print(transmissions[i])
#     transmissions[i] = (transmissions[i]/len(data2['transmission'])) * 100
#     
# print(transmissions)
# =============================================================================

# =============================================================================
# #DISTRIBUTION OF DRIVE
# drives = data2.pivot_table(index=['drive'], aggfunc='size')
# print(drives)
# for i in range(len(drives)):
#     print(drives[i])
#     drives[i] = (drives[i]/len(data2['drive'])) * 100
#     
# print(drives)
# =============================================================================

# =============================================================================
# #DISTRIBUTION OF CYLINDER
# cylinders = data2.applymap(str).pivot_table(index=['cylinders'], aggfunc='size')
# print(cylinders)
# for i in range(len(cylinders)):
#     print(cylinders[i])
#     cylinders[i] = (cylinders[i]/len(data2['cylinders'])) * 100
#     
# print(cylinders)
# =============================================================================






