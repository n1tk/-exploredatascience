import numpy as np
import pylab as pl
from scipy import stats

#load the data in
data = np.genfromtxt('ship-nmpg-imp.csv', delimiter=",", names=True,
dtype="f8,i8,f8,f8,f8,f8,i8,i8,S25")
# renaming data vectors
weight = data['wt']
nmpg = data['nmpg']

## model2
slope,intercept, r_value, p_value, std_err = stats.linregress(weight,nmpg)
Y = slope*weight+intercept
resid = nmpg-Y

newshipweight = 135# add code here
prediction = slope*newshipweight+intercept# add code here
print prediction
