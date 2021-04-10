#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

from sklearn.model_selection import train_test_split, KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.preprocessing import Normalizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import export_graphviz
from sklearn.model_selection import GridSearchCV
from tqdm.notebook import tqdm_notebook as tqdm


warnings.simplefilter(action="ignore")

df = pd.read_csv("C://Users//Ratnadeep Gawade//Desktop//python//Machine Learning//Data Set//Projects//Crop Predcition//FertPredictDataset.csv")

drop = ["Ca", "Mg", "S", "Lime", "C", "Moisture"]
df.drop(drop, axis=1, inplace=True)

df.head()

df.info()

df.describe()

X = df.iloc[:, :-1]
y = df.iloc[:, -1]
X.head(), y.head()

dtree_model = tree.DecisionTreeClassifier(criterion="entropy", max_depth=3)
dtree_model.fit(X, y)

K = input("K:")
N = input("N:")
P = input("P:")
fertilizer_value = [float(K), float(N), float(P)]
print(fertilizer_value)
fertilizer_value = np.asarray([fertilizer_value])

y_pred = dtree_model.predict(fertilizer_value)
print(f"The best Fertilizer best for your soil is class : {y_pred[0]}")

X_train, X_test, y_train, y_test = train_test_split(X,y,
	test_size=0.2,
	random_state=0,
	shuffle=True)
X_train = np.asarray(X_train)
X_test = np.asarray(X_test)

y_train = np.asarray(y_train)
y_test = np.asarray(y_test)

scalar = Normalizer().fit(X_train)
normalized_X_train =  scalar.transform(X_train)
normalized_X_test = scalar.transform(X_test)

# print(normalized_X_train)

feature_names = df.columns.tolist()
feature_names

new_df_for_plot = pd.DataFrame(data=np.c_[normalized_X_train,y_train],
	columns=feature_names)
new_df_for_plot.head()

sns.pairplot(data=new_df_for_plot, hue="class")
sns.color_palette("coolwarm", as_cmap=True)
sns.set_style("white")
plt.show()

K=3
knn_model = KNeighborsClassifier(3)
knn_model.fit(normalized_X_train, y_train)
y_pred = knn_model.predict(normalized_X_test)

print(f"Accuracy is: {accuracy_score(y_test, y_pred)*100}%")






