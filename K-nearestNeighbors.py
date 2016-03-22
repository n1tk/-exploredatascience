import numpy as np
import scipy as sp
from sklearn.neighbors import NearestNeighbors
import numpy as np

seeds = np.genfromtxt('seeds.txt',delimiter='\t')
seed_labels = np.genfromtxt('seed_labels.txt',delimiter='\t')

type1mixed = np.array([[16.12, 15, 0.9, 5.709, 3.485, 2.27, 5.443]])

nbrs = NearestNeighbors(n_neighbors=10, algorithm='brute').fit(seeds)
distances, indices = nbrs.kneighbors(type1mixed)
print indices
