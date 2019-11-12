import pandas as pd
from pydataset import data
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




iris = data("iris")
#Is 4 the optimal number? Try different values of k and visualize your results.


#Perform clustering with sepal length, sepal width, and petal length. Use a k of 4.
X = iris[["Sepal.Length","Sepal.Width","Petal.Length"]]

kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

centers = pd.DataFrame(kmeans.cluster_centers_,columns=X.columns)
centers

#Create a 3d visualization that shows your clusters along with the features specified above?
fig = plt.figure(figsize=(9, 7))
ax = Axes3D(fig)

ax.scatter(X["Sepal.Length"],X["Sepal.Width"],X["Petal.Length"], c=kmeans.labels_)
ax.scatter(centers["Sepal.Length"], centers["Sepal.Width"], centers["Petal.Length"], c='pink', s=10000, alpha=.4)
ax.set(xlabel='sepal_length', ylabel='sepal_width', zlabel='petal_length')
plt.show()

#See the most optimal number of k's.

k_values = []
inertias = []

for k in range(1, 10):
    kmeans = KMeans(n_clusters=k).fit(X)
    inertias.append(kmeans.inertia_)
    k_values.append(k)

plt.plot(k_values, inertias, marker='x')
plt.xlabel('K')
plt.ylabel('inertia')

kmeans.inertia_

df['cluster'] = kmeans.predict(X)

df.cluster = 'cluster_' + df.cluster.astype('str')

plt.figure(figsize=(10, 4))

plt.subplot(121)

for v in df.species.unique():
    iris = df[df.species == v]
    plt.scatter(iris.petal_length, iris.petal_width, label=v)

plt.legend()
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Petal Length and Width By Species')

plt.subplot(122)

for v in df.cluster.unique():
    iris = df[df.cluster == v]
    plt.scatter(iris.petal_length, iris.petal_width, label=v)

plt.legend()
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Petal Length and Width By Cluster')


# Create 3D viz showing centers and data points for running kmeans with 4 clusters.

fig = plt.figure(figsize=(12,9))
ax = Axes3D(fig)

ax.scatter(df.sepal_length, df.petal_length, df.petal_width, c=kmeans.labels_)
ax.scatter(centers.sepal_length, centers.petal_length, centers.petal_width, c="pink", s=10000, alpha=.4)

ax.set(xlabel='sepal_length', ylabel='petal_length', zlabel='petal_width')