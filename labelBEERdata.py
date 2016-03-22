# Imports
import numpy as np
from scipy import stats
from pybrain.datasets            import ClassificationDataSet
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SigmoidLayer

# Import data
datain=np.loadtxt(open("beerdata.csv","rb"), delimiter=",", skiprows=0)

# Data and outputs
datain=np.loadtxt(open("beerdata.csv","rb"), delimiter=",", skiprows=0)
y = datain[:,0]-1           # 178x1 vector classifications
X = datain[:,1:]            # 178x13 matrix of data points
X = stats.zscore(X, axis=0) # normalize the data by feature
m = X.shape[0]              # number of data points

# Create classification data set
data = ClassificationDataSet(13)
for i in range(m):
    data.addSample(X[i,:],int(y[i]))

# Convert output to vector of binary values
data._convertToOneOfMany()

# Split into test and train data
tstdata, trndata = data.splitWithProportion(0.25)

### Add your code here!
net = buildNetwork(13,20,3, bias=True, outputbias=True, outclass=SigmoidLayer)
trainer = BackpropTrainer(net, dataset=trndata, learningrate=5, momentum=0.01, weightdecay=0, verbose=False)
for i in range(10):
    trainer.trainEpochs(9)
    c = trainer.train()
    print i,c
for inp,trgt in tstdata:
    print net.activate(inp),trgt