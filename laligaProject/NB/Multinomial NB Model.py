import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix


player = pd.read_csv("label_clean_DF.csv")

playerTrainDF, playerTestDF = train_test_split(player,test_size = 0.3)
playerTestLabel = playerTestDF['label']

playerTestDF = playerTestDF.drop(["label"],axis = 1)
playerTrainDF_nolabel = playerTrainDF.drop(["label"],axis = 1)
playerTrainLabel = playerTrainDF['label']

dropcols = ['season','teamName','playerName','position']
playerTrainDF_nolabel_quant = playerTrainDF_nolabel.drop(dropcols,axis = 1)
playerTestDF_quant = playerTestDF.drop(dropcols,axis=1)

model = MultinomialNB()
model.fit(playerTrainDF_nolabel_quant,playerTrainLabel)

prediction = model.predict(playerTestDF_quant)

cnf_matrix = confusion_matrix(playerTestLabel, prediction)
print("\nThe confusion matrix is:")
print(cnf_matrix)

print(np.round(model.predict_proba(playerTestDF_quant),2))