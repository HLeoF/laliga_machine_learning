import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

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



################# NB Discover ###################################################

labels = ['Good','Normal','Bad']
sns.heatmap(cnf_matrix, annot=True,cmap='Blues',xticklabels=labels, yticklabels=labels, cbar=False)
plt.title("Confusion Matrix",fontsize=20)
plt.xlabel("Actual", fontsize=15)
plt.ylabel("Predicted", fontsize=15)


prob_matrix = np.round(model.predict_proba(playerTestDF_quant),2)
plt.figure(figsize=(15, 15))
sns.heatmap(prob_matrix, annot=True,cmap='Blues',xticklabels=labels, cbar=False)
plt.title("Model Prediction Probability",fontsize=20)
plt.xlabel("Labels", fontsize=15)

temp = pd.DataFrame(prediction)
temp1 = pd.DataFrame(playerTestLabel)
def lables(value):
    if value == "Good":
        return 3
    elif value == "Normal":
        return 2
    elif value == "Bad":
        return 1
temp = temp.rename(columns={0:'label'})
temp1 = temp1.rename(columns={0:'label'})

temp['val'] = temp['label'].apply(lables)

temp1['val'] = temp1['label'].apply(lables)


sns.lineplot(x=temp.index, y=temp['val'], alpha=0.5, label='Prediction')
sns.lineplot(x=temp.index, y=temp1['val'], alpha=0.5, label='Test')

plt.title('Test Label vs. Prediction Label')
plt.xlabel('Index')
plt.ylabel('Labels(1:Bad, 2: Nomral, 3: Good)')

plt.yticks([1,2,3])

plt.legend()
plt.show()

accuracy = accuracy_score(playerTestLabel, prediction)
print(accuracy)

#### Attacker Preformance Discover ##############################
temp3 = playerTestDF.reset_index()
temp3 = temp3.drop(['index'],axis=1)
merged_df = pd.merge(temp3, temp, left_index=True, right_index=True)
merged_df = merged_df.iloc[:, 0:14]
club = pd.read_csv("/content/clustering_analysis_df.csv")
club = club[['season','teamName','PTS']]
club = club.drop_duplicates()
merged_df = pd.merge(merged_df, club, on=['season','teamName'],how='left')
temp4 = merged_df.sort_values(by=['season', 'PTS'], ascending=[True, False])
temp4 = temp4[['season','teamName','playerName','label','PTS']]
temp4.head(15)

temp4.to_csv('Predition_player_results.csv')

print(temp4.head(15))