import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

########################## Pre-process Dataset from the original dataset #######################

df = pd.read_csv("clean_laliga_playerDF.csv")

player = df[['season','teamName','playerName','position','pass_accura','tackle_blocks','tackle_intercep','fouls_committed']]
player = player[player['season'].isin([2020, 2021, 2022])]
player = player[player['position'] == "Defender"]
player = player[~((player[['pass_accura','tackle_blocks','tackle_intercep','fouls_committed']] == 0).all(axis=1))]
print(player)

########################Using K-means clustering to label categories######################################
X = player[['pass_accura','tackle_blocks','tackle_intercep','fouls_committed']]
scaler = StandardScaler()
scale_X = scaler.fit_transform(X)
k_means_model = KMeans(n_clusters=3)
labels = k_means_model.fit_predict(X)
player["performance"] = labels

def cluster_value(value):
    if value == 2:
        return 'Good'
    elif value == 1:
        return "Normal"
    elif value == 0:
        return "Bad"

player['performance'] =  player['performance'].apply(cluster_value)
player['performance'] = player['performance'].astype('category')

####################### Split dataset to Train set and Test set#################################
playerTrainDF, playerTestDF = train_test_split(player,test_size = 0.3, random_state=42)
disjoint_check = pd.merge(playerTrainDF, playerTestDF, how='inner')

# Check Train and Test sets are disjoint
if not disjoint_check.empty:
    print("Train and Test set have same rows")
else:
    print("Train and Test set have not same rows")

playerTrainDF.to_csv("DTTrainDF.csv")
playerTestDF.to_csv("DTTestDF.csv")
print(playerTrainDF)
print(playerTestDF)
