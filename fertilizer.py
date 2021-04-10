#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import os
import sys
import fertilizer_rec as fr
from flask import  request

df = pd.read_csv("C://Users//Ratnadeep Gawade//Desktop//python//Machine Learning//Data Set//Projects//Crop Predcition//fertilizer.csv")
# df.head()

# df.info()

# df.columns

df.drop("Unnamed: 0", axis=1, inplace=True)

# df.head()

list_for_crops = []
list3 = df["Crop"].tolist()
for i in range(len(list3)):
    list_for_crops.append(str.lower(list3[i]))
list_for_crops    
df["Crop"] = pd.Series(data=list_for_crops)

# df["Crop"].unique()

class pred_fert_reco():

    
    def compute_values(self):
        
        def __init__(self):
            pass
        
        global Crop
        global nr
        global pr
        global kr
        global pHr

        Crop = str.lower(input("Enter the crop you want to grow: "))
        N = int(input("Enter the Nitrogen value of your soil:")) #10
        P = int(input("Enter the Phosphorous value of your soil:")) #20
        K = int(input("Enter the Potassium value of your soil:")) #40
        pH = float(input("Enter the pH value of your soil:"))

        # Crop = str(request.form['crop-value'])
        # N = int(request.form["n-value"]) #10
        # P = int(request.form['p-value']) #20
        # K = int(request.form['k-value']) #40
        # pH = float(request.form['pH-value'])

        ip = [Crop, N, P, K]

        nr = int( df[df["Crop"] == ip[0]]["N"][df[df["Crop"] == ip[0]].index[0]]) #20
        pr = int(df[df["Crop"] == ip[0]]["P"][df[df["Crop"] == ip[0]].index[0]]) #20
        kr = int(df[df["Crop"] == ip[0]]["K"][df[df["Crop"] == ip[0]].index[0]]) #30
        pHr = float(df[df["Crop"] == ip[0]]["pH"][df[df["Crop"] == ip[0]].index[0]]) #30
        
        dataset_values_of_NPKpH = [nr, pr, kr, pHr]

        dict_for_NPK = {"N":N, "P":P, "K":K, "pH":pH} #10, #0  #10
        # print("The Output of this function tells us the difference between the N, P, K values of the soil and the Crop that you wish to produce in a form of a dictionary.")
        # print(dict_for_NPK)
        
        #Values In datasrt coressponding to the crop
        # print(nr, pr, kr, pHr)
        
        return dict_for_NPK
    
    def fert_sol(self, args):
        
        def __init__(self):
            pass
        
        v = list(args.values())
        keys_for_rec = ["NHigh", "NLow", "PHigh", "PLow", "KHigh", "KLow"]
        # print(v)
        
        
        ##Recommendation for Nitrogen values
        #10 < 20
        if v[0] > nr : 
            print(fr.fertilizer_dic["NHigh"])
        elif v[0] == nr:
            print(f"\tNitrogen values of your soil is prefect for {Crop}")
        else:
            print(fr.fertilizer_dic["NLow"])
            
        print("\n")
        print("\t=========================================================")
        print("\n")
        
        #Recommendation for Phosphorous Values
        #0 == 0
        if v[1] > pr : 
            print(fr.fertilizer_dic["PHigh"])
        elif v[1] == pr:
            print(f"\tPhosphorous values of your soil is prefect for {Crop}")
        else:
            print(fr.fertilizer_dic["PLow"])
        print("\n")
        print("\th=========================================================")
                
        #Recommendation for Potassium Values
        #10 < 30
        if v[2] > kr : 
            print(fr.fertilizer_dic["KHigh"])
        elif v[2] == kr:
            print(f"\tPotassium values of your soil is prefect for {Crop}")
        else: #v[2] ==-10 < kr==30
            print(fr.fertilizer_dic["KLow"])
        
        print("\n")    
        print("\th=========================================================")
        
        #Recommendation for pH Values
        if v[3] > pHr : 
            print(fr.fertilizer_dic["pHHigh"])
        elif v[3] == pHr:
            print(f"\tPotassium values of your soil is prefect for {Crop}")
        else: #v[2] ==-10 < kr==30
            print(fr.fertilizer_dic["pHLow"])

obj1 = pred_fert_reco()

dict1 = obj1.compute_values()
#N=10, P=20, K=40

rec = obj1.fert_sol(dict1)






