#!/usr/bin/env python
# coding: utf-8

import numpy as np 
import pandas as pd 

df = pd.read_csv('C://Users//Ratnadeep Gawade//Desktop//python//Machine Learning//Data Set//Projects//Crop Predcition//apy_clean.csv')
df.head()

df.shape

x = df["State_Name"].unique()

df.columns

df.head()

new_df = df.groupby([df["State_Name"]=="Maharashatra", df["District_Name"]=="AKOLA", "Crop"]).mean()

def major_crops(state_name, district_name):
    state_name = str.capitalize(state_name)
    district_name = str.upper(district_name)
    
    state_df = df[df["State_Name"]==state_name]
    district_df = state_df[state_df["District_Name"]==district_name]
    df_new = district_df.groupby(by="Crop").mean().sort_values(by="Production", ascending=False).reset_index()
    
    
    return df_new["Crop"].unique()

# crop_list = major_crops("Maharashtra", "Kolhapur")
# crops = crop_list.tolist()

crop_df = pd.read_csv('C://Users//Ratnadeep Gawade//Desktop//python//Machine Learning//Data Set//Projects//Crop Predcition//Crop_Pred.csv')
crop_df.drop('Unnamed: 0', axis=1, inplace=True)

df_2 = pd.DataFrame()

cf = []
for i, crop in enumerate(crops):
    cf.append(crop_df[crop_df["Crop"] == crop])
    df_2 = pd.concat(cf, ignore_index=True)

from sklearn.preprocessing import LabelEncoder

X = df_2.iloc[:, 1:]

y = df_2["Crop"]

label_encoder = LabelEncoder()

y = label_encoder.fit_transform(y)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

min_max_scaler = MinMaxScaler()

scaled_X = min_max_scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(scaled_X, y,
                                                   test_size=0.25,
                                                   shuffle=True,
                                                   random_state=0)


from sklearn.ensemble import RandomForestClassifier
import time
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

X = np.asarray(X)

def predict_crop(artifical_values):
    
    start = time.time()
    if artifical_values in X.tolist():
        artifical_values = np.asarray([artifical_values])
        artifical_values = min_max_scaler.transform(artifical_values)
        model = RandomForestClassifier()
        model.fit(scaled_X, y)
        crops = []
        for i in range(6):
            pred = model.predict(artifical_values)
            crop = label_encoder.inverse_transform(pred)
            print(i, crop[0])
            if crop in crops:
                 pass
            else:
                crops.append(crop[0])
        print(f"The Crop best suitable for your soil is : {[str.upper(i) for i in crops][0]}")
    else:
        print("The values entered are not suitable for any crop in this region.")
    end = time.time()
    print(f"Execution time : {end-start}s")

# predict_crop([80, 40, 40, 5.50])

# def rec():
#     N = int(input("N:"))
#     P = int(input("P:"))
#     K = int(input("K:"))
#     pH = float(input("pH:"))

#     predict_crop([N, P, K, pH])










