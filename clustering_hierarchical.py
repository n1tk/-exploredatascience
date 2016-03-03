import numpy as np
import scipy
import pylab as pl
from matplotlib.pyplot import show
from scipy import cluster

#load the data
data = np.genfromtxt('zoo4.csv',delimiter=',',names=True)
labels = np.genfromtxt('zooLabels3.csv',delimiter=',',names=True,dtype=None)

#load the data into a numpy array
Xdata=np.array([data['hair'],data['feathers'],data['eggs'],data['milk'],data['airborne'],data['aquatic'],data['predator'],data['toothed'],data['backbone'],data['breathes'],data['venomous'],data['fins'],data['legs'],data['tail'],data['domestic'],data['catsize']]).transpose()

#transpose the labels
labs = np.array(labels['name']).transpose()

Z = scipy.cluster.hierarchy.average(Xdata) ### add method to cluster the data
print Z
