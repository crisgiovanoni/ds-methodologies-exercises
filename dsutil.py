#Standard Imports
import pandas as pd
import matplotlib.pyplot as plt

#Scikit Learn Imports
from sklearn.cluster import KMeans


def plot_elbow(df, range_size=10):

    k_values = []
    inertias = []

    for k in range(1,range_size):
        kmeans = KMeans(n_clusters=k).fit(df)
        inertias.append(kmeans.inertia_)
        k_values.append(k)

    plt.plot(k_values, inertias, marker='x')
    plt.xlabel('K')
    plt.ylabel('inertia')