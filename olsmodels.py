from ols import ols
import scipy as sp
from scipy import stats
import numpy as np

##header: 'mpg', 'cyl', 'disp', 'hp', 'wt', 'accel', 'yr', 'origin','name'
data = np.genfromtxt('ships.csv', delimiter=",",names=True, dtype="f8,i8,f8,f8,f8,f8,i8,i8,S25")

wt = data['wt']
cyl = data['cyl']
nmpg = data['nmpg'].transpose()
hp = data['hp']
disp = data['disp']

x1 = np.array([wt,cyl]).transpose()

# OLS Models
model1 = ols(nmpg,x1,'nmpg',['weight','cylinders'])

x2 = np.array([wt,cyl,hp,disp]).transpose()### Add code here!
model2 = ols(nmpg,x2,'nmpg',['wt','cyl','hp','disp'])

print model2.summary()### Add code here!
