import numpy as np
import matplotlib.pyplot as plt

# load data from csv into numpy arrays
X = np.genfromtxt('mixed-spectra-matrix.csv', delimiter=';')

# subtract the mean from all columns of X
X = X - X.mean(1)[:, np.newaxis]

# calculate svd
U, s, Vh = np.linalg.svd(X)### calculate the SVD of X using numpy

# sizes of matricies
print 'U\ts\tVh\n', U.shape, s.shape, Vh.shape

# plot tail off of s
plt.scatter(range(len(U)), s, color='#5D5166') #U is the matrix of left singular vectors, s is an array of the singular values
plt.title("Tail off of Eigenvalues")
plt.xlabel("Index of Eigenvalue")
plt.ylabel("Magnitude of Eigenvalue")
plt.show()
