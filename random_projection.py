import numpy as np
from sklearn import random_projection

# load data from csv into numpy arrays
data = np.genfromtxt('mixed-spectra-matrix.csv', delimiter=';')

# apply a Gaussian random projection
tx = random_projection.GaussianRandomProjection(n_components = 25) ### create the transformation object
data25 = tx.fit_transform(data)###  create the transformation
print data25
