import numpy as np
import pylab as pl
from scipy import stats

# load the data in
data = np.genfromtxt('ship-nmpg-imp.csv', delimiter=",", names=True, dtype="f8,i8,f8,f8,f8,f8,i8,i8,S25")

varnames = data.dtype.names

# we loop through names[1:-1] to skip nmpg and uid
for name in varnames[1:-1]:
  slope, intercept, r_value, p_value, std_err = stats.linregress(data[name], data['nmpg'])
  print "Comparing nmpg to %s" % name
  ## fill in the whitespace in the line below with the appropriate p_values
  print 'p value = ',  p_value    , '      log(pvalue) = ', np.log10(p_value)       , '\n'
