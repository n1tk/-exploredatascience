import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# load data from csv into numpy arrays
X = np.genfromtxt('mixed-spectra-matrix.csv', delimiter=';')

# do PCA on X
pca = PCA(n_components=2)###  instantiate the pca object

pcaX = pca.fit(X)###  fit the model

# plot tail off of components
plt.scatter(range(len(pca.explained_variance_)), pca.explained_variance_, color='#5D5166')
plt.title("Tail off of Principal Components")
plt.xlabel("Index of Principal Component")
plt.ylabel("Magnitude of Eigenvalue")
plt.show()
