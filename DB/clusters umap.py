
import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
from sklearn.cluster import KMeans
from umap import UMAP
import os

project_path: str = '.'

# Visualize the 2D space of the new features
def save_png(X_umap, Y_pred, id_user: int = 0):
    fig, ax = plt.subplots()
    ax.scatter(X_umap[:, 0], X_umap[:, 1], c=np.array(Y_pred))
    ax.set_xlabel('umap Component 1')
    ax.set_ylabel('umap Component 2')
    user_x, user_y = X_umap[id_user, 0], X_umap[id_user, 1]
    ax.scatter(user_x, user_y, c='white', s=25)
    ax.annotate('you', (user_x, user_y), textcoords="offset points", xytext=(0,10), ha='center')
    plt.savefig(f'{project_path}/umap.png')


def clusterize(data: np.ndarray, id_user: int = 0) -> np.ndarray:
    maxNumOfClusters = int(data.shape[0] / 2)
    optimalNumOfClusters = 1
    if maxNumOfClusters > 1:
        startError = KMeans(n_clusters=1).fit(data).inertia_
        for i in range(2, maxNumOfClusters):
            if KMeans(n_clusters=i).fit(data).inertia_ < startError / 2:
                optimalNumOfClusters = i
                break
        print(f"Optimal number of clusters: {optimalNumOfClusters}")
    kmeans = KMeans(n_clusters=optimalNumOfClusters).fit(data)

    # Получение значений классов после кластеризации
    Y_pred = kmeans.labels_
    user_cluster = Y_pred[id_user]
    same_cluster_ids = [idx for idx, label in enumerate(Y_pred) if label == user_cluster and idx != id_user]
    print(f"IDs in the same cluster as user {id_user}: {same_cluster_ids}")

    return Y_pred


def read_data() -> np.ndarray:
    import json

    # Load the JSON data from the file. 17 features
    with open(f'{project_path}/users.json') as file:
        database = json.load(file)

    data = [user['interests_values'] for user in database]
    # data = pd.read_json(f'{project_path}/data100.json').values.transpose()
    if data is None:
        print('error: no data')
        exit()

    return np.array(data)


def clusterization():
    data = read_data()
    print(data)
    id_user = data.shape[0] - 1
    Y_pred = clusterize(data, id_user)
    X_umap = UMAP().fit_transform(data)
    np.save(f'{project_path}/X_umap', X_umap)
    np.save(f'{project_path}/Y_pred', Y_pred)
    save_png(X_umap, Y_pred, id_user)


if __name__ == '__main__':
    if os.path.exists(f'{project_path}/X_umap.npy') and os.path.exists(f'{project_path}/Y_pred.npy'):
        X_umap = np.load(f'{project_path}/X_umap.npy')
        Y_pred = np.load(f'{project_path}/Y_pred.npy')
        save_png(X_umap, Y_pred)
    else:
        data = read_data()
        print(data)
        id_user = data.shape[0] - 1
        Y_pred = clusterize(data, id_user)
        X_umap = UMAP().fit_transform(data)
        np.save(f'{project_path}/X_umap', X_umap)
        np.save(f'{project_path}/Y_pred', Y_pred)
        save_png(X_umap, Y_pred, id_user)
