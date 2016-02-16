import numpy as np

# load data from csv into numpy arrays
X = np.genfromtxt('mixed-spectra-matrix.csv', delimiter=';')

# mean center X
X = X - X.mean(1)[:, np.newaxis]

# calculate svd
U, s, Vh = np.linalg.svd(X)

# get the first 25 concepts
S25 = np.diag(s)[:, :25]### diagonalize s, keep only the first 25 columns
Vh25 = Vh[:25, :]### keep only the first 25 rows of Vh
X25 = X.dot(Vh25.T)### use Vh25 to transform X into 25 dimensions

# print X25 and the shape
print X25
print 'num rows, num cols\n', X25.shape
