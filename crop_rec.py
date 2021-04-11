#!/usr/bin/env python
# coding: utf-8

import numpy as np 
import pandas as pd 

df = pd.read_csv('C://Users//Ratnadeep Gawade//Desktop//python//Machine Learning//Data Set//Projects//Crop Predcition//apy_clean.csv')
df.head()

df.columns

df.drop('Unnamed: 0', axis=1, inplace=True)

df.head()

new_df = df.groupby([df["State_Name"]=="Maharashatra", df["District_Name"]=="AKOLA", "Crop"]).mean()

def major_crops(state_name, district_name):
    state_name = str.capitalize(state_name)
    district_name = str.upper(district_name)
    
    state_df = df[df["State_Name"]==state_name]
    district_df = state_df[state_df["District_Name"]==district_name]
    df_new = district_df.groupby(by="Crop").mean().sort_values(by="Production", ascending=False).reset_index()
    
    crop_grown = df_new["Crop"][0:10]
    
    return crop_grow.to_list()






