import pandas as pd
from sklearn.cluster import  KMeans
import matplotlib.pyplot as plt

cate = pd.read_csv("/content/text.csv")

cate.head(5)

X = cate[["Height","Weight","Width"]]
model = KMeans(n_clusters=3)
label = model.fit_predict(X)
cate['label'] = label

plt.scatter(cate["Height"], cate["Weight"], c=cate["label"], cmap='viridis')
plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], marker='*', c='red', s=200)
plt.title('K-Means Clustering with Centers')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.show()

