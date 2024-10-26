
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


if __name__ == '__main__':
    data = pd.read_json('c:/Users/ASUS/OneDrive/CODES/nodeJS/tg-web-app-react-backend/DB/data5.json').values.transpose()

    maxNumOfClusters = int(data.shape[0] / 2)
    optimalNumOfClusters = 1
    startError = KMeans(n_clusters=1).fit(data).inertia_
    for i in range(2, maxNumOfClusters):
        if KMeans(n_clusters=i).fit(data).inertia_ < startError / 3:
            optimalNumOfClusters = i
            break
    print(optimalNumOfClusters)
    kmeans = KMeans(n_clusters=optimalNumOfClusters).fit(data)

    # Получение значений классов после кластеризации
    Y_pred = kmeans.labels_

    X_pca = PCA(n_components=2).fit_transform(data)

    # Visualize the 2D space of the new features
    fig, ax = plt.subplots()
    ax.scatter(X_pca[:, 0], X_pca[:, 1], c=np.array(Y_pred))
    ax.set_xlabel('pca Component 1')
    ax.set_ylabel('pca Component 2')
    plt.show()