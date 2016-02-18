import numpy as np
import scipy.stats as stats
x1=np.loadtxt(open('damper1.csv','rb'))
nsamples = len(x1)
se1 = np.std(x1,ddof=1)/np.sqrt(nsamples)
target = 1000.1
tstat1 = (np.mean(x1)-target)/se1
print tstat1
