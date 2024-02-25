import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

clustering_df = pd.read_csv("clustering_analysis_df.csv")

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

ax1.scatter(df2['shots_total'],df2['shots_on'],c = df2['cluster'])
ax1.set_xlabel("Shots Total")
ax1.set_ylabel("Shots On")
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