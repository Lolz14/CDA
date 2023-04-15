from sklearn.cluster import KMeans,AgglomerativeClustering
from matplotlib import pyplot as plt
import numpy as np

"""
np.random.seed(123)

X = np.zeros((100,2))

X[:50,0] = np.random.randn(50) + 5
X[:50,1] = np.random.randn(50) + 5

X[50:,0] = np.random.randn(50) - 5
X[50:,1] = np.random.randn(50) - 5

kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(X)
labels = kmeans.labels_

plt.figure()
plt.scatter(X[:50,0],X[:50,1])
plt.scatter(X[50:,0],X[50:,1])

plt.figure()
plt.scatter(X[labels == 0,0],X[labels == 0,1])
plt.scatter(X[labels == 1,0],X[labels == 1,1])
plt.show()
"""

np.random.seed(123)

X = np.zeros((100,2))

X[:50,0] = np.random.randn(50) + 5
X[:50,1] = np.random.randn(50) + 5

X[50:,0] = np.random.randn(50) - 5
X[50:,1] = np.random.randn(50) - 5

algs = [KMeans(),AgglomerativeClustering()]
ps = [{'n_clusters': 2,'random_state': 0,'n_init': "auto"},{'n_clusters': 2}]

def cluster(data,algs,ps):
	n = data.shape[0]
	k = len(algs)
	ans = np.zeros((k,n))
	for i,alg in enumerate(algs):
		p = ps[i]
		model = alg
		model.set_params(**p)
		model.fit(data)
		ans[i,:] = model.labels_
	return ans


test = cluster(X,algs,ps)

print(test[0,:])
print(test[1,:])


