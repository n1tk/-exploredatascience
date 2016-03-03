# Imports
import numpy as np
from scipy import stats
from pybrain.datasets import ClassificationDataSet

# Data and outputs
datain=np.loadtxt(open("beerdata.csv","rb"), delimiter=",", skiprows=0)
y = datain[:,0]-1           # 178x1 vector classifications
X = datain[:,1:]            # 178x13 matrix of data points
X = stats.zscore(X, axis=0) # normalize the data by feature
m = X.shape[0]              # number of data points

### Build a ClassificationDataSet data object and enter all of the data and classifications from X and y.

data = ClassificationDataSet(13)
for i in range(m):
    data.addSample(X[i,:],int(y[i]))
