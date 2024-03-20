import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

clustering_df = pd.read_csv("../NB/Clubs_DF.csv")

######################### K-Means Clustering ##############

X = clustering_df[['shots_total','shots_on','goals_total']]
scaler = StandardScaler()
scale_X = scaler.fit_transform(X)

######################### K Value Selection ###############
wcss = []
score = [0.0]

#### Elbow Method #########################################
for i in range(1, 11):
  model = KMeans(n_clusters=i)
  labels = model.fit_predict(X)
  wcss.append(model.inertia_)

########## Silhouette Method #############################
for i in range(2, 11):
  model = KMeans(n_clusters=i)
  labels = model.fit_predict(X)
  scores = silhouette_score(X,model.labels_)
  score.append(scores)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(range(1, 11), wcss, marker='o')
ax1.axvline(x=3, color='r', linestyle='--')
ax1.set_xlabel('Number of clusters K')
ax1.set_ylabel('WCSS')
ax1.set_title('Elbow Method')

ax2.plot(range(1, 11), score, marker='o')
ax2.axvline(x=2, color='r', linestyle='--')
ax2.set_xlabel('Number of clusters K')
ax2.set_ylabel('Silhouette Score')
ax2.set_title('Silhouette Method')

plt.tight_layout()
plt.show()

############# K-Mean Visualization ###########################
df2 = clustering_df.copy()
model2 = KMeans(n_clusters=2)
labels2 = model2.fit_predict(X)
df2["cluster"] = labels2

df3 = clustering_df.copy()
model3 = KMeans(n_clusters=3)
labels3 = model3.fit_predict(X)
df3["cluster"] = labels3

df4 = clustering_df.copy()
model4 = KMeans(n_clusters=4)
labels4 = model4.fit_predict(X)
df4["cluster"] = labels4

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
plot1 = ax1.scatter(df2['shots_total'],df2['shots_on'],c = df2['cluster'])

ax1.set_xlabel("Shots Total")
ax1.set_ylabel("Shots On")
ax1.legend()
ax1.set_title("K Value = 2 & Silhouette Method")

ax2.scatter(df3['shots_total'],df3['shots_on'],c = df3['cluster'])
ax2.set_xlabel("Shots Total")
ax2.set_ylabel("Shots On")
ax2.set_title("K Value = 3 & Elbow Method")

ax3.scatter(df4['shots_total'],df4['shots_on'],c = df4['cluster'])
ax3.set_xlabel("Shots Total")
ax3.set_ylabel("Shots On")
ax3.set_title("K Value = 4 & Random Picking")

plt.tight_layout()
plt.show()

########################## Data Exploring After Clustering #############################

df2.drop(columns=['Unnamed: 0'], inplace=True)
df3.drop(columns=['Unnamed: 0'], inplace=True)
df4.drop(columns=['Unnamed: 0'], inplace=True)

temp1 = df2[['season','teamName','PTS','cluster']]
temp1 = temp1.pivot_table(index=['season', 'teamName','PTS'], columns='cluster', aggfunc='size', fill_value=0).reset_index()
import seaborn as sns
temp1 = temp1[temp1['season'] == 2020]
temp1 = temp1.sort_values(by='PTS',ascending=False)

temp2 = df3[['season','teamName','PTS','cluster']]
temp2 = temp2.pivot_table(index=['season', 'teamName','PTS'], columns='cluster', aggfunc='size', fill_value=0).reset_index()
import seaborn as sns
temp2 = temp2[temp2['season'] == 2020]
temp2 = temp2.sort_values(by='PTS',ascending=False)

temp3 = df4[['season','teamName','PTS','cluster']]
temp3 = temp3.pivot_table(index=['season', 'teamName','PTS'], columns='cluster', aggfunc='size', fill_value=0).reset_index()
import seaborn as sns
temp3 = temp3[temp3['season'] == 2020]
temp3 = temp3.sort_values(by='PTS',ascending=False)

fig, axes = plt.subplots(1, 3, figsize=(20, 5))

axes[0].bar(temp1['teamName'], temp1[0], label='Cluster 0', color='#CAB91E')
axes[0].bar(temp1['teamName'], temp1[1], bottom=temp1[0], label='Cluster 1', color='#360143')
axes[0].legend()
axes[0].set_ylabel("Number")
axes[0].set_xlabel("PTS(High-->Low)")
axes[0].set_title("2020 Season - 2 Clusters")
axes[0].tick_params(axis='x', rotation=90)


axes[1].bar(temp2['teamName'], temp2[0], label='Cluster 0', color='#360143')
axes[1].bar(temp2['teamName'], temp2[1], bottom=temp2[0], label='Cluster 1', color='#1A7470')
axes[1].bar(temp2['teamName'], temp2[2], bottom=temp2[0] + temp2[1], label='Cluster 2', color='#CAB91E')
axes[1].legend()
axes[1].set_ylabel("Number")
axes[1].set_xlabel("PTS(High-->Low)")
axes[1].set_title("2020 Season - 3 Clusters")
axes[1].tick_params(axis='x', rotation=90)


axes[2].bar(temp3['teamName'], temp3[0], label='Cluster 0', color='#275372')
axes[2].bar(temp3['teamName'], temp3[1], bottom=temp3[0], label='Cluster 1', color='#2A9261')
axes[2].bar(temp3['teamName'], temp3[2], bottom=temp3[0] + temp3[1], label='Cluster 2', color='#CAB91E')
axes[2].bar(temp3['teamName'], temp3[3], bottom=temp3[0] + temp3[1] + temp3[2], label='Cluster 3', color='#360143')
axes[2].legend()
axes[2].set_ylabel("Number")
axes[2].set_xlabel("PTS(High-->Low)")
axes[2].set_title("2020 Season - 4 Clusters")
axes[2].tick_params(axis='x', rotation=90)

plt.show()