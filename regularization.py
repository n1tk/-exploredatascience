import numpy as np
import pylab as pl
from pybrain.datasets            import SupervisedDataSet
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import TanhLayer
from pybrain.structure.modules   import LinearLayer

# FOR PLOTTING
def plot_networks(nets,x,y):
    pl.figure()
    pl.plot(x,y,'ok')
    xmin = min(x)
    xmax = max(x)
    x2 = np.linspace(xmin,xmax,200)
    data = SupervisedDataSet(1,1)
    for i in range(len(x2)):
        data.addSample([x2[i]], [0])
    colors = ['#5D5166','#FF971C','#447BB2','#B24449']
    for i in range(len(nets)):
        y2 = nets[i].activateOnDataset(data)
        pl.plot(x2,y2[:,0],color=colors[i],linewidth=1.8)
    pl.legend(('data','decay=0.0','decay=0.05','decay=0.5'), loc='upper left')
    pl.show()

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

### Add your code here!
# Don't forget to call your networks: net0, net1, etc.
net0 = buildNetwork(1,100,100,1, hiddenclass=TanhLayer, outclass=LinearLayer)
net1 = buildNetwork(1,100,100,1, hiddenclass=TanhLayer, outclass=LinearLayer)
net2 = buildNetwork(1,100,100,1, hiddenclass=TanhLayer, outclass=LinearLayer)
nets = [net0,net1,net2]
trainer0 = BackpropTrainer(net0, dataset=data, learningrate=0.005, weightdecay=0)
trainer1 = BackpropTrainer(net1, dataset=data, learningrate=0.005, weightdecay=0.05)
trainer2 = BackpropTrainer(net2, dataset=data, learningrate=0.005, weightdecay=0.5)
trainer0.trainEpochs(200)
trainer1.trainEpochs(200)
trainer2.trainEpochs(200)
# DON'T TOUCH CODE BELOW THIS
nets = [net0,net1,net2]
plot_networks(nets,datain[:,0],datain[:,1])
