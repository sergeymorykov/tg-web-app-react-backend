import json
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load data from data.json
with open('data.json') as f:
    data = json.load(f)

# Convert data to a numpy array
data_array = np.array(data)

# Preprocess data (e.g., scale it)
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_array)

# Perform KMeans clustering
kmeans = KMeans(n_clusters=2)
kmeans.fit(data_scaled)

# Get cluster labels
labels = kmeans.labels_

print(labels)

