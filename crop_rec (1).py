#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 


# In[2]:


df = pd.read_csv('C://Users//Ratnadeep Gawade//Desktop//python//Machine Learning//Data Set//Projects//Crop Predcition//apy_clean.csv')
df.head()


# In[3]:


df.columns


# In[4]:


df.drop('Unnamed: 0', axis=1, inplace=True)


# In[5]:


df.head()


# In[6]:


new_df = df.groupby([df["State_Name"]=="Maharashatra", df["District_Name"]=="AKOLA", "Crop"]).mean()


# In[ ]:





# In[ ]:





# In[8]:


def major_crops(state_name, district_name):
    state_name = str.capitalize(state_name)
    district_name = str.upper(district_name)
    
    state_df = df[df["State_Name"]==state_name]
    district_df = state_df[state_df["District_Name"]==district_name]
    df_new = district_df.groupby(by="Crop").mean().sort_values(by="Production", ascending=False).reset_index()
    
    crop_grown = df_new["Crop"][0:10]
    
    return crop_grown.to_list()


# In[14]:


crop_list = major_crops("Maharashtra", "Akola")
crop_list


# In[10]:


crop_df = pd.read_csv('C://Users//Ratnadeep Gawade//Desktop//python//Machine Learning//Data Set//Projects//Crop Predcition//crop_new_dataset.csv')
crop_df.drop('Unnamed: 0', axis=1, inplace=True)
crop_df.head()


# In[13]:


crop_df[crop_df["Crop"]=="rice"].iloc[:, 1:5]


# In[15]:


def soil_values(crop):
    values_df = crop_df[crop_df["Crop"]==crop].iloc[:, 1:5]
    return values_df


# In[16]:


soil_values("rice")


# In[ ]:




