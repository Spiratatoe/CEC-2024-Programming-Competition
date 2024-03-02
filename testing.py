

import pandas as pd
import numpy as np
import seaborn as sns

data = pd.read_csv("data/algal_data_day_1.csv")

df_pivot = data.pivot_table(index='x', 
                          columns='y', 
                          values='value', 
                          aggfunc='mean').sort_index(ascending=False)

sns.heatmap(df_pivot, annot=True, cmap='coolwarm')




# import all files

# make it into one mega file per ressource 







# algal
df_algal = pd.DataFrame()
for i in range(30):
    # ele 1 is 0 ele 30 is 29
    j = i+1
    path = "data/algal_data_day_" + str(j) + ".csv"
    df_temp = pd.read_csv(path)
    
    # fix the range
    # step 1 find the min value
    # step 2 either increase/decrease every value equaly such that min is zero 
    
    min_value = df_temp['value'].min()
    
    df_temp = df_temp.dropna()
    if(min_value > 0):
        df_temp['value'] = df_temp['value'] - abs(min_value)
    else:
        df_temp['value'] = df_temp['value'] + abs(min_value)
        
    #add it to the mega file for ressource 
    
    df_temp.insert(4,"day", j)
    
    df_algal = df_algal._append(df_temp,ignore_index=True)
    
# coral
df_coral = pd.DataFrame()
for i in range(30):
    # ele 1 is 0 ele 30 is 29
    j = i+1
    path = "data/coral_data_day_" + str(j) + ".csv"
    df_temp = pd.read_csv(path)
    
    # fix the range
    # step 1 find the min value
    # step 2 either increase/decrease every value equaly such that min is zero 
    
    min_value = df_temp['value'].min()
    
    df_temp = df_temp.dropna()
    if(min_value > 0):
        df_temp['value'] = df_temp['value'] - abs(min_value)
    else:
        df_temp['value'] = df_temp['value'] + abs(min_value)
        
    #add it to the mega file for ressource 
    
    df_temp.insert(4,"day", j)
    
    df_coral = df_coral._append(df_temp,ignore_index=True)
    
# helium
df_helium = pd.DataFrame()
for i in range(30):
    # ele 1 is 0 ele 30 is 29
    j = i+1
    path = "data/helium_data_day_" + str(j) + ".csv"
    df_temp = pd.read_csv(path)
    
    # fix the range
    # step 1 find the min value
    # step 2 either increase/decrease every value equaly such that min is zero 
    
    min_value = df_temp['value'].min()
    
    df_temp = df_temp.dropna()
    if(min_value > 0):
        df_temp['value'] = df_temp['value'] - abs(min_value)
    else:
        df_temp['value'] = df_temp['value'] + abs(min_value)
        
    #add it to the mega file for ressource 
    
    df_temp.insert(4,"day", j)
    
    df_helium = df_helium._append(df_temp,ignore_index=True)
    
# oil
df_oil = pd.DataFrame()
for i in range(30):
    # ele 1 is 0 ele 30 is 29
    j = i+1
    path = "data/oil_data_day_" + str(j) + ".csv"
    df_temp = pd.read_csv(path)
    
    # fix the range
    # step 1 find the min value
    # step 2 either increase/decrease every value equaly such that min is zero 
    
    min_value = df_temp['value'].min()
    
    df_temp = df_temp.dropna()
    if(min_value > 0):
        df_temp['value'] = df_temp['value'] - abs(min_value)
    else:
        df_temp['value'] = df_temp['value'] + abs(min_value)
        
    #add it to the mega file for ressource 
    
    df_temp.insert(4,"day", j)
    
    df_oil = df_oil._append(df_temp,ignore_index=True)

# ship
df_ship = pd.DataFrame()
for i in range(30):
    # ele 1 is 0 ele 30 is 29
    j = i+1
    path = "data/ship_data_day_" + str(j) + ".csv"
    df_temp = pd.read_csv(path)
    
    # fix the range
    # step 1 find the min value
    # step 2 either increase/decrease every value equaly such that min is zero 
    
    min_value = df_temp['value'].min()
    
    df_temp = df_temp.dropna()
    if(min_value > 0):
        df_temp['value'] = df_temp['value'] - abs(min_value)
    else:
        df_temp['value'] = df_temp['value'] + abs(min_value)
        
    #add it to the mega file for ressource 
    
    df_temp.insert(4,"day", j)
    
    df_ship = df_ship._append(df_temp,ignore_index=True)
    
# species
df_species = pd.DataFrame()
for i in range(30):
    # ele 1 is 0 ele 30 is 29
    j = i+1
    path = "data/species_data_day_" + str(j) + ".csv"
    df_temp = pd.read_csv(path)
    
    # fix the range
    # step 1 find the min value
    # step 2 either increase/decrease every value equaly such that min is zero 
    
    min_value = df_temp['value'].min()
    
    df_temp = df_temp.dropna()
    if(min_value > 0):
        df_temp['value'] = df_temp['value'] - abs(min_value)
    else:
        df_temp['value'] = df_temp['value'] + abs(min_value)
        
    #add it to the mega file for ressource 
    
    df_temp.insert(4,"day", j)
    
    df_species = df_species._append(df_temp,ignore_index=True)
    
    












