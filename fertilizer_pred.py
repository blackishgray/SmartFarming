import numpy as np
import pandas as pd
import fertilizer_reccomendation as fr 

df = pd.read_csv("C://Users//Ratnadeep Gawade//Desktop//python//Machine Learning//Data Set//Projects//Crop Predcition//fertilizer.csv")
df.drop("Unnamed: 0", axis=1, inplace=True)

list_for_crops = []
list3 = df["Crop"].tolist()
for i in range(len(list3)):
	list_for_crops.append(str.lower(list3[i]))
	list_for_crops    
	df["Crop"] = pd.Series(data=list_for_crops)

def compute_values(args):

	ip = []
	for i in args:
		ip.append(i)

    nr = int(df[df["Crop"] == ip[0]]["N"][df[df["Crop"] == ip[0]].index[0]])
    pr = int(df[df["Crop"] == ip[0]]["P"][df[df["Crop"] == ip[0]].index[0]])
    kr = int(df[df["Crop"] == ip[0]]["K"][df[df["Crop"] == ip[0]].index[0]])
    pHr = float(df[df["Crop"] == ip[0]]["pH"][df[df["Crop"] == ip[0]].index[0]])
        
    dataset_values_of_NPKpH = [nr, pr, kr, pHr]

        # dict_for_NPK = {"N":N, "P":P, "K":K, "pH":pH} #10, #0  #10

    ip = list(args.values())
    keys_for_rec = ["NHigh", "NLow", "PHigh", "PLow", "KHigh", "KLow"]
        
        ##Recommendation for Nitrogen values
        #10 < 20
    if ip[0] > nr : 
    	nrec = fr.fertilizer_dic["NHigh"]
    elif ip[0] == nr:
        nrec = f"\tNitrogen values of your soil is prefect for {Crop}"
    else:
        nrec = fr.fertilizer_dic["NLow"]

        	print("\n")
        	print("\t=========================================================")
        	print("\n")

        #Recommendation for Phosphorous Values
        #0 == 0
    if ip[1] > pr : 
    	prec = fr.fertilizer_dic["PHigh"]
    elif ip[1] == pr:
    	prec = f"\tPhosphorous values of your soil is prefect for {Crop}"
    else:
    	prec = fr.fertilizer_dic["PLow"]

        	print("\n")
        	print("\th=========================================================")

        #Recommendation for Potassium Values
        #10 < 30
    if ip[2] > kr : 
    	krec = fr.fertilizer_dic["KHigh"]
    elif ip[2] == kr:
    	krec = f"\tPotassium values of your soil is prefect for {Crop}"
    else:  
     	krec = fr.fertilizer_dic["KLow"]

        	print("\n")    
        	print("\th=========================================================")

        #Recommendation for pH Values
    if ip[3] > pHr : 
    	pHrec = fr.fertilizer_dic["pHHigh"]
    elif ip[3] == pHr:
    	pHrec = f"\tPotassium values of your soil is prefect for {Crop}"
    else: 
    	pHrec = fr.fertilizer_dic["pHLow"]
     reccomendations = [nrec, prec, krec, pHrec]

    return reccomendations