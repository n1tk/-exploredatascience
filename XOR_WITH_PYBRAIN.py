# Imports
import numpy as np
from pybrain.datasets            import ClassificationDataSet
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SigmoidLayer

# Data and outputs
X = np.array([[-1,-1],[-1,1],[1,-1],[1,1]]).transpose()
y = np.array([0, 1, 1, 0])
data = ClassificationDataSet(2,1)
for i in range(0,X.shape[1]):
    data.addSample(X[:,i],y[i])

### Add your code here!
#inLayer = LinearLayer(2)
#hiddenLayer = SigmoidLayer(4)
#outLayer = LinearLayer(1)
#build network
net = buildNetwork(2,4,1, hiddenclass=SigmoidLayer, outclass=SigmoidLayer)
#create BackpropTrainer
trainer = BackpropTrainer(net, dataset=data, learningrate=1, momentum=0.001, weightdecay=0.000001, batchlearning=True)
#train the network
trainer.trainEpochs( 3000 )
#or can be used :
for i in range(30):
    trainer.trainEpochs(99)
    trainer.verbose=True
    trainer.trainEpochs(1)
    trainer.verbose=False
