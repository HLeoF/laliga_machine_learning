import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

playerTrainDF = pd.read_csv("SVMTrainDF.csv")
playerTestDF = pd.read_csv("SVMTestDF.csv")

playerTestLabel = playerTestDF['performance']

playerTestDF = playerTestDF.drop(['performance'],axis = 1)
playerTrainDF_nolabel = playerTrainDF.drop(['performance'],axis = 1)
playerTrainLabel = playerTrainDF['performance']

dropcols = ['season','teamName','playerName','position']
playerTrainDF_nolabel_quant = playerTrainDF_nolabel.drop(dropcols,axis = 1)
playerTestDF_quant = playerTestDF.drop(dropcols,axis=1)

############################# Kernel: Linear ###########################################

svm_model = LinearSVC(C=1.0,random_state=42)
svm_model.fit(playerTrainDF_nolabel_quant,playerTrainLabel)
prediction = svm_model.predict(playerTestDF_quant)
print(accuracy_score(playerTestLabel, prediction))

svm_model2 = LinearSVC(C=1.0,random_state=42)
svm_model2.fit(playerTrainDF_nolabel_quant,playerTrainLabel)
prediction2 = svm_model2.predict(playerTestDF_quant)
print(accuracy_score(playerTestLabel, prediction2))

svm_model3 = LinearSVC(C=50,random_state=42)
svm_model3.fit(playerTrainDF_nolabel_quant,playerTrainLabel)
prediction3 = svm_model3.predict(playerTestDF_quant)
print(accuracy_score(playerTestLabel, prediction3))

linear_cnf_matrix = confusion_matrix(playerTestLabel,prediction)
linear_cnf_matrix2 = confusion_matrix(playerTestLabel,prediction2)
linear_cnf_matrix3 = confusion_matrix(playerTestLabel,prediction3)

fig, axes = plt.subplots(2, 2, figsize=(15, 15))

labels = ['Good','Normal']
sns.heatmap(linear_cnf_matrix, annot=True,cmap='Blues',xticklabels=labels, yticklabels=labels, cbar=False,ax=axes[0,0])
axes[0,0].set_title("LinearSVC Confusion Matrix C=0.01",fontsize=20)
axes[0,0].set_xlabel("Actual", fontsize=15)
axes[0,0].set_ylabel("Predicted", fontsize=15)

sns.heatmap(linear_cnf_matrix2, annot=True,cmap='Blues',xticklabels=labels, yticklabels=labels, cbar=False,ax=axes[0,1])
axes[0,1].set_title("LinearSVC Confusion Matrix C=1.0",fontsize=20)
axes[0,1].set_xlabel("Actual", fontsize=15)
axes[0,1].set_ylabel("Predicted", fontsize=15)

sns.heatmap(linear_cnf_matrix3, annot=True,cmap='Blues',xticklabels=labels, yticklabels=labels, cbar=False,ax=axes[1,0])
axes[1,0].set_title("LinearSVC Confusion Matrix C=50",fontsize=20)
axes[1,0].set_xlabel("Actual", fontsize=15)
axes[1,0].set_ylabel("Predicted", fontsize=15)


############################ Kernel: RBF #########################################

from sklearn.svm import SVC
svm_rbf_model = SVC(C=0.01, kernel='rbf',verbose=False)
svm_rbf_model.fit(playerTrainDF_nolabel_quant,playerTrainLabel)
rbf_prediction = svm_rbf_model.predict(playerTestDF_quant)
print(accuracy_score(playerTestLabel,rbf_prediction))

svm_rbf_model2 = SVC(C=0.015, kernel='rbf',verbose=False)
svm_rbf_model2.fit(playerTrainDF_nolabel_quant,playerTrainLabel)
rbf_prediction2 = svm_rbf_model2.predict(playerTestDF_quant)
print(accuracy_score(playerTestLabel,rbf_prediction2))

svm_rbf_model3 = SVC(C=30, kernel='rbf',verbose=False)
svm_rbf_model3.fit(playerTrainDF_nolabel_quant,playerTrainLabel)
rbf_prediction3 = svm_rbf_model3.predict(playerTestDF_quant)
print(accuracy_score(playerTestLabel,rbf_prediction3))

rbf_cnf_matrix = confusion_matrix(playerTestLabel,rbf_prediction)
rbf_cnf_matrix2 = confusion_matrix(playerTestLabel,rbf_prediction2)
rbf_cnf_matrix3 = confusion_matrix(playerTestLabel,rbf_prediction3)


fig, axes = plt.subplots(2, 2, figsize=(15, 15))

labels = ['Good','Normal']
sns.heatmap(rbf_cnf_matrix, annot=True,cmap='Blues',xticklabels=labels, yticklabels=labels, cbar=False,ax=axes[0,0])
axes[0,0].set_title("rbfSVC Confusion Matrix C=0.01",fontsize=20)
axes[0,0].set_xlabel("Actual", fontsize=15)
axes[0,0].set_ylabel("Predicted", fontsize=15)

sns.heatmap(rbf_cnf_matrix2, annot=True,cmap='Blues',xticklabels=labels, yticklabels=labels, cbar=False,ax=axes[0,1])
axes[0,1].set_title("rbfSVC Confusion Matrix C=0.015",fontsize=20)
axes[0,1].set_xlabel("Actual", fontsize=15)
axes[0,1].set_ylabel("Predicted", fontsize=15)

sns.heatmap(rbf_cnf_matrix3, annot=True,cmap='Blues',xticklabels=labels, yticklabels=labels, cbar=False,ax=axes[1,0])
axes[1,0].set_title("rbfSVC Confusion Matrix C=30",fontsize=20)
axes[1,0].set_xlabel("Actual", fontsize=15)
axes[1,0].set_ylabel("Predicted", fontsize=15)

######################################## Kernel: Polynomial ############################################

svm_poly_model = SVC(C=0.01,kernel='poly',gamma="scale",verbose=False)
svm_poly_model.fit(playerTrainDF_nolabel_quant,playerTrainLabel)
poly_prediction = svm_poly_model.predict(playerTestDF_quant)
print(accuracy_score(playerTestLabel,poly_prediction))

svm_poly_model2 = SVC(C=0.05, kernel='poly',gamma="scale", verbose=False)
svm_poly_model2.fit(playerTrainDF_nolabel_quant,playerTrainLabel)
poly_prediction2 = svm_poly_model2.predict(playerTestDF_quant)
print(accuracy_score(playerTestLabel,poly_prediction2))

svm_poly_model3 = SVC(C=30,kernel='poly',gamma="scale", verbose=False)
svm_poly_model3.fit(playerTrainDF_nolabel_quant,playerTrainLabel)
poly_prediction3 = svm_poly_model3.predict(playerTestDF_quant)
print(accuracy_score(playerTestLabel,poly_prediction3))

poly_cnf_matrix = confusion_matrix(playerTestLabel,poly_prediction)
poly_cnf_matrix2 = confusion_matrix(playerTestLabel,poly_prediction2)
poly_cnf_matrix3 = confusion_matrix(playerTestLabel,poly_prediction3)


fig, axes = plt.subplots(2, 2, figsize=(15, 15))

labels = ['Good','Normal']
sns.heatmap(poly_cnf_matrix, annot=True,cmap='Blues',xticklabels=labels, yticklabels=labels, cbar=False,ax=axes[0,0])
axes[0,0].set_title("PolySVC Confusion Matrix C=0.01",fontsize=20)
axes[0,0].set_xlabel("Actual", fontsize=15)
axes[0,0].set_ylabel("Predicted", fontsize=15)

sns.heatmap(poly_cnf_matrix2, annot=True,cmap='Blues',xticklabels=labels, yticklabels=labels, cbar=False,ax=axes[0,1])
axes[0,1].set_title("PolySVC Confusion Matrix C=0.05",fontsize=20)
axes[0,1].set_xlabel("Actual", fontsize=15)
axes[0,1].set_ylabel("Predicted", fontsize=15)

sns.heatmap(poly_cnf_matrix3, annot=True,cmap='Blues',xticklabels=labels, yticklabels=labels, cbar=False,ax=axes[1,0])
axes[1,0].set_title("PolySVC Confusion Matrix C=30",fontsize=20)
axes[1,0].set_xlabel("Actual", fontsize=15)
axes[1,0].set_ylabel("Predicted", fontsize=15)

######################################### SVM Visualization ##########################################

pca = PCA(n_components=2)
X = pca.fit_transform(playerTrainDF_nolabel_quant)
Y = pca.fit_transform(playerTestDF_quant)

linear_model = LinearSVC(C=20)
linear_model.fit(X, playerTrainLabel)
linear_prediction = linear_model.predict(Y)
print(accuracy_score(playerTestLabel, linear_prediction))


def plot_svm(model, X, y):
    plt.figure(figsize=(10, 6))

    plt.scatter(X[:, 0], X[:, 1], c=playerTrainLabel.map({'Good': 'blue', 'Normal': 'red'}), s=30, edgecolors='k')
    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    xx = np.linspace(xlim[0], xlim[1], 100)
    yy = np.linspace(ylim[0], ylim[1], 100)
    YY, XX = np.meshgrid(yy, xx)
    xy = np.vstack([XX.ravel(), YY.ravel()]).T
    Z = model.decision_function(xy).reshape(XX.shape)

    # Decision boundary
    ax.contour(XX, YY, Z, colors='green', levels=[-1, 0, 1], alpha=0.5, linestyles=['-', '--', '-'])

    plt.title("SVM Viusalization Example (Linear)")
    plt.xlabel("Rating")
    plt.ylabel("Key Pass")
    plt.show()


plot_svm(linear_model, X, playerTrainLabel.values)

########################### Midfielder predictions result show in dataset ############################
temp = pd.DataFrame(poly_prediction3)
temp = temp.rename(columns={0:'label'})
temp3 = playerTestDF.reset_index()
temp3 = temp3.drop(['index'],axis=1)
merged_df = pd.merge(temp3, temp, left_index=True, right_index=True)
merged_df

club = pd.read_csv("Clubs_DF.csv")
club = club[['season','teamName','PTS']]
club = club.drop_duplicates()
merged_df = pd.merge(merged_df, club, on=['season','teamName'],how='left')
temp4 = merged_df.sort_values(by=['season', 'PTS'], ascending=[True, False])
temp4 = temp4[['season','teamName','playerName','label','PTS']]