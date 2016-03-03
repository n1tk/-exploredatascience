# IMPORTS
import numpy as np
from pybrain.datasets            import SupervisedDataSet
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import TanhLayer
from pybrain.structure.modules   import LinearLayer

# LOAD DATA
datain=np.loadtxt(open("vespene.csv","rb"), delimiter=",", skiprows=0)

# NUMBER OF DATA POINTS
m = datain.shape[0]

# MEAN CENTER THE DATA
datain[:,0]=datain[:,0]-np.mean(datain[:,0])
datain[:,1]=datain[:,1]-np.mean(datain[:,1])

# DATA CLASS AND ENTRY
# data = ClassificationDataSet(1,1) <-- For classification
data = SupervisedDataSet(1,1) # For regression
for i in range(m):
    data.addSample(datain[i,0], datain[i,1])
net = buildNetwork(1, 10, 1 , hiddenclass=TanhLayer, outclass=LinearLayer) ### Create a network with 1 input unit, 10 hidden units, and 1 output unit that uses the tanh transfer function at the hidden layer and a linear output layer
trainer = BackpropTrainer(net, dataset=data, learningrate=0.00005, verbose=True) #Create a BackpropTrainer object with learningrate=0.00005 and verbose=True.
