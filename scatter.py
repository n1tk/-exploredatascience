import numpy as np
import pylab as pl

# load the data in
data = np.genfromtxt('ship-nmpg.csv', delimiter=",", names=True, dtype="f8,i8,f8,f8,f8,f8,i8,i8,S25")

varnames = ['nmpg', 'cyl', 'disp', 'hp', 'wt', 'accel', 'yr', 'origin','name']

# we loop through names[1:-1] to skip nmpg and uid
for name in varnames[1:-1]:
  pl.figure()
  pl.scatter(data[name], data['nmpg'] )##### use the scatter method to plot here #####
  pl.title("%s verses nmpg" % name)
  pl.xlabel(name)
  pl.ylabel('NMPG')
  pl.xticks()
  pl.yticks()
  pl.show()
