import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

X,y=make_blobs(n_samples=400,centers=4,random_state=0)
kmeans=KMeans(n_clusters=4,random_state=0)
kmeans.fit(X)
labels=kmeans.labels_


plt.scatter(X[:,0],X[:,1],c=labels,cmap="viridis")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Clustering Data")
plt.colorbar(label="Cluster Label")
plt.show()
