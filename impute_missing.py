import numpy as np
from scipy import stats

data = np.genfromtxt('ship-nmpg.csv', delimiter=",", names=True, dtype="f8,i8,f8,f8,f8,f8,i8,i8,S35")

hpmean = stats.nanmean(data['hp'])

hpmedian = stats.nanmedian(data['hp'])

imputeHP = np.round((hpmean + hpmedian)/ 2.0)


for i in range(len(data['hp'])):
  if np.isnan(data['hp'][i]):
     data['hp'][i] = imputeHP ## assign value here

np.savetxt('ship-nmpg-imp.csv',  data   , delimiter=',', newline='\n',fmt="%f,%i,%f,%f,%f,%f,%i,%i,%s")
