import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

########################## Pre-process Dataset from the original dataset #######################

df = pd.read_csv("clean_laliga_playerDF.csv")


df['duel_success_rate'] = df['duel_won'] / df['duel_total']
df['dribble_success_rate'] = df['dribble_success'] / df['dribble_attemp']
player = df[['season', 'teamName', 'playerName', 'position', 'rating',
             'game_minutes', 'duel_success_rate', 'dribble_success_rate',
             'key_pass', 'pass_accura', 'fouls_drawn']]
player = player[player['season'].isin([2020, 2021, 2022])]
player = player[player['position'] == "Midfielder"]
player = player.dropna()


print(player)

########################Using K-means clustering to label categories######################################

X = player[['rating','game_minutes','duel_success_rate', 'dribble_success_rate','key_pass', 'pass_accura', 'fouls_drawn']]
scaler = StandardScaler()
scale_X = scaler.fit_transform(X)
k_means_model = KMeans(n_clusters=2)
labels = k_means_model.fit_predict(X)
player["performance"] = labels


def cluster_value(value):
    if value == 0:
        return 'Good'
    elif value == 1:
        return "Normal"

player['performance'] =  player['performance'].apply(cluster_value)
player['performance'] = player['performance'].astype('category')

print(player)

####################### Split dataset to Train set and Test set#################################
playerTrainDF, playerTestDF = train_test_split(player,test_size = 0.3, random_state=42)
disjoint_check = pd.merge(playerTrainDF, playerTestDF, how='inner')

# Check Train and Test sets are disjoint
if not disjoint_check.empty:
    print("Train and Test set have same rows")
else:
    print("Train and Test set have not same rows")

playerTrainDF.to_csv("SVMTrainDF.csv")
playerTestDF.to_csv("SVMTestDF.csv")
print(playerTrainDF)
print(playerTestDF)