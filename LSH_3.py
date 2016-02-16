import numpy as np
from sklearn import random_projection

# load data from csv into numpy arrays
data = np.genfromtxt('mixed-spectra-matrix.csv', delimiter=';')

# apply a Gaussian random projection
tx = random_projection.GaussianRandomProjection(n_components = 25)
data25 = tx.fit_transform(data)

# first define a transformation function to apply to each element
def tx01(x):
    return 0 if x < 0 else 1

# apply tx01 to each element using vectorize
vtx01 = np.vectorize(tx01)###  vectorize the tx01 function
data01 = vtx01(data25)### apply function to each element in data25
print data01
