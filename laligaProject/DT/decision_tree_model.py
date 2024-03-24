import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import graphviz

playerTrainDF = pd.read_csv("DTTrainDF.csv")
playerTestDF = pd.read_csv("DTTestDF.csv")

playerTestLabel = playerTestDF['performance']

playerTestDF = playerTestDF.drop(['performance'],axis = 1)
playerTrainDF_nolabel = playerTrainDF.drop(['performance'],axis = 1)
playerTrainLabel = playerTrainDF['performance']

dropcols = ['season','teamName','playerName','position']
playerTrainDF_nolabel_quant = playerTrainDF_nolabel.drop(dropcols,axis = 1)
playerTestDF_quant = playerTestDF.drop(dropcols,axis=1)


############ Tree 1: Gini & Best ################################

model = DecisionTreeClassifier(criterion='gini', splitter='best', max_depth=None,
                  min_samples_split=2, min_samples_leaf=1,
                  min_weight_fraction_leaf=0.0,
                  max_features=None, random_state=42,
                  max_leaf_nodes=None, min_impurity_decrease=0.0,
                  class_weight=None, ccp_alpha=0.0)

model.fit(playerTrainDF_nolabel_quant,playerTrainLabel)

TREE_Vis = tree.export_graphviz(model,
                    out_file=None,
                    feature_names=playerTrainDF_nolabel_quant.columns,
                    class_names=["Good", "Normal", "Bad"],
                    filled=True, rounded=True,
                    special_characters=True)

graph = graphviz.Source(TREE_Vis)
graph

predictions = model.predict(playerTestDF_quant)
conf_matrix = confusion_matrix(playerTestLabel, predictions)
accuracy = accuracy_score(playerTestLabel, predictions)
print(accuracy)


labels = ['Good','Normal','Bad']
sns.heatmap(conf_matrix, annot=True,cmap='Blues',xticklabels=labels, yticklabels=labels, cbar=False)
plt.title("Confusion Matrix",fontsize=20)
plt.xlabel("Actual", fontsize=15)
plt.ylabel("Predicted", fontsize=15)
plt.show()

################## Tree plot 2 Entropy & Best splitter ######################

model2 = DecisionTreeClassifier(criterion='entropy',splitter='best',max_depth=None,
                  min_samples_split=2, min_samples_leaf=1,
                  min_weight_fraction_leaf=0.0,
                  max_features=None, random_state=42,
                  max_leaf_nodes=None, min_impurity_decrease=0.0,
                  class_weight=None, ccp_alpha=0.0)

model2.fit(playerTrainDF_nolabel_quant,playerTrainLabel)
TREE_Vis = tree.export_graphviz(model2,
                    out_file=None,
                    feature_names=playerTrainDF_nolabel_quant.columns,
                    class_names=["Good", "Normal", "Bad"],
                    filled=True, rounded=True,
                    special_characters=True)
graph = graphviz.Source(TREE_Vis)
graph

predictions2 = model2.predict(playerTestDF_quant)
conf_matrix2 = confusion_matrix(playerTestLabel, predictions2)
accuracy2 = accuracy_score(playerTestLabel, predictions2)
print(conf_matrix2)
print(accuracy2)

sns.heatmap(conf_matrix2, annot=True,cmap='Blues',xticklabels=labels, yticklabels=labels, cbar=False)
plt.title("Confusion Matrix",fontsize=20)
plt.xlabel("Actual", fontsize=15)
plt.ylabel("Predicted", fontsize=15)
plt.show()

######################### Tree Plot 3 Gini and random splitter #########################

model3 = DecisionTreeClassifier(criterion='gini',splitter='random',max_depth=None,
                  min_samples_split=2, min_samples_leaf=1,
                  min_weight_fraction_leaf=0.0,
                  max_features=None, random_state=42,
                  max_leaf_nodes=None, min_impurity_decrease=0.0,
                  class_weight=None, ccp_alpha=0.0)
model3.fit(playerTrainDF_nolabel_quant,playerTrainLabel)
TREE_Vis = tree.export_graphviz(model3,
                    out_file=None,
                    feature_names=playerTrainDF_nolabel_quant.columns,
                    class_names=["Good", "Normal", "Bad"],
                    filled=True, rounded=True,
                    special_characters=True)
graph = graphviz.Source(TREE_Vis)
graph

predictions3 = model3.predict(playerTestDF_quant)
conf_matrix3 = confusion_matrix(playerTestLabel, predictions3)
accuracy3 = accuracy_score(playerTestLabel, predictions3)
print(conf_matrix3)
print(accuracy3)

sns.heatmap(conf_matrix3, annot=True,cmap='Blues',xticklabels=labels, yticklabels=labels, cbar=False)
plt.title("Confusion Matrix",fontsize=20)
plt.xlabel("Actual", fontsize=15)
plt.ylabel("Predicted", fontsize=15)
plt.show()
