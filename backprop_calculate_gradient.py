import numpy as np

# logistic function
def logistic(x):
    return 1/(1+np.exp(-x))

# this is the derivative of logistic with respect to x
def dlogistic(x):
    u = logistic(x)
    return u*(1-u)

# forward propagation step for a single data point
def forwardprop(w1,w2,x):
    a0 = np.insert(x,0,1)  # insert bias unit at input layer
    z1 = w1.dot(a0)        # calculate input to hidden layer
    a1 = logistic(z1)      # calculate output from hidden layer
    a1 = np.insert(a1,0,1) # insert bias unit at hidden layer
    z2 = w2.dot(a1)        # calculate input to output layer
    a2 = logistic(z2)      # calculate output of neural network
    return a2,z2,a1,z1,a0

# the data and desired outputs
X = np.array([[0,0],[0,1],[1,0],[1,1]]).transpose()
y = np.array([0, 1, 1, 0])
m = X.shape[1]

# architecture
nin = X.shape[0]
nhid = 2
nout = 1

# randomize weights
np.random.seed(561999213) # ensures same randomization every time for everyone
w1 = (np.sqrt(6)/np.sqrt(nhid+nin+1))*2*(np.random.rand(nhid,nin+1)-0.5)
w2 = (np.sqrt(6)/np.sqrt(nhid+1+nout))*2*(np.random.rand(nout,nhid+1)-0.5)

# forward prop for the first data point
a2,z2,a1,z1,a0 = forwardprop(w1,w2,X[:,0])

# backprop to hidden layer
d2 = a2 - y[0]
dw2 = np.outer(d2,a1)

### Add your code here!
v2 = np.reshape(w2[:,1:],(nout,nhid))
d1 = v2.transpose().dot(d2)*dlogistic(z1)
dw1 = np.outer(d1,a0)
