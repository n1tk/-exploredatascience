import numpy as np
import pylab as pl
from scipy import stats

#load the data in
data = np.genfromtxt('ship-nmpg-imp.csv', delimiter=",", names=True,
dtype="f8,i8,f8,f8,f8,f8,i8,i8,S25")

#varnames = ['nmpg', 'cyl', 'disp', 'hp', 'wt', 'accel', 'yr', 'origin','name']
varnames = data.dtype.names

# renaming data vectors for simplicity
weight = data['wt']
nmpg = data['nmpg']

print 'Model 1: Weight as a predictor for nmpg'

#Calculating the linear dependence between mpg and weight
slope,intercept, r_value, p_value, std_err = stats.linregress(weight,nmpg)
Y = slope*weight+intercept
resid = nmpg-Y
fig, (ax1,ax2) = pl.subplots(2)
ax1.scatter(weight, nmpg,  color='#FF971C')
ax1.plot(weight,Y, color='black')
ax1.set_xlabel('Weight')
ax1.set_ylabel('NMPG')

ax2.hist(resid, 40, color='#5D5166')
ax2.set_xlabel('Residuals')
ax2.set_ylabel('Frequency')

ax1.set_title('Weight Model')
pl.show()

print 'Model 2: log_weight as a predictor for nmpg'

logwt = np.log(weight)

#Calculating the linear dependence between mpg and log(     )
logslope, logintercept, logr,logp, log_err = stats.linregress(logwt,nmpg)
logY = logslope*logwt+logintercept
logresid = nmpg - logY

fig, (ax1,ax2) = pl.subplots(2)
ax1.scatter(logwt,nmpg, color='#FF971C')
ax1.plot(logwt,logY, color='black')
ax1.set_xlabel('Log(Weight)')
ax1.set_ylabel('NMPG')

ax2.hist(logresid, 40, color='#5D5166')
ax2.set_xlabel('Residuals of log model')
ax2.set_ylabel('Frequency')

ax1.set_title('Log(Weight) Model')
pl.show()
