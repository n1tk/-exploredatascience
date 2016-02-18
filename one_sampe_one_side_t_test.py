import numpy as np
import scipy.stats as stats
x2=np.loadtxt(open('damper2.csv','rb'))
nsamples = len(x2)
# create a t-distribution with nsamples-1 degrees of freedom
# t.pdf(x) and t.cdf(x) returns the value of the pdf and cdf at x respectively
t = stats.t(nsamples-1)
target = 1000.1
se2 = np.std(x2,ddof=1)/np.sqrt(nsamples)
tstat2 = (np.mean(x2)-target)/se2
print tstat2
