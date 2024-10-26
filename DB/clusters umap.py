
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from umap import UMAP
import os

project_path: str = 'c:/Users/ASUS/OneDrive/CODES/nodeJS/tg-web-app-react-backend/DB'

# Visualize the 2D space of the new features
def save_png(X_umap, Y_pred):
    fig, ax = plt.subplots()
    ax.scatter(X_umap[:, 0], X_umap[:, 1], c=np.array(Y_pred))
    ax.set_xlabel('umap Component 1')
    ax.set_ylabel('umap Component 2')
    plt.savefig(f'{project_path}/umap.png')


def clusterize(data):
    maxNumOfClusters = int(data.shape[0] / 2)
    optimalNumOfClusters = 1
    if maxNumOfClusters > 1:
        startError = KMeans(n_clusters=1).fit(data).inertia_
        for i in range(2, maxNumOfClusters):
            if KMeans(n_clusters=i).fit(data).inertia_ < startError / 2:
                optimalNumOfClusters = i
                break
        print(optimalNumOfClusters)
    kmeans = KMeans(n_clusters=optimalNumOfClusters).fit(data)

    # Получение значений классов после кластеризации
    Y_pred = kmeans.labels_

    return Y_pred


def read_data():
    data = pd.read_json(f'{project_path}/data100.json').values.transpose()
    if data is None:
        print('error: no data')
        exit()

    return data


if __name__ == '__main__':
    if os.path.exists(f'{project_path}/X_umap.json'):
        X_umap = np.load(f'{project_path}/X_umap.json')
    else:
        data = read_data()
        Y_pred = clusterize(data)
        X_umap = UMAP().fit_transform(data)
        np.save(f'{project_path}/X_umap.json', X_umap)
        save_png(X_umap, Y_pred)
