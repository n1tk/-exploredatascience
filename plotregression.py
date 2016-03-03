import numpy as np
import pylab as pl
from scipy import stats

# load the data in
data = np.genfromtxt('ship-nmpg-imp.csv', delimiter=",", names=True, dtype="f8,i8,f8,f8,f8,f8,i8,i8,S25")

varnames = data.dtype.names

# we loop through names[1:-1] to skip nmpg and uid
for name in varnames[1:-1]:
  slope, intercept, r_value, p_value, std_err = stats.linregress(data[name],data['nmpg'])
  print "Comparing nmpg to %s" % name
  print 'r_value = ',  r_value   ,'     r_sqrd = ',    r_value**2       , '\n'  ## add code here


  pl.figure()
  pl.scatter(data[name], data['nmpg'], color='#FF971C')
  Y = slope * data[name] + intercept
  pl.plot(data[name], Y, color='purple', alpha=0.5 ,linewidth=2)    ## add code beginning of line
  pl.title('%s model \n r^2= %s, log_pvalue= %s' % (name,r_value*r_value,np.log10(p_value)))
  pl.xlabel(name)
  pl.ylabel('NMPG')
  pl.xticks()
  pl.yticks()
  pl.show()
