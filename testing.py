

import pandas as pd
import numpy as np
import seaborn as sns

'''
data = pd.read_csv("data/algal_data_day_1.csv")

df_pivot = data.pivot_table(index='x', 
                          columns='y', 
                          values='value', 
                          aggfunc='mean').sort_index(ascending=False)

sns.heatmap(df_pivot, annot=True, cmap='coolwarm')
'''


# import all files

# make it into one mega file per ressource 




def fix_range(df_temp):
    min_value = df_temp['value'].min()
    
    df_temp = df_temp.dropna()
    if(min_value > 0):
        df_temp['value'] = df_temp['value'] - abs(min_value)
    else:
        df_temp['value'] = df_temp['value'] + abs(min_value)
        
    return df_temp



def make_df(day):
    print('day : '+ str(day))
    # preserve
    # what we will return
    df_returned = pd.DataFrame()
    
    # get path
    path = "data/coral_data_day_" + str(day) + ".csv"
    df_coral = pd.read_csv(path)
    # sort data
    df_coral = fix_range(df_coral)
    # since preserve values should be (-)
    df_coral['value'] = -df_coral['value']
    # append into return df
    df_returned = df_returned._append(df_coral,ignore_index=True)
    print('coral : ', df_coral['value'].min())
    
    
    #repeat
    
    # obtain
    path = "data/helium_data_day_" + str(day) + ".csv"
    df_helium = pd.read_csv(path)
    df_helium = fix_range(df_helium)
    df_returned = df_returned._append(df_helium,ignore_index=True)
    
    print('helium : ', df_helium['value'].max())
    
    # obtain
    path = "data/oil_data_day_" + str(day) + ".csv"
    df_oil = pd.read_csv(path)
    df_oil = fix_range(df_oil)
    df_returned = df_returned._append(df_oil,ignore_index=True)
    print('oil : ', df_oil['value'].max())
    
    # obtain or perserve
    # we choose to not count it as perserve as it overlaps with the helium
    path = "data/ship_data_day_" + str(day) + ".csv"
    df_ship = pd.read_csv(path)
    df_ship = fix_range(df_ship)
    df_returned = df_returned._append(df_ship,ignore_index=True)
    print('ship : ', df_ship['value'].max())
    
    # preserve
    path = "data/species_data_day_" + str(day) + ".csv"
    df_species = pd.read_csv(path)
    df_species = fix_range(df_species)
    # since preserve values should be (-)
    df_species['value'] = -df_species['value']
    df_returned = df_returned._append(df_species,ignore_index=True)
    print('species : ', df_species['value'].min())
    
    # obtain
    path = "data/metal_data_day_" + str(day) + ".csv"
    df_metal = pd.read_csv(path)
    df_metal = fix_range(df_metal)
    print('metal : ', df_metal['value'].max())
   
    
    df_returned = df_returned._append(df_metal,ignore_index=True)
    
    return df_returned
    



#make files of all types per day 


df_day_1 = make_df(1)
df_day_2 = make_df(2)
df_day_3 = make_df(3)
df_day_4 = make_df(4)
df_day_5 = make_df(5)
df_day_6 = make_df(6)
df_day_7 = make_df(7)
df_day_8 = make_df(8)
df_day_9 = make_df(9)
df_day_10 = make_df(10)
df_day_11 = make_df(11)
df_day_12 = make_df(12)
df_day_13 = make_df(13)
df_day_14 = make_df(14)
df_day_15 = make_df(15)
df_day_16 = make_df(16)
df_day_17 = make_df(17)
df_day_18 = make_df(18)
df_day_19 = make_df(19)
df_day_20 = make_df(20)
df_day_21 = make_df(21)
df_day_22 = make_df(22)
df_day_23 = make_df(23)
df_day_24 = make_df(24)
df_day_25 = make_df(25)
df_day_26 = make_df(26)
df_day_27 = make_df(27)
df_day_28 = make_df(28)
df_day_29 = make_df(29)
df_day_30 = make_df(30)




# helium maxing 

# x : 0,3
# y : 0,3

def helium_maxing(day):
    
    # obtain
    path = "data/helium_data_day_" + str(day) + ".csv"
    df_hel = pd.read_csv(path)
    df_hel = fix_range(df_hel)
    
    df_hel = df_hel[df_hel['x'] < 4]
    df_hel = df_hel[df_hel['y'] < 4]
    
    print('helium : ', df_hel['value'].max())
    
    return df_hel

    



    
#df_hell = helium_maxing(3)




# i want to know what to perserve around the helium 

'''
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
        
    df_temp = df_temp[df_temp['x'] < 4]
    df_temp = df_temp[df_temp['y'] < 4]
        
    #add it to the mega file for ressource 
    
    df_temp.insert(4,"day", j)
    
    df_coral = df_coral._append(df_temp,ignore_index=True)


# species
df_species = pd.DataFrame()
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
    
    df_temp_species = df_temp
        
    df_temp = df_temp[df_temp['x'] < 4]
    df_temp = df_temp[df_temp['y'] < 4]
        
    #add it to the mega file for ressource 
    
    df_temp.insert(4,"day", j)
    
    df_species = df_species._append(df_temp,ignore_index=True)
    
    
# ships
df_ships = pd.DataFrame()
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
        
    df_temp = df_temp[df_temp['x'] < 4]
    df_temp = df_temp[df_temp['y'] < 4]
        
    #add it to the mega file for ressource 
    
    df_temp.insert(4,"day", j)
    
    df_ships = df_ships._append(df_temp,ignore_index=True)


'''



#algo time .,.,.,.,.,.,.,..,

'''
# this is the see the heat map used in the slides 

df_pivot = df_day_1.pivot_table(index='x', 
                          columns='y', 
                          values='value', 
                          aggfunc='mean').sort_index(ascending=False)

sns.heatmap(df_pivot, annot=True, cmap='coolwarm')

'''

# after looking the data and maps, helium is the best mineral, so know we need to see which tiles to not destroy ecologically 

#sort preserves 
df_eco = df_day_1[df_day_1['value'] < 0]
df_eco = df_eco[df_eco['x'] < 4]
df_eco = df_eco[df_eco['y'] < 4]

df_eco['tag'] = "x" + df_eco['x'].apply(str) + "y" + df_eco['y'].apply(str)
df_eco = df_eco.groupby('tag').sum()


# so now we know all the the eco values in the coral region 
# so daily we want to find the best place to send the rig that day 
# since the square is a 4x4 we can move to any of those tiles that day as we have 5 movuments

# we will need to reopen the oil info for that day as it is ineficient to go back to the old tiles
day = 1
path = "data/helium_data_day_" + str(day) + ".csv"
df_helium = pd.read_csv(path)
df_helium = fix_range(df_helium)




